import random
import re

from Customer import Customer
import pymysql
from Operator import Operator
from Order import Order
from Vehicle import Vehicle, VehicleCapacityError
from vehicleStop import vehicleStop
from Manager import Manager

mysql_config = {
    'host': '35.246.24.203',
    'port': 3306,
    'user': 'root',
    'password': '3022008a',
    'database': 'progSDTeamProject',
}
# connect to mysql
db = pymysql.connect(**mysql_config)


class app:
    def __init__(self):
        self.__customer = None
        self.__operator = None
        self.__manager = None
        self.__bike = None
        self.__order = None
        self.__cost = None
        self.__error = None
        self.__QRcodeURL = None
        self.__stop = None
        self.__bikeID = None
        self.__unpaidOrder = None
        self.__stopID = None
        self.__code_ver = None
        print("app running")

    @property
    def stopID(self):
        return self.__stopID

    @stopID.setter
    def stopID(self, value):
        self.__stopID = value

    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, value):
        self.__manager = value

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, value):
        self.__operator = value

    @property
    def bike(self):
        return self.__bike

    @bike.setter
    def bike(self, value):
        self.__bike = value

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        self.__cost = value

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def error(self):
        return self.__error

    @error.setter
    def error(self, value):
        self.__error = value

    @property
    def QRcodeURL(self):
        return self.__QRcodeURL

    @QRcodeURL.setter
    def QRcodeURL(self, value):
        self.__QRcodeURL = value

    @property
    def stop(self):
        return self.__stop

    @stop.setter
    def stop(self, value):
        self.__stop = value

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
            oneSQL = "SELECT * FROM Managers WHERE email = %s"
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
                return 1  # 返回1 说明是Customer 根据1的值 生成相对应的页面
            if option == '2':
                self.__operator = Operator(currentEmail)
                return 2  # 返回2 说明是Operator 根据2的值 生成相对应的页面
            if option == '3':
                self.__manager = Manager(currentEmail)
                return 3  # 返回2 说明是Operator 根据2的值 生成相对应的页面

        else:
            return False

    def register(self, par: list):
        # par : name:str,password:str,email:str
        customer = Customer()
        flag = customer.add(par)
        return flag

    # 之后改为从框中输入
    def generateCodeOP(self,par: list,option: str):
        if option == '2':
            self.__operator = Operator()
            # par : name:str,password:str,email:str
            self.__code_ver = self.__operator.generateCode(par)
        if option == '3':
            self.__manager = Manager()
            self.__code_ver = self.__manager.generateCode(par)

        return self.__code_ver

    def flagCode(self):
        if self.__code_ver is None:
            return False
        else:
            return True

    # 注册operator 和 manager
    def registerOM(self, par: list, code:str, option: str):
        # option 2 is operator
        if option == '2':
            if code == self.__code_ver:
                flag = self.__operator.add()
                return flag

        if option == '3':
            if code == self.__code_ver:
                flag = self.__manager.add()
                return flag

    """
    Customer接口方法  包括 租车 还车 支付 单独支付 报告维修 充值余额（内置生成QR码） 更改姓名 邮箱 密码 
    """

    # 租车
    def rentVehicle(self, bikeID: int):
        self.__bikeID = bikeID
        self.__bike = Vehicle(self.__customer, self.__bikeID)
        self.__order = Order(self.__customer, self.__bike)
        try:
            flag = self.__order.startRent()
        except Exception as e:
            # self.__unpaidOrder = self.__order.detailsFormat(self.__order.toPayOrder())
            # id = str(self.__unpaidOrder[0][0])
            # startTime = self.__unpaidOrder[0][3]
            # cost = str(self.__unpaidOrder[0][-5])
            # self.__error = "You will need to pay id:" + id + " for a total of £" + cost + " for orders timed from: " + startTime  # get属性 可以拿到该值
            # print(self.__error)
            flag = False
        return flag

    # 还车
    def returnVehicle(self, stopID: int):
        if self.__order is not None:
            self.__stop = vehicleStop(stopID)
            flag = self.__order.endRent(self.__stop)
            return flag
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
        self.__order = Order(self.__customer,None)
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
        flag = self.__bike.reportFix()
        # self.__reportCustomerID 存入到是 生成报告的id
        return flag

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
        QRcode = self.generateQRcodeString(total)  # 可以在集成的时候把它单独拿出来 先生成QRcode再支付 或者刷新按钮
        if QRcode is not None:
            flag = self.__customer.topUpBalance()
            return flag
        else:
            return False

    # 更改Customer邮箱
    def updateCustomerEmail(self, newEmail: str):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if bool(re.match(pattern, newEmail)):
            flag = self.__customer.updateEmail(newEmail)
            return flag
        else:
            return False  # 修改邮箱 不是一个邮箱

    # 更改Customer名字
    def updateCustomerName(self, newName: str):
        flag = self.__customer.updateName(newName)
        return flag

    # 更改Customer密码
    def updateCustomerPassword(self, newPassword: str):
        flag = self.__customer.updatePassword(newPassword)
        return flag

    def getUnfilledOrder(self):
        res = self.__customer.unpaidDetails()
        return res

    """
    Operator接口方法   
    """

    # 添加车辆 数据类型 par = ['E-bike',1,'normal']
    def addVehicleOP(self, par: list):
        self.__bike = Vehicle(None, None)
        flag = self.__operator.addVehicle(self.__bike, par, self.__operator)
        return flag

    # 删除车辆 数据类型 bikeID
    def deleteVehicleOP(self, bikeID: int):
        self.__bike = Vehicle(None, bikeID)
        flag = self.__operator.deleteVehicle(self.__bike, self.__operator)
        return flag

    # 车辆充电
    def changeBatteryOP(self, bikeID: int):
        self.__bike = Vehicle(None, bikeID)
        flag = self.__operator.changeBattery(self.__bike, self.__operator)
        return flag

    # 更改车辆位置
    def changeLocationOP(self, bikeID: int, newLocation: int):
        self.__bike = Vehicle(None, bikeID)
        flag = self.__operator.changeLocation(self.__bike, newLocation, self.__operator)
        return flag

    # 追踪车辆
    def track(self, bikeID: int):
        self.__bike = Vehicle(None, bikeID)
        location = self.__operator.getLocation(self.__bike)
        return location

    # 开始维修车辆
    def fixBikeOP(self, bikeID: int):
        self.__bike = Vehicle(None, bikeID)
        flag = self.__operator.fixBike(self.__bike, self.__operator)
        return flag

    # 结束维修车辆
    def endFixBikeOP(self, bikeID: int, reportID: int):
        self.__bike = Vehicle(None, bikeID)
        flag = self.__operator.endFixBike(self.__bike, reportID, self.__operator)
        return flag

    # 增加车站
    def addVehicleStopOP(self, par: list):
        self.__stop = vehicleStop()
        flag = self.__operator.addVehicleStop(par, self.__stop)
        return flag

    # 删除车站
    def deleteVehicleStopOP(self, stopID: int):
        self.__stop = vehicleStop(stopID)
        flag = self.__operator.deleteVehicleStop(self.__stop)
        return flag

    # 更新车站方法
    def updateVehicleStopAxisOP(self, stopID: int, newAxis: str):
        self.__stop = vehicleStop(stopID)
        flag = self.__operator.updateVehicleStopAxis(newAxis, self.__stop)
        return flag

    def updateVehicleStopNameOP(self, stopID: int, newName: str):
        self.__stop = vehicleStop(stopID)
        flag = self.__operator.updateVehicleStopName(newName, self.__stop)
        return flag

    def updateVehicleStopMaxCapacityOP(self, stopID: int, newMaxCapacity: int):
        self.__stop = vehicleStop(stopID)
        flag = self.__operator.updateVehicleStopMaxCapacity(newMaxCapacity, self.__stop)
        return flag

    # 更新 Operator 姓名 邮箱 密码
    def updateNameOP(self, newName: str):
        flag = self.__operator.updateName(newName)
        return flag

    def updateEmailOP(self, newEmail: str):
        flag = self.__operator.updateEmail(newEmail)
        return flag

    def updatePasswordOP(self, newPassword: str):
        flag = self.__operator.updatePassword(newPassword)
        return flag

    """
       Manager接口方法   
    """
    # generate pdf

    def managerViewPdf(self):
        # export csv
        # table_name = '`Order`'
        # output_csv_file = 'visualizationOrder.csv'
        # self.__manager.exportToCSV(table_name, output_csv_file)
        #
        # # generate pdf
        # data = self.__manager.load_data('visualizationOrder.csv')
        # self.__manager.visualizePlotting(data)
        # filename = "multi_plot_image.pdf"
        # # manager.saveToPdf(filename)
        # self.__manager.openPdfInBrowser(filename)

        data = self.__manager.load_data('visualizationOrder.csv')
        self.__manager.visualizePlotting(data)
        self.__manager.predictionPlotting(data)
        self.__manager.openPdfInBrowser('DataVisualization.pdf')
        self.__manager.openPdfInBrowser('DataPrediction.pdf')

    def updateNameOM(self, newName:str):
        flag = self.__manager.updateName(newName)
        return flag

    def updatePasswordOM(self, newPassword:str):
        flag = self.__manager.updatePassword(newPassword)
        return flag

    def updateEmailOM(self, newEmail:str):
        flag = self.manager.updateEmail(newEmail)
        return flag

    """
    格式化输出：Customer 1、全部车站  2.全部可用车辆 3.全部关于自己的订单 4.自己所提交的所有报告
              Operator 1、全部车站 2、全部车辆 3、全部报告 
              Manager 1、全部用户表 2、全部操作员表 3、全部订单  4、全部维修记录
    """
    """ Customer 1、全部车站  2.全部可用车辆 3.全部关于自己的订单 4.自己所提交的所有报告 """

    # 格式化输出 全部车站
    def getAllStopsCU(self):
        self.__stop = vehicleStop()
        res = self.tableFormat(self.__stop.detailsFormat(self.__stop.stopDetails()))
        tableHead = "{:<5} {:<50} {:<25} {:<25}".format("ID", "NAME", "MAX_CAPACITY", "CURRENT_CAPACITY")
        res.insert(0, tableHead)
        return res

    # 格式化输出 全部可用车辆（选定车站）
    def getAvailableVehicle(self):
        self.__stop = vehicleStop(self.__stopID)
        res = self.tableFormatVehicle(self.__stop.vehicleToList())
        tableHead = "{:<5} {:<20} {:<20} {:<25}".format("ID", "TYPE", "BATTERYSTATUS", "STATUS")
        res.insert(0, tableHead)
        return res

    def tableFormatVehicle(self, details: list):
        res = []
        for i in details:
            finalString = "{:<5} {:<20} {:<20} {:<25}".format(*i)
            res.append(finalString)
        return res

    def tableFormat(self, details: list):
        res = []
        for i in details:
            finalString = "{:<5} {:<50} {:<25} {:<25}".format(*i)
            res.append(finalString)
        return res

    # 全部关于自己的订单
    def getOrderList(self):
        print(self.__customer.orderDetails())
        res = self.tableFormatOrder(self.__customer.orderDetails())
        tableHead = "{:<4} {:<4} {:<3} {:<3} {:<20} {:<20} {:<20} {:<24} {:<5} {:<6} {:<6}".format(
            "ID", "BIKE", "S-S", "E-S", "START_TIME", "END_TIME", "CREATE_TIME", "FINISH_TIME", "COST", "ISPAID",
            "STATUS")
        res.insert(0, tableHead)
        return res

    def tableFormatOrder(self, details: list):
        res = []
        for i in details:
            finalString = "{:<4} {:<4} {:<3} {:<3} {:<20} {:<20} {:<20} {:<24} {:<5} {:<6} {:<6}".format(*i)
            res.append(finalString)
        return res

    # 自己所提交的所有报告
    def tableFormatReport(self, details: list):
        res = []
        for i in details:
            finalString = "{:<4} {:<40} {:<20} {:<20} {:<6}".format(*i)
            res.append(finalString)
        return res

    def getReportList(self):
        res = self.tableFormatReport(self.__customer.reportDetails())
        tableHead = "{:<4} {:<40} {:<20} {:<20} {:<6}".format(
            "ID", "MESSAGE", "START_TIME", "END_TIME", "STATUS")
        res.insert(0, tableHead)
        return res

    """ Operator 1、全部车站 2、全部车辆 3、全部报告 """
    # 全部车站
    def getAllStopsOP(self):
        self.__stop = vehicleStop()
        res = self.tableFormatOP(self.__stop.detailsFormat(self.__stop.stopDetailsOP()))
        tableHead = "{:<5} {:<40} {:<40} {:<20} {:<20}".format("ID", "NAME", "AXIS", "MAX_CAPACITY", "CURRENT_CAPACITY")
        res.insert(0, tableHead)
        return res

    def tableFormatOP(self, details: list):
        res = []
        for i in details:
            finalString = "{:<5} {:<40} {:<40} {:<20} {:<20}".format(*i)
            res.append(finalString)
        return res

    # 全部车辆
    def getAllVehicleOP(self):
        self.__stop = vehicleStop()
        res = self.tableFormatAllVehicle(self.__stop.vehicleAllList())
        tableHead = "{:<5} {:<10} {:<10} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10}".format(
            "ID", "TYPES", "PRICE", "BATTERYSTATUS", "LOCATIONS", "STATUS", "ISRENTED","ISLOCKED", "RENTER")
        res.insert(0, tableHead)
        return res

    def tableFormatAllVehicle(self, details: list):
        res = []
        for i in details:
            finalString = "{:<5} {:<10} {:<10} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10} ".format(*i)
            res.append(finalString)
        return res

    # 全部报告
    def tableFormatReportOP(self, details: list):
        res = []
        for i in details:
            finalString = "{:<5} {:<10} {:<40} {:<25} {:<25} {:<10} {:<10}".format(*i)
            res.append(finalString)
        return res

    def getALLReportOP(self):
        res = self.tableFormatReportOP(self.__operator.reportAllDetails())
        tableHead = "{:<5} {:<10} {:<40} {:<25} {:<25} {:<10} {:<10}".format(
            "ID","FROM_ID","MESSAGE", "START_TIME", "END_TIME", "STATUS", "AUTHEN")
        res.insert(0, tableHead)
        return res

    """ Manager 1、全部用户表 2、全部操作员表 3、全部订单 4、全部维修记录 """

    # 全部用户表
    def tableFormatCustomerOM(self, details: list):
        res = []
        for i in details:
            # 不要密码
            finalString = "{:<5} {:<20} {:<25} {:<25}".format(*i)
            res.append(finalString)
        return res

    def getALLCustomerOM(self):
        res = self.tableFormatCustomerOM(self.__manager.getAllCustomer())
        tableHead = "{:<5} {:<20} {:<25} {:<25}".format(
            "ID","NAME","EMAIL", "ACCOUNT_BALANCE")
        res.insert(0, tableHead)
        return res

    # 全部操作者
    def tableFormatOperatorOM(self, details: list):
        res = []
        for i in details:
            # 不要密码
            finalString = "{:<5} {:<15} {:<25}".format(*i)
            res.append(finalString)
        return res

    def getALLOperatorOM(self):
        res = self.tableFormatOperatorOM(self.__manager.getAllOperator())
        tableHead = "{:<5} {:<15} {:<25} ".format(
            "ID","NAME","EMAIL")
        res.insert(0, tableHead)
        return res

    # 全部订单
    def getOrderListOM(self):
        res = self.tableFormatOrderOM(self.__manager.getAllOrder())
        tableHead = "{:<4} {:<5} {:<6} {:<3} {:<3} {:<20} {:<20} {:<20} {:<24} {:<6} {:<6} {:<6}".format(
            "ID", "BIKE", "RENTER", "S-S", "E-S", "START_TIME", "END_TIME", "CREATE_TIME", "FINISH_TIME", "COST", "ISPAID",
            "STATUS")
        res.insert(0, tableHead)
        return res

    def tableFormatOrderOM(self, details: list):
        res = []
        for i in details:
            finalString = "{:<4} {:<5} {:<6} {:<3} {:<3} {:<20} {:<20} {:<20} {:<24} {:<6} {:<6} {:<6}".format(*i)
            res.append(finalString)
        return res

    # 全部维修记录
    def tableFormatRecordsOM(self, details: list):
        res = []
        for i in details:
            finalString = "{:<5} {:<25} {:<25} {:<10} {:<25}".format(*i)
            res.append(finalString)
        return res

    def getALLRecordOM(self):
        res = self.tableFormatRecordsOM(self.__manager.getAllRecord())
        tableHead = "{:<5} {:<25} {:<25} {:<10} {:<25}".format(
            "ID","OPERATOR_EMAIL","DATA","BIKE_ID","STATUS")
        res.insert(0, tableHead)
        return res

    # 全部报告
    def tableFormatReportOM(self, details: list):
        res = []
        for i in details:
            finalString = "{:<5} {:<10} {:<40} {:<25} {:<25} {:<10} {:<10}".format(*i)
            res.append(finalString)
        return res

    def getALLReportOM(self):
        res = self.tableFormatReportOM(self.__manager.reportAllDetailsOM())
        tableHead = "{:<5} {:<10} {:<40} {:<25} {:<25} {:<10} {:<10}".format(
            "ID","FROM_ID","MESSAGE", "START_TIME", "END_TIME", "STATUS", "AUTHEN")
        res.insert(0, tableHead)
        return res

    # 全部车站
    def getAllStopsOM(self):
        self.__stop = vehicleStop()
        res = self.tableFormatOP(self.__stop.detailsFormat(self.__stop.stopDetailsOP()))
        tableHead = "{:<5} {:<40} {:<40} {:<20} {:<20}".format("ID", "NAME", "AXIS", "MAX_CAPACITY", "CURRENT_CAPACITY")
        res.insert(0, tableHead)
        return res

    # 全部车
    def getAllVehicleOM(self):
        self.__stop = vehicleStop()
        res = self.tableFormatAllVehicle(self.__stop.vehicleAllList())
        tableHead = "{:<5} {:<10} {:<10} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10}".format(
            "ID", "TYPES", "PRICE", "BATTERYSTATUS", "LOCATIONS", "STATUS", "ISRENTED","ISLOCKED", "RENTER")
        res.insert(0, tableHead)
        return res



