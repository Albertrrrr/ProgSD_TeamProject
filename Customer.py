"""
Introduction to Customer Class
"""
import pymysql
from pymysql import err

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
    def __init__(self, email, par=None):
        if par is None:
            oneSQL = "SELECT * FROM Customers WHERE email = %s"
            cursor.execute(oneSQL, email)
            oneData = cursor.fetchone()
            self.__id = oneData[0]
            self.__name = oneData[1]
            self.__password = oneData[2]
            self.__email = oneData[3]
            self.__balance = oneData[4]
        else:
            self.__id = currentID + 1
            self.__name = par[0]
            self.__password = par[1]
            self.__email = par[2]
            self.__balance = 5.5

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

    # update to database
    def add(self):
        saveSQL = "insert ignore into Customers(customerID,name,password,email,accountBalance)" \
                  "values(%s,%s,%s,%s,%s)"
        cursor.execute(saveSQL, (self.__id, self.name, self.password, self.__email, self.__balance))
        db.commit()
        print("Add a new customer successfully", self.__id, self.name, self.password, self.email, self.balance)

    def delete(self):
        deleteSQL = "delete from Customers where customerID = %s"
        cursor.execute(deleteSQL, self.__id)
        db.commit()
        print("Delete customer successfully", self.__id)

    def updateName(self, newName: str):
        self.__name = newName
        updateSQL = "update Customers set name = %s where customerID = %s"
        cursor.execute(updateSQL, (self.__name, self.__id))
        db.commit()
        print("Change successfully")

    def updatePassword(self, newPassword: str):
        self.__password = newPassword
        updateSQL = "update Customers set password = %s where customerID = %s"
        cursor.execute(updateSQL, (self.__password, self.__id))
        db.commit()
        print("Change successfully")

    def updateEmail(self, newEmail: str):
        deleteSQL = "delete from Customers where customerID = %s"
        cursor.execute(deleteSQL, self.__id)
        db.commit()

        saveSQL = "insert ignore into Customers(customerID,name,password,email,accountBalance)" \
                  "values(%s,%s,%s,%s,%s)"
        cursor.execute(saveSQL, (self.__id, self.name, self.password, newEmail, self.__balance))
        db.commit()

        print("Change successfully")

