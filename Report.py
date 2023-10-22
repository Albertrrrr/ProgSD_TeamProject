from Customer import Customer
from Operator import Operator
import pymysql
import datetime
# mysql configs

mysql_config = {
    'host': '35.246.24.203',
    'port': 3306,
    'user': 'root',
    'passwd': '3022008a',
    'database': 'progSDTeamProject',
}
# connect to mysql
db = pymysql.connect(**mysql_config)
cursor = db.cursor()

cursor.execute("SELECT * from `Report`")
data = cursor.fetchall()
# 拿到属于数据库的最后一个id
currentID = data[-1][0]

class Report:
    def __init__(self,customer: Customer, operator: Operator,message: str):
        if operator is None:
            self.__reportID = currentID + 1
            self.__formID = customer.id
            self.__message = message
            current_time = datetime.datetime.now()
            date = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.__startTime = date
            self.__endTime = None
            self.__status = 0
            self.__authen = 0
        elif customer is None:
            self.__reportID = currentID + 1
            self.__formID = operator.id
            self.__message = message
            current_time = datetime.datetime.now()
            date = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.__startTime = date
            self.__endTime = None
            self.__status = 0
            self.__authen = 1

    @property
    def formID(self):
        return self.__formID

    @formID.setter
    def formID(self, value):
        self.__formID = value

    @property
    def endTime(self):
        return self.__endTime

    @endTime.setter
    def endTime(self, value):
        self.__endTime = value

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value

    @property
    def startTime(self):
        return self.__startTime

    @startTime.setter
    def startTime(self, value):
        self.__startTime = value

    @property
    def reportID(self):
        return self.__reportID

    @reportID.setter
    def reportID(self, value):
        self.__reportID = value

    @property
    def authen(self):
        return self.__authen

    @authen.setter
    def authen(self, value):
        self.__authen = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def report(self):
        reportSQL = "insert into `Report`(reportID,fromID,message,startTime,endTIme,status,authen) values(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(reportSQL, (self.__reportID,self.__formID,self.__message,self.__startTime,self.__endTime,self.__status,self.__authen))
        db.commit()
        print("Add a new report successfully", self.__reportID, self.__message)

    #done 方法之后要修改为manager修改 传入manager对象才能进行修改
    def done(self,reportID: int):
        current_time = datetime.datetime.now()
        self.__endTime = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.__status = 1

        doneSQL = "update `Report` set endTime = %s,status = %s where reportID = %s"
        cursor.execute(doneSQL, (self.__endTime, self.__status, reportID))
        db.commit()

        print("Successfully, processed the report id: ", reportID)

    def reportDetails(self):
        flagSQL = 'SELECT * FROM `Report` WHERE fromID = %s And authen = %s'
        cursor.execute(flagSQL, (self.__formID,self.__authen))
        details = cursor.fetchall()
        return details

    def detailsFormat(self,details: tuple):
        detailsList = list(details)
        res = []
        for i in detailsList:
            for j in range(3,5):
                i = list(i)
                i[j] = i[j].strftime("%Y-%m-%d %H:%M:%S")
            res.append(i)
        return res

    def update(self,message:str,reportID:int):
        self.__message = message
        current_time = datetime.datetime.now()
        self.__startTime = current_time.strftime("%Y-%m-%d %H:%M:%S")
        updateSQL = "update `Report` set message = %s,startTime = %s where reportID = %s"
        cursor.execute(updateSQL, (self.__message, self.__startTime, reportID))
        db.commit()
        print("Successfully, updates the report id: ", reportID)


if __name__ == '__main__':
    customer = Customer("zhangruixian@gmail.com")
    rep = Report(customer,None,"")
    detail = rep.reportDetails()
    res = rep.detailsFormat(detail)
    for i in res:
        print(i)

    rep.update("Update",4)

    detail = rep.reportDetails()
    res = rep.detailsFormat(detail)
    for i in res:
        print(i)