if __name__ == '__main__':
    import time
    # app = app()
    #
    # par1 = ["manager123@gmail.com", "manager123", "3"]
    # app.login(par1)
    # app.managerViewPdf()
    # 用户测试
    # app = app()
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

    # generate pdf
    # data = manager.load_data('visualizationOrder.csv')
    # manager.visualizePlotting(data)
    # manager.predictionPlotting(data)
    # manager.openPdfInBrowser('DataVisualization.pdf')
    # manager.openPdfInBrowser('DataPrediction.pdf')

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
    # 测试Operator 增加车辆
    app = app()
    # par = ["zhangruixian@gmail.com", "3022008", '2']
    # app.login(par)
    # for i in range(20):
    #     Rand = random.randint(1,8)
    #     app.addVehicleOP(['bike',Rand,'normal'])

    """
    app running
    Login successfully
    Add a new vehicle successfully:  4 Bike
    Records: 13
    Add a new log successfully 13 zhangruixian@gmail.com 2023-10-28 08:51:19 4 Add a new bike
    """
    # 测试Operator 删除车辆
    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008", '2']
    # app.login(par)
    # app.deleteVehicleOP(4)

    """
    app running
    Login successfully
    Delete the vehicle successfully:  4
    Records: 14
    Add a new log successfully 14 zhangruixian@gmail.com 2023-10-28 09:07:07 4 Delete bike id is: 4
    """

    # 测试Operator 测试充电
    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008", '2']
    # app.login(par)
    # app.changeBatteryOP(2)

    """
    app running
    Login successfully
    Successfully change battery of bike
    Records: 15
    Add a new log successfully 15 zhangruixian@gmail.com 2023-10-28 11:27:53 2 change new battery
    """

    # 测试Operator 更改单车车站
    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008", '2']
    # app.login(par)
    # app.changeLocationOP(3,1)

    """
    app running
    Login successfully
    Successfully change location of bike
    Records: 16
    Add a new log successfully 16 zhangruixian@gmail.com 2023-10-28 11:34:23 3 Change location: 2 to 1
    """

    # 测试Operator 维修 维修结束
    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008a", '1']
    # app.login(par)
    # app.reportCustomer(2)

    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008", '2']
    # app.login(par)
    # #app.fixBikeOP(2)
    # app.endFixBikeOP(2,13)

    """
    app running
    Login 'zhangruixian@gmail.com' successfully
    Add a new report successfully 13 The Bike needs to fix, id is : 2
    Successfully report
    
    app running
    Login successfully
    Fixing ...
    Records: 17
    Add a new log successfully 17 zhangruixian@gmail.com 2023-10-28 11:57:36 2 Fixing bike: 2
    
    app running
    Login successfully
    Successfully, processed the report id:  13
    Report id: 13 is done
    Records: 18
    Add a new log successfully 18 zhangruixian@gmail.com 2023-10-28 11:58:22 2 Fixing bike is done: 2
    """

    # 测试Operator 新建车站 删除车站 更新车站
    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008", '2']
    # app.login(par)
    # parStop = ['Test3', '(55.869，-3.31)', 20]
    # app.addVehicleStopOP(parStop)
    # time.sleep(5)
    # app.updateVehicleStopAxisOP(3,"(55.869，-7.31)")
    # time.sleep(5)
    # app.updateVehicleStopNameOP(3,"Testing")
    # time.sleep(5)
    # app.updateVehicleStopMaxCapacityOP(3,25)
    # app.deleteVehicleStopOP(3)

    """
    app running
    Login successfully
    Add a new vehicle stop successfully 3 Test3 (55.869，-8.31) 20
    Change successfully
    Change successfully
    Change successfully
    Delete customer successfully 3
    """

    # 格式化输出测试 Customer
    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008a", '1']
    # app.login(par)
    # for i in app.getAllStopsCU():
    #     print(i)
    #
    # print(" ")
    #
    # for i in app.getAvailableVehicle(1):
    #     print(i)
    #
    # print(" ")
    #
    # for i in app.getOrderList():
    #     print(i)
    #
    # print(" ")
    #
    # for i in app.getReportList():
    #     print(i)
    """
    app running
    Login 'zhangruixian@gmail.com' successfully
    ID    NAME                 MAX_CAPACITY              CURRENT_CAPACITY         
    1     TestNameIng          30                        2                        
    2     Test                 30                        1                        
    3     Test3                20                        1                        
     
    ID    TYPE                 BATTERYSTATUS             STATUS                   
    2     E-bike               100.0                     normal                   
    3     E-bike               99.3                      normal                   
     
    ID   BIKE S-S E-S START_TIME           END_TIME             CREATE_TIME          FINISH_TIME              COST  ISPAID STATUS
    5    1    5   3   2023-10-17 15:50:49  2023-10-17 15:50:59  2023-10-22 15:50:49  2023-10-22 15:51:00      0.2   True   True  
    6    2    1   5   2023-10-17 15:51:20  2023-10-17 15:51:30  2023-10-22 15:51:20  2023-10-22 15:51:31      0.2   True   True  
    7    2    2   4   2023-10-17 16:18:32  2023-10-17 16:18:42  2023-10-22 16:18:32  2023-10-22 16:18:42      0.2   True   True  
    8    2    3   3   2023-10-18 16:19:01  2023-10-18 16:19:10  2023-10-22 16:19:01  2023-10-22 16:19:10      0.18  True   True  
    15   1    5   3   2023-10-19 15:50:49  2023-10-19 15:50:59  2023-10-22 15:50:49  2023-10-22 15:51:00      0.2   True   True  
    16   2    1   3   2023-10-19 15:51:20  2023-10-19 15:51:30  2023-10-22 15:51:20  2023-10-22 15:51:31      0.2   True   True  
    17   2    2   3   2023-10-19 16:18:32  2023-10-19 16:18:42  2023-10-22 16:18:32  2023-10-22 16:18:42      0.2   True   True  
    18   2    3   3   2023-10-20 16:19:01  2023-10-20 16:19:10  2023-10-22 16:19:01  2023-10-22 16:19:10      0.18  True   True  
    25   1    5   2   2023-10-21 15:50:49  2023-10-21 15:50:59  2023-10-22 15:50:49  2023-10-22 15:51:00      0.2   True   True  
    26   2    1   1   2023-10-22 15:51:20  2023-10-22 15:51:30  2023-10-22 15:51:20  2023-10-22 15:51:31      0.2   True   True  
    27   2    2   1   2023-10-22 16:18:32  2023-10-22 16:18:42  2023-10-22 16:18:32  2023-10-22 16:18:42      0.2   True   True  
    28   2    3   1   2023-10-22 16:19:01  2023-10-22 16:19:10  2023-10-22 16:19:01  2023-10-22 16:19:10      0.18  True   True  
    31   3    2   2   2023-10-24 16:47:48  2023-10-24 16:47:53  2023-10-24 16:47:48  2023-10-24 16:47:53      0.1   True   True  
    32   3    2   2   2023-10-24 16:53:11  2023-10-24 16:53:21  2023-10-24 16:53:11  2023-10-24 16:53:21      0.2   True   True  
    33   3    2   2   2023-10-24 19:16:57  2023-10-24 19:17:07  2023-10-24 19:16:57  2023-10-24 19:30:39      0.2   True   True  
    34   2    1   1   2023-10-24 19:30:40  2023-10-24 19:30:40  2023-10-24 19:30:40  2023-10-24 19:30:40      0.0   True   True  
    35   1    2   2   2023-10-24 19:37:42  2023-10-24 19:37:42  2023-10-24 19:37:42  2023-10-24 19:38:17      0.0   True   True  
    36   2    1   1   2023-10-24 19:38:17  2023-10-24 19:38:18  2023-10-24 19:38:17  2023-10-24 19:38:18      0.02  True   True  
    37   3    2   2   2023-10-24 20:52:14  2023-10-24 20:52:24  2023-10-24 20:52:14  2023-10-24 20:52:25      0.2   True   True  
     
    ID   MESSAGE                                  START_TIME           END_TIME             STATUS
    1    The 1 bike is broken                     2023-10-18 14:50:45  2023-10-19 07:51:42  1     
    2    The id of bike 2 is broken               2023-10-19 07:42:45  2023-10-19 07:52:18  1     
    3    The id of bike 2 is broken               2023-10-19 07:46:56  2023-10-19 07:52:21  1     
    4    Update                                   2023-10-19 08:06:23  2023-10-19 07:57:54  1     
    5    The Bike needs to fix, id is : 1         2023-10-22 10:38:19  2023-10-22 11:02:49  1     
    6    The Bike needs to fix, id is : 1         2023-10-22 11:06:01  2023-10-22 11:06:01  1     
    13   The Bike needs to fix, id is : 2         2023-10-28 11:55:28  2023-10-28 11:58:21  1   
    
    """

    # 格式化输出测试 Operator
    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008", '2']
    # app.login(par)
    # for i in app.getAllStopsOP():
    #     print(i)
    #
    # print(" ")
    #
    # for i in app.getAllVehicleOP():
    #     print(i)
    #
    # print(" ")
    #
    # for i in app.getALLReportOP():
    #     print(i)

    """
    app running
    Login successfully
    ID    NAME                 AXIS                      MAX_CAPACITY              CURRENT_CAPACITY         
    1     TestNameIng          (55.869，-5.301)           30                        2                        
    2     Test                 (55.869，-6.21)            30                        1                        
    3     Test3                (55.869，-7.31)            20                        1                        

    ID    TYPES      PRICE      BATTERYSTATUS   LOCATIONS       STATUS     ISRENTED   ISLOCKED   RENTER    
    1     E-bike     0.02       100.0           2               normal     0          0          None       
    2     E-bike     0.02       100.0           1               normal     0          0          None       
    3     E-bike     0.02       99.3            1               normal     0          0          None       
    4     Bike       0.005      0.0             3               normal     0          0          None       

    ID    FROM_ID    MESSAGE                                  START_TIME                END_TIME                  STATUS     AUTHEN    
    1     1          The 1 bike is broken                     2023-10-18 14:50:45       2023-10-19 07:51:42       1          0         
    2     1          The id of bike 2 is broken               2023-10-19 07:42:45       2023-10-19 07:52:18       1          0         
    3     1          The id of bike 2 is broken               2023-10-19 07:46:56       2023-10-19 07:52:21       1          0         
    4     1          Update                                   2023-10-19 08:06:23       2023-10-19 07:57:54       1          0         
    5     1          The Bike needs to fix, id is : 1         2023-10-22 10:38:19       2023-10-22 11:02:49       1          0         
    6     1          The Bike needs to fix, id is : 1         2023-10-22 11:06:01       2023-10-22 11:06:01       1          0         
    7     2          The Bike needs to fix, id is : 2         2023-10-22 22:46:21       2023-10-22 22:46:21       1          0         
    8     2          The Bike needs to fix, id is : 1         2023-10-22 22:47:30       2023-10-22 22:48:10       1          0         
    9     2          The Bike needs to fix, id is : 2         2023-10-22 22:50:35       2023-10-22 22:50:55       1          0         
    10    2          The Bike needs to fix, id is : 1         2023-10-22 22:52:52       2023-10-22 22:53:12       1          0         
    11    2          The Bike needs to fix, id is : 3         2023-10-22 22:55:48       2023-10-22 22:55:58       1          0         
    12    2          The Bike needs to fix, id is : 1         2023-10-22 22:56:40       2023-10-22 22:56:50       1          0         
    13    1          The Bike needs to fix, id is : 2         2023-10-28 11:55:28       2023-10-28 11:58:21       1          0        
    """

    # 格式化输出测试 Manager
    # app = app()
    # par = ["zhangruixian@gmail.com", "3022008", '2']
    # app.login(par)
    # for i in app.getALLCustomerOM():
    #     print(i)
    #
    # print(" ")
    #
    # for i in app.getALLOperatorOM():
    #     print(i)
    #
    # print(" ")
    #
    # for i in app.getOrderListOM():
    #     print(i)
    #
    # print(" ")
    #
    # for i in app.getALLRecordOM():
    #     print(i)
    #
    # print(" ")
    #
    # for i in app.getALLReportOM():
    #     print(i)
    """
    app running
    Login successfully
    ID    NAME                 EMAIL                     ACCOUNT_BALANCE          
    5     Yuqing Ren           renyuqing@gmail.com       5.5                      
    1     Zhang,Ruixian        zhangruixian@gmail.com    590.14                   
    2     Yujia Ye             zhangyujia@gmail.com      152.19                   
    3     Junan Zheng          zhengjunan@yahool.com     4.39                     
    4     Junan Zheng          zhengjunnan99@gmail.com   5.5                      
     
    ID    NAME            EMAIL                     
    1     ZZZ             zhangruixian@gmail.com   
    2     Yuqing Ren      renyuqing@gmail.com      
     
    ID   BIKE  RENTER S-S E-S START_TIME           END_TIME             CREATE_TIME          FINISH_TIME              COST   ISPAID STATUS
    1    2     2      1   3   2023-10-16 15:47:04  2023-10-16 15:47:09  2023-10-22 15:47:04  2023-10-22 15:47:09      0.1    True   True  
    2    2     2      2   3   2023-10-16 15:48:01  2023-10-16 15:48:06  2023-10-22 15:48:01  2023-10-22 15:48:06      0.1    True   True  
    3    2     3      3   3   2023-10-17 15:49:14  2023-10-17 15:49:19  2023-10-22 15:49:14  2023-10-22 15:49:20      0.1    True   True  
    4    2     3      4   3   2023-10-17 15:49:57  2023-10-17 15:50:07  2023-10-22 15:49:57  2023-10-22 15:50:08      0.2    True   True  
    5    1     1      5   3   2023-10-17 15:50:49  2023-10-17 15:50:59  2023-10-22 15:50:49  2023-10-22 15:51:00      0.2    True   True  
    6    2     1      1   5   2023-10-17 15:51:20  2023-10-17 15:51:30  2023-10-22 15:51:20  2023-10-22 15:51:31      0.2    True   True  
    7    2     1      2   4   2023-10-17 16:18:32  2023-10-17 16:18:42  2023-10-22 16:18:32  2023-10-22 16:18:42      0.2    True   True  
    8    2     1      3   3   2023-10-18 16:19:01  2023-10-18 16:19:10  2023-10-22 16:19:01  2023-10-22 16:19:10      0.18   True   True  
    9    2     3      4   2   2023-10-18 16:19:34  2023-10-18 16:19:42  2023-10-22 16:19:34  2023-10-22 16:19:42      0.16   True   True  
    10   2     2      5   3   2023-10-18 15:47:04  2023-10-18 15:47:09  2023-10-22 15:47:04  2023-10-22 15:47:09      0.1    True   True  
    11   2     2      1   4   2023-10-18 15:47:04  2023-10-18 15:47:09  2023-10-22 15:47:04  2023-10-22 15:47:09      0.1    True   True  
    12   2     2      2   2   2023-10-18 15:48:01  2023-10-18 15:48:06  2023-10-22 15:48:01  2023-10-22 15:48:06      0.1    True   True  
    13   2     3      3   4   2023-10-18 15:49:14  2023-10-18 15:49:19  2023-10-22 15:49:14  2023-10-22 15:49:20      0.1    True   True  
    14   2     3      4   5   2023-10-19 15:49:57  2023-10-19 15:50:07  2023-10-22 15:49:57  2023-10-22 15:50:08      0.2    True   True  
    15   1     1      5   3   2023-10-19 15:50:49  2023-10-19 15:50:59  2023-10-22 15:50:49  2023-10-22 15:51:00      0.2    True   True  
    16   2     1      1   3   2023-10-19 15:51:20  2023-10-19 15:51:30  2023-10-22 15:51:20  2023-10-22 15:51:31      0.2    True   True  
    17   2     1      2   3   2023-10-19 16:18:32  2023-10-19 16:18:42  2023-10-22 16:18:32  2023-10-22 16:18:42      0.2    True   True  
    18   2     1      3   3   2023-10-20 16:19:01  2023-10-20 16:19:10  2023-10-22 16:19:01  2023-10-22 16:19:10      0.18   True   True  
    19   2     3      4   2   2023-10-20 16:19:34  2023-10-20 16:19:42  2023-10-22 16:19:34  2023-10-22 16:19:42      0.16   True   True  
    20   2     2      5   1   2023-10-20 15:47:04  2023-10-20 15:47:09  2023-10-22 15:47:04  2023-10-22 15:47:09      0.1    True   True  
    21   2     2      1   3   2023-10-21 15:47:04  2023-10-21 15:47:09  2023-10-22 15:47:04  2023-10-22 15:47:09      0.1    True   True  
    22   2     2      2   4   2023-10-21 15:48:01  2023-10-21 15:48:06  2023-10-22 15:48:01  2023-10-22 15:48:06      0.1    True   True  
    23   2     3      3   5   2023-10-21 15:49:14  2023-10-21 15:49:19  2023-10-22 15:49:14  2023-10-22 15:49:20      0.1    True   True  
    24   2     3      4   3   2023-10-21 15:49:57  2023-10-21 15:50:07  2023-10-22 15:49:57  2023-10-22 15:50:08      0.2    True   True  
    25   1     1      5   2   2023-10-21 15:50:49  2023-10-21 15:50:59  2023-10-22 15:50:49  2023-10-22 15:51:00      0.2    True   True  
    26   2     1      1   1   2023-10-22 15:51:20  2023-10-22 15:51:30  2023-10-22 15:51:20  2023-10-22 15:51:31      0.2    True   True  
    27   2     1      2   1   2023-10-22 16:18:32  2023-10-22 16:18:42  2023-10-22 16:18:32  2023-10-22 16:18:42      0.2    True   True  
    28   2     1      3   1   2023-10-22 16:19:01  2023-10-22 16:19:10  2023-10-22 16:19:01  2023-10-22 16:19:10      0.18   True   True  
    29   2     3      4   5   2023-10-22 16:19:34  2023-10-22 16:19:42  2023-10-22 16:19:34  2023-10-22 16:19:42      0.16   True   True  
    30   2     2      5   3   2023-10-22 15:47:04  2023-10-22 15:47:09  2023-10-22 15:47:04  2023-10-22 15:47:09      0.1    True   True  
    31   3     1      2   2   2023-10-24 16:47:48  2023-10-24 16:47:53  2023-10-24 16:47:48  2023-10-24 16:47:53      0.1    True   True  
    32   3     1      2   2   2023-10-24 16:53:11  2023-10-24 16:53:21  2023-10-24 16:53:11  2023-10-24 16:53:21      0.2    True   True  
    33   3     1      2   2   2023-10-24 19:16:57  2023-10-24 19:17:07  2023-10-24 19:16:57  2023-10-24 19:30:39      0.2    True   True  
    34   2     1      1   1   2023-10-24 19:30:40  2023-10-24 19:30:40  2023-10-24 19:30:40  2023-10-24 19:30:40      0.0    True   True  
    35   1     1      2   2   2023-10-24 19:37:42  2023-10-24 19:37:42  2023-10-24 19:37:42  2023-10-24 19:38:17      0.0    True   True  
    36   2     1      1   1   2023-10-24 19:38:17  2023-10-24 19:38:18  2023-10-24 19:38:17  2023-10-24 19:38:18      0.02   True   True  
    37   3     1      2   2   2023-10-24 20:52:14  2023-10-24 20:52:24  2023-10-24 20:52:14  2023-10-24 20:52:25      0.2    True   True  
     
    ID    OPERATOR_EMAIL            DATA                      BIKE_ID    STATUS                   
    1     zhangruixian@gmail.com    2023-10-22 21:42:24       1          change new battery       
    2     zhangruixian@gmail.com    2023-10-22 22:10:19       4          Add a new bike           
    3     zhangruixian@gmail.com    2023-10-22 22:12:35       4          Delete the bike          
    4     zhangruixian@gmail.com    2023-10-22 22:21:26       3          Change location: 2 to 1  
    5     zhangruixian@gmail.com    2023-10-22 22:24:21       3          Fixing bike: 3           
    6     zhangruixian@gmail.com    2023-10-22 22:46:22       2          Fixing bike is done: 2   
    7     zhangruixian@gmail.com    2023-10-22 22:47:50       1          Fixing bike: 1           
    8     zhangruixian@gmail.com    2023-10-22 22:50:45       2          Fixing bike: 2           
    9     zhangruixian@gmail.com    2023-10-22 22:53:02       1          Fixing bike: 1           
    10    zhangruixian@gmail.com    2023-10-22 22:55:53       3          Fixing bike: 3           
    11    zhangruixian@gmail.com    2023-10-22 22:56:45       1          Fixing bike: 1           
    12    zhangruixian@gmail.com    2023-10-22 22:56:50       1          Fixing bike is done: 1   
    13    zhangruixian@gmail.com    2023-10-28 08:51:19       4          Add a new bike           
    14    zhangruixian@gmail.com    2023-10-28 09:07:07       4          Delete bike id is: 4     
    15    zhangruixian@gmail.com    2023-10-28 11:27:53       2          change new battery       
    16    zhangruixian@gmail.com    2023-10-28 11:34:23       3          Change location: 2 to 1  
    17    zhangruixian@gmail.com    2023-10-28 11:57:36       2          Fixing bike: 2           
    18    zhangruixian@gmail.com    2023-10-28 11:58:22       2          Fixing bike is done: 2   
    19    zhangruixian@gmail.com    2023-10-28 14:02:21       4          Add a new bike           
     
    ID    FROM_ID    MESSAGE                                  START_TIME                END_TIME                  STATUS     AUTHEN    
    1     1          The 1 bike is broken                     2023-10-18 14:50:45       2023-10-19 07:51:42       1          0         
    2     1          The id of bike 2 is broken               2023-10-19 07:42:45       2023-10-19 07:52:18       1          0         
    3     1          The id of bike 2 is broken               2023-10-19 07:46:56       2023-10-19 07:52:21       1          0         
    4     1          Update                                   2023-10-19 08:06:23       2023-10-19 07:57:54       1          0         
    5     1          The Bike needs to fix, id is : 1         2023-10-22 10:38:19       2023-10-22 11:02:49       1          0         
    6     1          The Bike needs to fix, id is : 1         2023-10-22 11:06:01       2023-10-22 11:06:01       1          0         
    7     2          The Bike needs to fix, id is : 2         2023-10-22 22:46:21       2023-10-22 22:46:21       1          0         
    8     2          The Bike needs to fix, id is : 1         2023-10-22 22:47:30       2023-10-22 22:48:10       1          0         
    9     2          The Bike needs to fix, id is : 2         2023-10-22 22:50:35       2023-10-22 22:50:55       1          0         
    10    2          The Bike needs to fix, id is : 1         2023-10-22 22:52:52       2023-10-22 22:53:12       1          0         
    11    2          The Bike needs to fix, id is : 3         2023-10-22 22:55:48       2023-10-22 22:55:58       1          0         
    12    2          The Bike needs to fix, id is : 1         2023-10-22 22:56:40       2023-10-22 22:56:50       1          0         
    13    1          The Bike needs to fix, id is : 2         2023-10-28 11:55:28       2023-10-28 11:58:21       1          0    
    """