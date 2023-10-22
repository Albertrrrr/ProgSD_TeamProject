import pymysql

from Records import Records
from Vehicle import Vehicle

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
cursor.execute("SELECT * from Operators")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
# 拿到属于数据库的最后一个id
try:
    currentID = data[-1][0]
except:
    currentID = 0


class OperatorError(Exception):
    pass


class Operator:
    def __init__(self, email=None):
        if email is None:
            self.__id = None
            self.__name = None
            self.__password = None
            self.__email = None
            self.__par = []
            pass
        else:

            oneSQL = "SELECT * FROM Operators WHERE email = %s"
            cursor.execute(oneSQL, email)
            oneData = cursor.fetchone()

            if oneData == None:
                raise OperatorError("You have to check your email and password")
            else:
                self.__id = oneData[0]
                self.__name = oneData[1]
                self.__password = oneData[2]
                self.__email = oneData[3]
                self.__par = []

                print("Login successfully")

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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def generateCode(self, par: list):
        self.__par = par

        cursor.execute("SELECT * from Operators_ver")
        data = cursor.fetchall()
        try:
            currentID = data[-1][0]
        except:
            currentID = 0

        self.__id = currentID + 1
        self.__name = self.__par[0]
        self.__password = self.__par[1]
        self.__email = self.__par[2]

        saveSQL = "insert ignore into Operators_ver(operatorID,name,password,email,code_ver)" \
                  "values(%s,%s,%s,%s,(LPAD(FLOOR(RAND() * 10000), 4, '0')))"
        addFlag = cursor.execute(saveSQL, (self.__id, self.__name, self.__password, self.__email))
        db.commit()

        if addFlag:
            print("Add a new Operators_ver successfully", self.__id, self.__name, self.__password, self.__email)
            return True
        else:
            print("Change another email")
            return False

    def add(self, code: str):

        codeSQL = "SELECT * FROM `Operators_ver` WHERE operatorID = %s"
        cursor.execute(codeSQL, self.__id)
        data = cursor.fetchone()
        code_ver = data[-1]

        if code == code_ver:
            saveSQL = "insert ignore into Operators(operatorID,name,password,email)" \
                      "values(%s,%s,%s,%s)"
            addFlag = cursor.execute(saveSQL, (self.__id, self.__name, self.__password, self.__email))
            db.commit()
            if addFlag:
                print("Add a new Operator successfully", self.__id, self.__name, self.__password, self.__email)
                return True
            else:
                print("Change another email")
                return False

    def delete(self):
        deleteSQL = "delete from Operators where operatorID = %s"
        cursor.execute(deleteSQL, self.__id)
        db.commit()
        print("Delete operator successfully", self.__id)

    # 更新名字
    def updateName(self, newName: str):
        self.__name = newName
        updateSQL = "update Operators set name = %s where operatorID = %s"
        cursor.execute(updateSQL, (self.__name, self.__id))
        db.commit()
        print("Change successfully")

    # 更新密码
    def updatePassword(self, newPassword: str):
        self.__password = newPassword
        updateSQL = "update Operators set password = %s where operatorID = %s"
        cursor.execute(updateSQL, (self.__password, self.__id))
        db.commit()
        print("Change successfully")

    # 更新邮件 主键
    def updateEmail(self, newEmail: str):
        self.__email = newEmail
        deleteSQL = "delete from Operators where operatorID = %s"
        cursor.execute(deleteSQL, self.__id)
        db.commit()

        saveSQL = "insert ignore into Operators(operatorID,name,password,email)" \
                  "values(%s,%s,%s,%s)"
        cursor.execute(saveSQL, (self.__id, self.__name, self.__password, self.__email))
        db.commit()

        print("Change successfully")

    def changeBattery(self, vehicle: Vehicle):
        operator = Operator(self.__email)
        vehicle.changeBatteryStatus()
        recordStr = 'change new battery'
        record = Records(operator, vehicle, recordStr)
        record.add()

    def addVehicle(self, vehicle: Vehicle, par: list):
        operator = Operator(self.__email)
        vehicle.add(par)
        recordStr = 'Add a new bike'
        record = Records(operator, vehicle, recordStr)
        record.add()

    def deleteVehicle(self, vehicle: Vehicle):
        operator = Operator(self.__email)
        vehicle.delete()
        recordStr = 'Delete the bike'
        record = Records(operator, vehicle, recordStr)
        record.add()

    def changeLocation(self, vehicle: Vehicle, newLocation: int):
        operator = Operator(self.__email)
        oldLocation = vehicle.locations
        vehicle.updateLocations(newLocation)
        recordStr = 'Change location: ' + str(oldLocation) + ' to ' + str(newLocation)
        record = Records(operator, vehicle, recordStr)
        record.add()

    def getLocation(self, vehicle: Vehicle):
        return vehicle.vehicleID

    def fixBike(self, vehicle: Vehicle):
        operator = Operator(self.__email)
        vehicle.fixing()
        recordStr = 'Fixing bike: ' + str(vehicle.vehicleID)
        record = Records(operator, vehicle, recordStr)
        record.add()

    def endFixBike(self, vehicle: Vehicle, reportID: int):
        operator = Operator(self.__email)
        vehicle.endFix(reportID, operator)
        recordStr = 'Fixing bike is done: ' + str(vehicle.vehicleID)
        record = Records(operator, vehicle, recordStr)
        record.add()


if __name__ == '__main__':
    from Customer import Customer
    import time
    # 新用户
    # operator = Operator()
    # par = ['RRR', '3022008a', 'zhangruixian98@gmail.com']
    # operator.generateCode(par)
    # flag = False
    # while not flag:
    #     code = input("Enter code: ")
    #     flag = operator.add(code)

    # 用户测试
    # flag = False
    # while not flag:
    #     email = input("Enter your email: ")
    #     try:
    #         operator = Operator(email)
    #         flag = True
    #     except OperatorError as e:
    #         print(e)
    #         continue

    # 更改email
    # newEmail = 'zhangruixian@gmail.com'
    # operator.updateEmail(newEmail)

    # newP_N = ['ZZZ','3022008']
    # #更改密码
    # operator.updateName(newP_N[0])
    # operator.updatePassword(newP_N[1])

    # 测试修改电池
    # operator = Operator("zhangruixian@gmail.com")
    # vehicle1 = Vehicle(None,1)
    # operator.changeBattery(vehicle1)

    # 测试添加车辆
    # operator = Operator("zhangruixian@gmail.com")
    # par = ['E-bike',2,'normal']
    # vehicle1 = Vehicle(None, None)
    # operator.addVehicle(vehicle1,par)

    # 测试删除车辆
    # operator = Operator("zhangruixian@gmail.com")
    # vehicle1 = Vehicle(None, 4)
    # operator.deleteVehicle(vehicle1)

    # 测试更改车辆位置
    # operator = Operator("zhangruixian@gmail.com")
    # vehicle1 = Vehicle(None, 3)
    # operator.changeLocation(vehicle1,1)

    # 测试修理
    # operator = Operator("zhangruixian@gmail.com")
    # vehicle1 = Vehicle(None, 2)
    # operator.fixBike(vehicle1)

    #测试修理结束 修理全过程
    operator = Operator("zhangruixian@gmail.com")
    customer = Customer("zhangyujia@gmail.com")
    vehicle1 = Vehicle(customer, 1)
    idReport = vehicle1.reportFix()
    time.sleep(5)
    operator.fixBike(vehicle1)
    time.sleep(5)
    operator.endFixBike(vehicle1,idReport)



