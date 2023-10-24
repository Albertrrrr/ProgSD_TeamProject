import re

from Customer import Customer
import pymysql
from Operator import Operator
from Order import Order
from Vehicle import Vehicle
from vehicleStop import vehicleStop

mysql_config = {
    'host': '35.246.24.203',
    'port': 3306,
    'user': 'root',
    'passwd': '3022008a',
    'database': 'progSDTeamProject',
}
# connect to mysql
db = pymysql.connect(**mysql_config)


class app:
    def __init__(self):
        self.__customer = Customer()
        self.__operator = None
        self.__manager = None
        self.__bike = None
        self.__order = None
        self.__cost = None
        self.__error = None
        self.__reportCustomerID = None
        self.__QRcodeURL = None
        print("app running")

    # mysql configs

    # Customer Operator Manager 登陆
    def login(self, par: list):
        # email password
        currentEmail = par[0]
        currentPassword = par[1]
        option = par[2]
        cursor = db.cursor()

        if option == '1':
            oneSQL = "SELECT * FROM Customers WHERE email = %s"
            cursor.execute(oneSQL, currentEmail)
            db.commit()

        elif option == '2':
            oneSQL = "SELECT * FROM Operators WHERE email = %s"
            cursor.execute(oneSQL, currentEmail)
            db.commit()

        elif option == '3':
            oneSQL = "SELECT * FROM Manager WHERE email = %s"
            cursor.execute(oneSQL, currentEmail)
            db.commit()

        oneData = cursor.fetchone()

        try:
            rightPassword = oneData[2]
        except TypeError as e:
            return False  # 登陆失败 请检查邮箱名与密码

        # 生成不同操作者的对象
        if currentPassword == rightPassword:
            if option == '1':
                self.__customer = Customer(currentEmail)
            return True
        else:
            return False

    def register(self, par: list):
        # par : name:str,password:str,email:str
        customer = Customer()
        flag = customer.add(par)
        return flag

    # 之后改为从框中输入
    def enterCode(self):
        code = input("Enter code: ")
        return code

    # 注册operator 和 manager
    def registerOM(self, par: list):
        # 先生成code
        operator = Operator()
        # par : name:str,password:str,email:str
        operator.generateCode(par)
        userCode = self.enterCode()  # 之后修改
        flag = operator.add(userCode)
        return flag

    # 租车
    def rentVehicle(self, bikeID: int):
        self.__bike = Vehicle(self.__customer, bikeID)
        self.__order = Order(self.__customer, self.__bike)
        try:
            flag = self.__order.startRent()
        except Exception as e:
            unpaidOrder = self.__order.detailsFormat(self.__order.toPayOrder())
            id = str(unpaidOrder[0][0])
            startTime = unpaidOrder[0][3]
            cost = str(unpaidOrder[0][-5])
            self.__error = "You will need to pay id:" + id + " for a total of £" + cost + " for orders timed from: " + startTime  # get属性 可以拿到该值
            print(self.__error)
            return False
        return flag

    # 还车
    def returnVehicle(self, stopID: int):
        if self.__order is not None:
            stop = vehicleStop(stopID)
            flag = self.__order.endRent(stop)
            if flag is not None:
                return True
            else:
                return False
        else:
            return False

    # 支付 并关闭订单
    def payOrder(self):
        flag = self.__order.pay()
        if flag:
            flagClosed = self.__order.close()
            if flagClosed:
                return True
            else:
                return False
        else:
            return False

    # 单独支付订单
    def payToOrder(self):
        flag = self.__order.payTo()
        if flag:
            flagClosed = self.__order.close()
            if flagClosed:
                return True
            else:
                return False
        else:
            return False

    # 取消订单
    def cancelOrder(self):
        flag = self.__order.cancel()
        return flag

    # 客户报告
    def reportCustomer(self, bikeID: int):
        self.__bike = Vehicle(self.__customer, bikeID)
        self.__reportCustomerID = self.__bike.reportFix()
        # self.__reportCustomerID 存入到是 生成报告的id
        if self.__reportCustomerID is not None:
            return True
        else:
            return False

    # 生成QRCODE
    def generateQRcodeString(self, total: float):
        self.__QRcodeURL = self.__customer.generateQRCode(total)
        print(self.__QRcodeURL)
        if self.__QRcodeURL is not None:
            return True
        else:
            return False

    # 充值
    def topUp(self, total: float):
        QRcode = self.generateQRcodeString(total)
        if QRcode is not None:
            flag = self.__customer.topUpBalance()
            return flag
        else:
            return False

    # 更改Customer邮箱
    def updateCustomerEmail(self,newEmail:str):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if bool(re.match(pattern,newEmail)):
            flag = self.__customer.updateEmail(newEmail)
            return flag
        else:
            return False #修改邮箱 不是一个邮箱

    # 更改Customer名字
    def updateCustomerName(self,newName:str):
        flag = self.__customer.updateName(newName)
        return flag

    # 更改Customer密码
    def updateCustomerPassword(self,newPassword:str):
        flag = self.__customer.updatePassword(newPassword)
        return flag


