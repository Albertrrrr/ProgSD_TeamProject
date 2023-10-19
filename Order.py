import pymysql
import datetime
from Customer import Customer

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

cursor.execute("SELECT * from `Order`")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
# 拿到属于数据库的最后一个id
currentID = data[-1][0]


class OrderError(Exception):
    pass


class Order:
    # par 格式 email, vehicleID
    def __init__(self, customer: Customer):
        self.__email = customer.email
        renter_id = customer.id

        flagSQL = 'SELECT * FROM `Order` WHERE renter = %s'
        cursor.execute(flagSQL,renter_id)
        orderList = cursor.fetchall()

        self.__isFlag = True
        for i in orderList:
            if i[9] == '0':
                self.__isFlag = False

        if self.__isFlag:
            current_time = datetime.datetime.now()
            startTime = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.__id = currentID + 1
            self.__renterID = renter_id
            self.__bikeID = 1 #之后修改
            self.__startTime = startTime
            self.__endTime = None

            current_time = datetime.datetime.now()
            creatTime = current_time.strftime("%Y-%m-%d %H:%M:%S")

            self.__createTime = creatTime
            self.__finishTime = None
            self.__cost = 0
            self.__isPaid = 0
            self.__isFlag = 1
            self.__status = 0

        else:
            self.__isFlag = 0

    @property
    def endTime(self):
        return self.__endTime

    @endTime.setter
    def endTime(self, value):
        self.__endTime = value

    @property
    def isPaid(self):
        return self.__isPaid

    @isPaid.setter
    def isPaid(self, value):
        self.__isPaid = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def isFlag(self):
        return self.__isFlag

    @isFlag.setter
    def isFlag(self, value):
        self.__isFlag = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def bikeID(self):
        return self.__bikeID

    @bikeID.setter
    def bikeID(self, value):
        self.__bikeID = value

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        self.__cost = value

    @property
    def renterID(self):
        return self.__renterID

    @renterID.setter
    def renterID(self, value):
        self.__renterID = value

    @property
    def startTime(self):
        return self.__startTime

    @startTime.setter
    def startTime(self, value):
        self.__startTime = value

    @property
    def finishTime(self):
        return self.__finishTime

    @finishTime.setter
    def finishTime(self, value):
        self.__finishTime = value

    @property
    def createTime(self):
        return self.__createTime

    @createTime.setter
    def createTime(self, value):
        self.__createTime = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def startRent(self):
        if len(dir(self)) == 48:
            raise OrderError("You have a unpaid order, please pay it")
        else:
            startSQL = "insert into `Order`(orderID,renter,bike,startTime,endTime,createTime,finishTime,cost,isPaid,status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(startSQL, (self.__id, self.__renterID, self.__bikeID, self.__startTime, self.__endTime,
                                      self.__createTime,self.__finishTime,self.__cost,self.__isPaid,self.__status))
            db.commit()
            print("Add a new order successfully",self.__email)


    def endRent(self):
        current_time = datetime.datetime.now()
        self.__endTime = current_time.strftime("%Y-%m-%d %H:%M:%S")

        stat = datetime.datetime.strptime(self.__startTime, "%Y-%m-%d %H:%M:%S")
        end = datetime.datetime.strptime(self.__endTime, "%Y-%m-%d %H:%M:%S")

        time_difference = end -stat
        seconds = time_difference.total_seconds()

        self.__cost = seconds * 0.05

        updateSQL = "update `Order` set endTime = %s,cost = %s where orderID = %s"
        cursor.execute(updateSQL, (self.__endTime, self.__cost, self.__id))
        db.commit()

        return self.__cost

    def pay(self):
        customer = Customer(self.__email,par=None)
        accountBalance = customer.balance
        if accountBalance >= self.__cost:
            accountBalance -= self.__cost
            customer.updateBalance(accountBalance)
            self.__isPaid = 1
            updateSQL = "update `Order` set isPaid = %s where orderID = %s"
            cursor.execute(updateSQL, (self.__isPaid, self.__id))
            db.commit()
            print("successfully paid")
            return True
        else:
            return False

    def close(self):
        if self.__isPaid:
            current_time = datetime.datetime.now()
            self.__finishTime = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.__status = 1

            updateSQL = "update `Order` set finishTime = %s,status = %s where orderID = %s"
            cursor.execute(updateSQL, (self.__finishTime, self.__status, self.__id))
            db.commit()

    def orderDetails(self):
        flagSQL = 'SELECT * FROM `Order` WHERE renter = %s'
        cursor.execute(flagSQL, self.__renterID)
        details = cursor.fetchall()
        return details

    def detailsFormat(self,details: tuple):
        detailsList = list(details)
        res = []
        for i in detailsList:
            for j in range(3,7):
                i = list(i)
                i[j] = i[j].strftime("%Y-%m-%d %H:%M:%S")
            res.append(i)
        return res
    def cancel(self):
        stat = datetime.datetime.strptime(self.__startTime, "%Y-%m-%d %H:%M:%S")
        current_time = datetime.datetime.now()
        time = current_time - stat
        second = time.total_seconds()
        if second < 60:
            self.pay()
            self.close()
            print("Cancel Successfully")

    def payTo(self,id: int):
        customer = Customer(self.__email, par=None)
        accountBalance = customer.balance
        idSQL = 'SELECT * FROM `Order` WHERE orderID = %s'
        cursor.execute(idSQL, id)
        index = cursor.fetchone()
        cost = index[-3]

        if accountBalance >= cost:
            accountBalance -= cost
            customer.updateBalance(accountBalance)
            isPaid = 1
            updateSQL = "update `Order` set isPaid = %s where orderID = %s"
            cursor.execute(updateSQL, (isPaid, id))
            db.commit()
            print("successfully paid: ", id)

            current_time = datetime.datetime.now()
            finishTime = current_time.strftime("%Y-%m-%d %H:%M:%S")
            status = 1

            updateSQL = "update `Order` set finishTime = %s,status = %s where orderID = %s"
            cursor.execute(updateSQL, (finishTime, status, id))
            db.commit()

            print("Closed abnormal order: ", id)

            return True
        else:
            return False


if __name__ == '__main__':
    import time
    from Customer import Customer

    customer = Customer("zhangruixian@gmail.com")
    order1 = Order(customer)
    try:
        order1.startRent()
    except OrderError as e:
        print(e)
        pass

    order1.payTo(12)
    order2 = Order(customer)

    #order1.cancel()

    # time.sleep(10)
    # order1.endRent()
    # flag = order1.pay()
    # if flag:
    #     order1.close()
    #
    # details = order1.orderDetails()
    # dList = order1.detailsFormat(details)
    # for i in dList:
    #     print(i)








