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
cursor.execute("SELECT * from Records")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
# 拿到属于数据库的最后一个id


class Records:
    def __init__(self,operator,vehicle,status: str):
        if operator is None:
            self.__id = None
            self.__email = None
            self.__date = None
            self.__bikeID = None
            self.__status = None

        else:
            cursor.execute("SELECT * from Records")
            # 使用 fetchone() 方法获取单条数据.
            data = cursor.fetchall()

            try:
                currentID = data[-1][0]
            except:
                currentID = 0

            self.__id = currentID + 1
            self.__email = operator.email

            current_time = datetime.datetime.now()
            startTime = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.__date = startTime
            self.__bikeID = vehicle.vehicleID
            self.__status = status
            print("Records:", self.__id)

    def add(self):
        saveSQL = "insert ignore into Records(recordID,operator,`date`,bikeID,status)" \
                  "values(%s,%s,%s,%s,%s)"
        addFlag = cursor.execute(saveSQL, (self.__id,self.__email,self.__date,self.__bikeID,self.__status ))
        db.commit()
        if addFlag:
            print("Add a new log successfully", self.__id,self.__email,self.__date,self.__bikeID,self.__status)
            return True
        else:
            print("Unsuccessfully")
            return False