if __name__ == '__main__':
    import time

    # 用户测试
    app = app()
    # par1 = ["Yuqing Ren", "9988", "renyuqing@gmail.com"]
    #
    # par2 = ["zhangruixian@gmail.com", "3022008a", '1']
    # par3 = ["renyuqing@gmail.com", "9988", '1']
    # par4 = ["zhangruixian@gmail.com", "3022008", '2']
    # print(app.login(par2))  # 测试登陆成功
    # print(app.login(par3))  # 测试登陆失败
    # print(app.login(par4))  # 测试登陆成功
    #
    # print(app.register(par1))
    # print(app.login(par3))
    #
    # print(app.registerOM(par1))

    # Customer功能测试 租车流程测试 正常全流程
    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008a", '1']
    # app.login(par)
    # app.rentVehicle(3)
    # time.sleep(10)
    # app.returnVehicle(2)
    # app.payOrder()
    """
    app running
    Login 'zhangruixian@gmail.com' successfully
    Successfully rent
    Add a new order id : 37 successfully from: zhangruixian@gmail.com
    Successfully return
    Change balance successfully
    successfully paid
    """

    # Customer功能测试 租车流程测试 非正常流程 需要支付后进行租车
    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008a", '1']
    # app.login(par)
    # app.rentVehicle(1)
    # app.returnVehicle(2)
    """
    app running
    Login 'zhangruixian@gmail.com' successfully
    Successfully rent
    Add a new order id : 35 successfully from: zhangruixian@gmail.com
    Successfully return
    """

    # Customer功能测试 租车流程测试 非正常流程 支付后租车
    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008a", '1']
    # app.login(par)
    # app.rentVehicle(1)
    # app.payToOrder()
    # app.rentVehicle(2)
    # app.returnVehicle(1)
    # app.payOrder()

    """
    app running
    Login 'zhangruixian@gmail.com' successfully
    You will need to pay id:35 for a total of £0.0 for orders timed from: 2023-10-24 19:37:42
    Change balance successfully
    successfully paid:  35
    Closed abnormal order:  35
    Successfully rent
    Add a new order id : 36 successfully from: zhangruixian@gmail.com
    Successfully return
    Change balance successfully
    successfully paid
    """

    # Customer 功能测试 生成报告
    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008a", '1']
    # app.login(par)
    # app.reportCustomer(2)
    """
    app running
    Login 'zhangruixian@gmail.com' successfully
    Add a new report successfully 13 The Bike needs to fix, id is : 2
    Successfully report
    
    数据库Vehicle status: reporting isLock: 1 已经上锁
        Report: 13	1	The Bike needs to fix, id is : 2	2023-10-24 19:45:23		0	0
    """

    # Customer 功能测试 充值
    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008a", '1']
    # app.login(par)
    # app.topUp(100) #生成金额最多两位

    """
    app running
    Login 'zhangruixian@gmail.com' successfully
    二维码保存成功！
    qrcode_image/qr_test_ali_20231024202355_1.png
    now sleep 1s
    not paid...
    now sleep 1s
    not paid...
    successfully top up account balance
    """
    # 测试更改 邮箱 密码 用户吗
    # app = app()
    # par = ["renyuqing@gmail.com", "9988", '1']
    # app.login(par)
    # app.updateCustomerName("Ren,Yuqing")
    # app.updateCustomerPassword("3022008a")
    # app.updateCustomerEmail("renyuqing5588@gmail.com") #修改邮箱后重新登录

    # app = app()
    # par = ["renyuqing5588@gmail.com", "9988", '1']
    # app.login(par)
    """
    app running
    Login 'renyuqing@gmail.com' successfully
    Change successfully
    Change successfully
    Change successfully
    
    app running
    Login 'renyuqing5588@gmail.com' successfully
    """


