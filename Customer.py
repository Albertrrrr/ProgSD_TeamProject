"""
Introduction to Customer Class
"""
import pymysql
from pay import pay
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
cursor.execute("SELECT * from Customers")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
# 拿到属于数据库的最后一个id
currentID = data[-1][0]

class Customer:
    def __init__(self, email=None):
        if email is None:
            pass
        else:
            oneSQL = "SELECT * FROM Customers WHERE email = %s"
            cursor.execute(oneSQL, email)
            oneData = cursor.fetchone()
            self.__id = oneData[0]
            self.__name = oneData[1]
            self.__password = oneData[2]
            self.__email = oneData[3]
            self.__balance = oneData[4]

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

    #增加customer par=[name,password,email]
    def add(self, par: list):

        self.__id = currentID + 1
        self.__name = par[0]
        self.__password = par[1]
        self.__email = par[2]
        self.__balance = 5.5

        saveSQL = "insert ignore into Customers(customerID,name,password,email,accountBalance)" \
                  "values(%s,%s,%s,%s,%s)"
        addFlag = cursor.execute(saveSQL, (self.__id, self.__name, self.__password, self.__email, self.__balance))
        db.commit()
        if addFlag:
            print("Add a new customer successfully", self.__id, self.__name, self.__password, self.__email, self.__balance)
            return True
        else:
            print("Change another email")
            return False


    #删除customer
    def delete(self):
        deleteSQL = "delete from Customers where customerID = %s"
        cursor.execute(deleteSQL, self.__id)
        db.commit()
        print("Delete customer successfully", self.__id)

    #更新名字
    def updateName(self, newName: str):
        self.__name = newName
        updateSQL = "update Customers set name = %s where customerID = %s"
        cursor.execute(updateSQL, (self.__name, self.__id))
        db.commit()
        print("Change successfully")

    #更新密码
    def updatePassword(self, newPassword: str):
        self.__password = newPassword
        updateSQL = "update Customers set password = %s where customerID = %s"
        cursor.execute(updateSQL, (self.__password, self.__id))
        db.commit()
        print("Change successfully")

    #更新邮件 主键
    def updateEmail(self, newEmail: str):
        deleteSQL = "delete from Customers where customerID = %s"
        cursor.execute(deleteSQL, self.__id)
        db.commit()

        saveSQL = "insert ignore into Customers(customerID,name,password,email,accountBalance)" \
                  "values(%s,%s,%s,%s,%s)"
        cursor.execute(saveSQL, (self.__id, self.name, self.password, newEmail, self.__balance))
        db.commit()

        print("Change successfully")

    def updateBalance(self,newBalance: str):
        self.__balance = newBalance
        updateSQL = "update Customers set accountBalance = %s where customerID = %s"
        cursor.execute(updateSQL, (self.__balance, self.__id))
        db.commit()
        print("Change successfully")

    def topUpBalance(self,topupNumber: float):
        current_time = datetime.datetime.now()
        time_string = current_time.strftime("%Y%m%d%H%_M%S_")
        out_trade_no = time_string + str(self.__id)
        payer = pay(out_trade_no,topupNumber,"15m")
        flag = payer.pay()
        if flag:
            self.__balance += topupNumber
            topUpBalanceSQL = "update Customers set accountBalance = %s where customerID = %s"
            cursor.execute(topUpBalanceSQL, (self.__balance, self.__id))
            db.commit()
            print("successfully top up account balance")
        else:
            print("top up account balance failed")



