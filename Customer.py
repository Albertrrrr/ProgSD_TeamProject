"""
Introduction to Customer Class
"""
import pymysql
from pay import pay
import datetime
from config import mysql_config

# mysql configs


class CustomerError(Exception):
    pass


class Customer:
    def __init__(self, email=None):

        # connect to mysql
        self.__db = pymysql.connect(**mysql_config)
        self.__cursor = self.__db.cursor()

        self.__cursor.execute("SELECT * from Customers ORDER BY customerID")
        # 使用 fetchone() 方法获取单条数据.
        data = self.__cursor.fetchall()


        try:
            currentID = data[-1][0]
        except:
            currentID = 0

        if email is None:
            self.__id = currentID + 1
            self.__name = None
            self.__password = None
            self.__email = None
            self.__balance = None
            self.__out_trade_no = None
            self.__topUpNUmber = None
            pass
        else:

            oneSQL = "SELECT * FROM Customers WHERE email = %s"
            self.__cursor.execute(oneSQL, email)
            oneData = self.__cursor.fetchone()

            if oneData == None:
                raise CustomerError("You have to check your email and password")
            else:
                self.__id = oneData[0]
                self.__name = oneData[1]
                self.__password = oneData[2]
                self.__email = oneData[3]
                self.__balance = oneData[4]
                self.__out_trade_no = None
                self.__topUpNUmber = None
                self.__payer = None

                print("Login '" + self.__email + "' successfully")

    @property
    def out_trade_no(self):
        return self.__out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self.__out_trade_no = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    # 增加customer par=[name,password,email]
    def add(self, par: list):
        self.__name = par[0]
        self.__password = par[1]
        self.__email = par[2]
        self.__balance = 5.5

        saveSQL = "insert ignore into Customers(customerID,name,password,email,accountBalance)" \
                  "values(%s,%s,%s,%s,%s)"
        addFlag = self.__cursor.execute(saveSQL, (self.__id, self.__name, self.__password, self.__email, self.__balance))
        self.__db.commit()
        if addFlag:
            print("Add a new customer successfully", self.__id, self.__name, self.__password, self.__email,
                  self.__balance)
            return True
        else:
            print("Change another email")
            return False

    # 删除customer 在manager中补充
    def delete(self):
        deleteSQL = "delete from Customers where customerID = %s"
        flag = self.__cursor.execute(deleteSQL, self.__id)
        self.__db.commit()
        if flag == 0:
            print("Change unsuccessfully")
            return False
        else:
            print("Delete customer successfully", self.__id)
            return True


    # 更新名字
    def updateName(self, newName: str):
        self.__name = newName
        updateSQL = "update Customers set name = %s where customerID = %s"
        flag = self.__cursor.execute(updateSQL, (self.__name, self.__id))
        self.__db.commit()
        if flag:
            print("Change successfully")
            return True
        else:
            print("Change unsuccessfully")
            return False


    # 更新密码
    def updatePassword(self, newPassword: str):
        self.__password = newPassword
        updateSQL = "update Customers set password = %s where customerID = %s"
        flag = self.__cursor.execute(updateSQL, (self.__password, self.__id))
        self.__db.commit()
        if flag:
            print("Change successfully")
            return True
        else:
            print("Change unsuccessfully")
            return False

    # 更新邮件 主键
    def updateEmail(self, newEmail: str):
        deleteSQL = "delete from Customers where customerID = %s"
        self.__cursor.execute(deleteSQL, self.__id)
        self.__db.commit()

        saveSQL = "insert ignore into Customers(customerID,name,password,email,accountBalance)" \
                  "values(%s,%s,%s,%s,%s)"
        flag = self.__cursor.execute(saveSQL, (self.__id, self.name, self.password, newEmail, self.__balance))
        self.__db.commit()

        if flag:
            print("Change successfully")
            return True
        else:
            print("Change unsuccessfully")
            return False

    def updateBalance(self, newBalance: str):
        self.__balance = newBalance
        updateSQL = "update Customers set accountBalance = %s where customerID = %s"
        self.__cursor.execute(updateSQL, (self.__balance, self.__id))
        self.__db.commit()
        print("Change balance successfully")

    def generateQRCode(self, topUpNumber: float):
        current_time = datetime.datetime.now()
        time_string = current_time.strftime("%Y%m%d%H%M%S_")
        self.__out_trade_no = time_string + str(self.__id)
        self.__topUpNUmber = topUpNumber
        self.__payer = pay(self.__out_trade_no, self.__topUpNUmber, "15m")
        self.__payer.generateQRcode()
        QRcodeURL = 'qrcode_image/qr_test_ali' + '_' + self.out_trade_no + '.png'
        return QRcodeURL

    def topUpBalance(self):
        flag = self.__payer.pay()
        if flag:
            self.__balance += self.__topUpNUmber
            topUpBalanceSQL = "update Customers set accountBalance = %s where customerID = %s"
            self.__cursor.execute(topUpBalanceSQL, (self.__balance, self.__id))
            self.__db.commit()
            print("successfully top up account balance")
            return True
        else:
            print("top up account balance failed")
            return False

    def detailsFormat(self, details: tuple):
        detailsList = list(details)
        res = []
        for i in detailsList:
            res.append(list(i))
        return res

    def orderDetails(self):
        print(self.__id)
        flagSQL = 'SELECT orderID,bike,startStop,endStop,startTime,endTime,createTime,finishTime,cost,isPaid,status FROM `Order` WHERE renter = %s'
        self.__cursor.execute(flagSQL, self.__id)
        self.__db.commit()
        details = self.__cursor.fetchall()
        res = self.detailsFormat(details)
        for i in res:
            for k in range(4,8):
                if i[k] is not None:
                    i[k] = i[k].strftime("%Y-%m-%d %H:%M:%S")
                else:
                    i[k] = 'None'

            for j in range(9,11):
                if i[j] == 1 or i[j] == '1':
                    i[j] = "True"
        return res

    def reportDetails(self):
        flagSQL = 'SELECT reportID,message,startTime,endTime,status FROM `Report` WHERE fromID = %s'
        self.__cursor.execute(flagSQL, self.__id)
        details = self.__cursor.fetchall()
        res = self.detailsFormat(details)
        for i in res:
            for k in range(2, 4):
                i[k] = i[k].strftime("%Y-%m-%d %H:%M:%S")

            if i[-2] == 1 or i[-2] == '1':
                    i[-2] = "True"
        return res

    def unpaidDetails(self):
        flagSQL = 'SELECT orderID,bike,startTime,cost,isPaid FROM `Order` WHERE renter = %s and isPaid = 0'
        self.__cursor.execute(flagSQL, self.__id)
        self.__db.commit()
        details = self.__cursor.fetchall()
        key = self.detailsFormat(details)
        res = []
        for i in key:
            i[2] = i[2].strftime("%Y-%m-%d %H:%M:%S")
            finalString = "{:<5} {:<5} {:<20} {:<8} {:<5}".format(*i)
            res.append(finalString)
        tableHead = "{:<5} {:<5} {:<20} {:<8} {:<5}".format(
            "ID", "BIKE", "START_TIME", "COST", "ISPAID")
        res.insert(0, tableHead)

        return res




