import pymysql
import datetime
from Customer import Customer
from Vehicle import Vehicle
from vehicleStop import vehicleStop
from config import mysql_config



class OrderError(Exception):
    pass


class Order:
    # par 格式 email, vehicleID
    def __init__(self, customer: Customer, vehicle:Vehicle):

        # connect to mysql
        self.__db = pymysql.connect(**mysql_config)
        self.__cursor = self.__db.cursor()

        self.__cursor.execute("SELECT * from `Order`")
        # 使用 fetchone() 方法获取单条数据.
        data = self.__cursor.fetchall()
        self.__db.commit()
        # 拿到属于数据库的最后一个id
        try:
            currentID = data[-1][0]
        except:
            currentID = 0

        if vehicle is None:
            self.__customer = customer
            self.__renterID = self.__customer.id
            self.__email = self.__customer.email
            self.__vehicle = None
            self.__id = None
            self.__bikeID = None
            self.__startTime = None
            self.__endTime = None
            self.__createTime = None
            self.__finishTime = None
            self.__cost = 0
            self.__isFlag = 1
            self.__status = 0
            self.__isPaid = 0
            self.__startStop = None
            self.__endStop = None

        else:
            self.__customer = customer
            self.__email = self.__customer.email
            self.__vehicle = vehicle

            current_time = datetime.datetime.now()
            startTime = current_time.strftime("%Y-%m-%d %H:%M:%S")

            self.__id = currentID + 1
            self.__renterID = self.__customer.id
            self.__bikeID = vehicle.vehicleID
            self.__startTime = startTime
            self.__endTime = None

            current_time = datetime.datetime.now()
            creatTime = current_time.strftime("%Y-%m-%d %H:%M:%S")

            self.__createTime = creatTime
            self.__finishTime = None

            self.__cost = 0
            self.__isFlag = 1
            self.__status = 0
            self.__isPaid = 0

            self.__startStop = vehicle.locations
            self.__endStop = None

            flagSQL = 'SELECT * FROM `Order` WHERE renter = %s'
            self.__cursor.execute(flagSQL, self.__renterID)
            orderList = self.__cursor.fetchall()

            for i in orderList:
                if i[9] == '0':
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
        if  self.__isFlag == 0:
            raise OrderError("You have a unpaid order, please pay it")
        else:
            self.__vehicle.rent()
            self.__bikeID = self.__vehicle.vehicleID
            startSQL = "insert into `Order`(orderID,renter,bike,startTime,endTime,createTime,finishTime,cost,isPaid,status,startStop,endStop) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.__cursor.execute(startSQL, (self.__id, self.__renterID, self.__bikeID, self.__startTime, self.__endTime,
                                      self.__createTime, self.__finishTime, self.__cost, self.__isPaid, self.__status,self.__startStop,self.__endStop))
            self.__db.commit()
            print("Add a new order id : " + str(self.__id) + " successfully from: " + self.__email)
            return True

    def endRent(self, stop: vehicleStop):
        self.__endStop = stop.id
        current_time = datetime.datetime.now()
        self.__endTime = current_time.strftime("%Y-%m-%d %H:%M:%S")

        stat = datetime.datetime.strptime(self.__startTime, "%Y-%m-%d %H:%M:%S")
        end = datetime.datetime.strptime(self.__endTime, "%Y-%m-%d %H:%M:%S")

        time_difference = end - stat
        seconds = time_difference.total_seconds()

        self.__cost = seconds * self.__vehicle.price  # 已修改

        if self.__vehicle.types == "E-bike":
            self.__vehicle.batteryDiscount(seconds)

        self.__vehicle.returnBike(stop)


        updateSQL = "update `Order` set endTime = %s,cost = %s,endStop = %s where orderID = %s"
        flag = self.__cursor.execute(updateSQL, (self.__endTime, self.__cost, self.__endStop, self.__id))
        self.__db.commit()

        if flag == 1:
            return True
        else:
            return False

    def pay(self):
        accountBalance = self.__customer.balance
        if accountBalance >= self.__cost:
            accountBalance -= self.__cost
            self.__customer.updateBalance(accountBalance)
            self.__isPaid = 1
            updateSQL = "update `Order` set isPaid = %s where orderID = %s"
            self.__cursor.execute(updateSQL, (self.__isPaid, self.__id))
            self.__db.commit()
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
            self.__cursor.execute(updateSQL, (self.__finishTime, self.__status, self.__id))
            self.__db.commit()
            return True
        else:
            return False


    def orderDetails(self):
        flagSQL = 'SELECT * FROM `Order` WHERE renter = %s'
        print(self.__renterID)
        self.__cursor.execute(flagSQL, self.__renterID)
        self.__db.commit()
        details = self.__cursor.fetchall()

        return details

    def detailsFormat(self, details: tuple):
        detailsList = list(details)
        res = []
        for i in detailsList:
            for j in range(3, 7):
                i = list(i)
                if i[j] is not None:
                    i[j] = i[j].strftime("%Y-%m-%d %H:%M:%S")
                else:
                    i[j] = None
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
            return True
        else:
            return False

    def toPayOrder(self):
        toPaySQL = 'SELECT orderID,startTime,cost,isPaid FROM `Order` WHERE renter = %s AND isPaid = 0'
        cursor.execute(toPaySQL, self.__renterID)
        toPayDetail = cursor.fetchall()
        res = self.topayFormat(toPayDetail)
        return res
    def topayFormat(self, details:tuple):
        details = list(details)
        res = []
        tableHead = "{:<5} {:<20} {:<5} {:<5}".format("ID", "START_TIME", "COST", "STATUS")
        res.append(tableHead)
        for i in details:
            i = list(i)
            i[1] = i[1].strftime("%Y-%m-%d %H:%M:%S")
            if i[3] == 0:
                i[3] = "not paid"
            finalString = "{:<5} {:<20} {:<5} {:<5}".format(*i)
            res.append(finalString)
        return res

    def payTo(self):
        accountBalance = self.__customer.balance
        idSQL = 'SELECT * FROM `Order` WHERE renter = %s AND isPaid = 0'
        self.__cursor.execute(idSQL, self.__renterID)
        self.__db.commit()
        index = self.__cursor.fetchone()
        print(index)
        try:
            self.__cost = index[-5]
            self.__id = index[0]
        except TypeError:
            return False

        if accountBalance >= self.__cost:
            accountBalance -= self.__cost
            self.__customer.updateBalance(accountBalance)
            self.__isPaid = 1
            updateSQL = "update `Order` set isPaid = %s where orderID = %s"
            self.__cursor.execute(updateSQL, (self.__isPaid, self.__id))
            self.__db.commit()
            print("successfully paid: ", self.__id)

            current_time = datetime.datetime.now()
            self.__finishTime = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.__status = 1

            updateSQL = "update `Order` set finishTime = %s,status = %s where orderID = %s"
            self.__cursor.execute(updateSQL, (self.__finishTime, self.__status, self.__id))
            self.__db.commit()

            self.__isFlag = 1
            self.__isPaid = 1
            self.close()
            print("Closed abnormal order: ", self.__id)

            return True
        else:
            return False


if __name__ == '__main__':
    import time
    # from Customer import Customer
    # zyj = "zhangyujia@gmail.com"
    # zrx = "zhangruixian@gmail.com"
    # zjn = "zhengjunan@yahool.com"
    #
    # customer = Customer(zjn)
    # vehicle = Vehicle(customer, 2)
    # order1 = Order(customer,vehicle)
    # stop = vehicleStop(1)
    #
    # print(order1.detailsFormat(order1.orderDetails()))
    #
    # try:
    #     order1.startRent()
    # except OrderError as e:
    #     print(order1.detailsFormat(order1.toPayOrder()))
    #     order1.payTo()
    #     order1.startRent()
    #     pass
    #
    # time.sleep(8)
    # order1.endRent(stop)
    # order1.pay()
    # order1.close()

    # order1.cancel()

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
