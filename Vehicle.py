import pymysql
from Customer import Customer
from vehicleStop import vehicleStop
from Report import Report

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

cursor.execute("SELECT * from `Vehicle`")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
# 拿到属于数据库的最后一个id
currentID = data[-1][0]


class VehicleCapacityError(Exception):
    pass


class Vehicle:
    def __init__(self, customer: Customer, vehicleID: int = None):
        if vehicleID is None:
            self.__vehicleID = currentID + 1
            self.__types = None
            self.__price = None
            self.__batteryStatus = None
            self.__locations = None
            self.__status = None
            self.__isRented = None
            self.__isLocked = None
            self.__renter = None

        elif customer or vehicleID is not None:
            self.__customer = customer

            self.__vehicleID = vehicleID
            oneSQL = "SELECT * FROM `Vehicle` WHERE vehicleID = %s"
            cursor.execute(oneSQL, vehicleID)
            oneData = cursor.fetchone()

            self.__types = oneData[1]
            self.__price = oneData[2]
            self.__batteryStatus = oneData[3]
            self.__locations = oneData[4]
            self.__status = oneData[5]
            self.__isRented = oneData[6]
            self.__isLocked = oneData[7]
            self.__renter = oneData[-1]

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def batteryStatus(self):
        return self.__batteryStatus

    @batteryStatus.setter
    def batteryStatus(self, value):
        self.__batteryStatus = value

    @property
    def vehicleID(self):
        return self.__vehicleID

    @vehicleID.setter
    def vehicleID(self, value):
        self.__vehicleID = value

    @property
    def isRented(self):
        return self.__isRented

    @isRented.setter
    def isRented(self, value):
        self.__isRented = value

    @property
    def locations(self):
        return self.__locations

    @locations.setter
    def locations(self, value):
        self.__locations = value

    @property
    def isLocked(self):
        return self.__isLocked

    @isLocked.setter
    def isLocked(self, value):
        self.__isLocked = value

    @property
    def renter(self):
        return self.__renter

    @renter.setter
    def renter(self, value):
        self.__renter = value

    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, value):
        self.__types = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def rent(self):
        if self.__status == 'normal':
            self.__renter = self.__customer.id
            self.__isRented = 1
            self.__isLocked = 1
            updateSQL = "update `Vehicle` set renter = %s,isRented = %s,isLocked = %s where vehicleID = %s"
            cursor.execute(updateSQL, (self.__renter, self.__isRented, self.__isLocked, self.__vehicleID))
            db.commit()
            print("Successfully rent")
            return True
        else:
            return False

    def returnBike(self, stop: vehicleStop):
        if self.__isRented == 1:
            self.__renter = None
            self.__isRented = 0
            self.__isLocked = 0
            self.__locations = stop.id
            updateSQL = "update `Vehicle` set locations = %s,renter = %s,isRented = %s,isLocked = %s where vehicleID = %s"
            cursor.execute(updateSQL,
                           (self.__locations, self.__renter, self.__isRented, self.__isLocked, self.__vehicleID))
            db.commit()
            print("Successfully return")

    # type locations status
    def add(self, par: list):
        self.__types = par[0]
        if self.__types == 'E-bike':
            self.__price = 0.02
            self.__batteryStatus = 100
        else:
            self.__price = 0.005
            self.__batteryStatus = 0

        self.__locations = par[1]
        self.__status = par[2]
        self.__isRented = 0

        if self.__status == 'normal':
            self.__isLocked = 0
        else:
            self.__isLocked = 1
        self.__renter = None

        currentCapacity = 0
        maxCapacity = 0
        searchSQL = "SELECT `maxCapacity`,`currentCapacity` FROM `VehicleStop` WHERE locationID = %s"
        cursor.execute(searchSQL, self.__locations)
        capacityList = cursor.fetchall()
        for row in capacityList:
            currentCapacity = row[1]
            maxCapacity = row[0]

        if currentCapacity <= maxCapacity:
            saveSQL = "insert ignore into Vehicle(vehicleID,types,price,batteryStatus,locations,status,isRented,isLocked,renter)" \
                      "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            addFlag = cursor.execute(saveSQL,
                                     (self.__vehicleID, self.__types, self.__price, self.__batteryStatus,
                                      self.__locations,
                                      self.__status, self.__isRented, self.__isLocked, self.__renter))
            db.commit()

            if addFlag:
                print("Add a new vehicle successfully: ", self.__vehicleID, self.__types)
                return True
            else:
                print("Unsuccessfully add")
                return False
        else:
            raise VehicleCapacityError

    def delete(self):
        deleteSQL = "delete from Vehicle where vehicleID = %s"
        flag = cursor.execute(deleteSQL, self.__vehicleID)
        db.commit()
        if flag == 0:
            return False
        else:
            print("Delete the vehicle successfully: ", self.__vehicleID)
            return True

    def reportFix(self):
        message = "The Bike needs to fix, id is : " + str(self.__vehicleID)
        reportFix = Report(self.__customer, None, message)
        reportFix.report()
        self.__status = 'reporting'
        self.__isLocked = 1
        updateSQL = "update `Vehicle` set status = %s,isLocked = %s where vehicleID = %s"
        flag = cursor.execute(updateSQL, (self.__status, self.__isLocked, self.__vehicleID))
        db.commit()
        if flag == 0:
            return False
        else:
            print("Successfully report")
            return True

    def fixing(self):
        if self.__status == 'reporting':
            self.__status = 'fixing'
            self.__isLocked = 1
            updateSQL = "update `Vehicle` set status = %s, isLocked = %s where vehicleID = %s"
            flag = cursor.execute(updateSQL, (self.__status, self.__isLocked, self.__vehicleID))
            db.commit()
            if flag == 0:
                return False
            else:
                print("Fixing ...")
                return True
        else:
            return False

    def endFix(self, reportID: int, operator):
        if self.__status == "fixing":
            self.__status = 'normal'
            self.__isLocked = 0
            report = Report(None, operator, "")
            report.done(reportID)

            updateSQL = "update `Vehicle` set status = %s, isLocked=%s where vehicleID = %s"
            flag = cursor.execute(updateSQL, (self.__status, self.__isLocked, self.__vehicleID))
            db.commit()
            if flag == 0:
                return False
            else:
                print("Report id: " + str(reportID) + " is done")
                return True
        else:
            return False

    def changeBatteryStatus(self):
        self.__batteryStatus = 100
        flag = updateSQL = "update `Vehicle` set batteryStatus=%s where vehicleID = %s"
        cursor.execute(updateSQL, (self.__batteryStatus, self.__vehicleID))
        db.commit()
        if flag == 0:
            return False
        else:
            print("Successfully change battery of bike")
            return True


    def updateLocations(self, newLocations: int):
        self.__locations = newLocations
        flag = updateSQL = "update `Vehicle` set locations=%s where vehicleID = %s"
        cursor.execute(updateSQL, (self.__locations, self.__vehicleID))
        db.commit()
        if flag == 0:
            return False
        else:
            print("Successfully change location of bike")
            return True

    def updateBatteryStatus(self):
        updateSQL = "update `Vehicle` set batteryStatus=%s where vehicleID = %s"
        cursor.execute(updateSQL, (self.__batteryStatus, self.__vehicleID))
        db.commit()

    def batteryDiscount(self, second: float):
        secondBattery = 0.01
        self.__batteryStatus -= secondBattery * second
        self.updateBatteryStatus()


if __name__ == '__main__':
    # customer = Customer("zhangruixian@gmail.com")
    # vehicle1 = Vehicle(customer,None,1)
    # vehicle1.rent()
    # stop2 = vehicleStop(2)
    # vehicle1.returnBike(stop2)
    #
    # operator1 = Operator("")
    vehicle = Vehicle(None, 2)
    # vehicle.updateLocations(2)

    # vehicle2 = Vehicle(None,operator1,None)
    # par = ['E-bike',1,'normal']
    # vehicle2.add(par)

    # vehicle2 = Vehicle(customer,None,1)
    # vehicle1.reportFix()
    #
    # vehicle2 = Vehicle(None,operator1,1)
    # vehicle2.endFix(6)
