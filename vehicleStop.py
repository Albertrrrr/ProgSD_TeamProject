import pymysql

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

cursor.execute("SELECT * from `VehicleStop`")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
# 拿到属于数据库的最后一个id
currentID = data[-1][0]

class vehicleStop:
    def __init__(self, locationID:int = None):
        if locationID is None:
            pass
        else:
            oneSQL = "SELECT * FROM `VehicleStop` WHERE locationID = %s"
            cursor.execute(oneSQL, locationID)
            oneData = cursor.fetchone()
            self.__id = oneData[0]
            self.__name = oneData[1]
            self.__axis = oneData[2]
            self.__maxCapacity = oneData[3]
            self.__currentCapacity = oneData[4]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def currentCapacity(self):
        return self.__currentCapacity

    @currentCapacity.setter
    def currentCapacity(self, value):
        self.__currentCapacity = value

    @property
    def axis(self):
        return self.__axis

    @axis.setter
    def axis(self, value):
        self.__axis = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def maxCapacity(self):
        return self.__maxCapacity

    @maxCapacity.setter
    def maxCapacity(self, value):
        self.__maxCapacity = value

    def add(self, par: list):
        self.__id = currentID + 1
        self.__name = par[0]
        self.__axis = par[1]
        self.__maxCapacity = par[2]

        searchSQL = "SELECT COUNT(*) FROM Vehicle WHERE locations = %s AND isLocked = 0 AND isRented = 0"
        cursor.execute(searchSQL,self.__id)
        data = cursor.fetchone()
        self.__currentCapacity = data[0]

        saveSQL = "insert ignore into VehicleStop(locationID,name,axis,maxCapacity,currentCapacity)" \
                  "values(%s,%s,%s,%s,%s)"

        addFlag = cursor.execute(saveSQL, (self.__id, self.__name, self.__axis, self.__maxCapacity,self.__currentCapacity))
        db.commit()
        if addFlag:
            print("Add a new vehicle stop successfully", self.__id, self.__name, self.__axis, self.__maxCapacity,self.__currentCapacity)
            return True
        else:
            print("Change another axis")
            return False

    def delete(self):
        deleteSQL = "delete from VehicleStop where locationID = %s"
        flag = cursor.execute(deleteSQL, self.__id)
        db.commit()
        if flag == 0:
            return False
        else:
            print("Delete customer successfully", self.__id)
            return True

    def updateName(self, newName: str):
        self.__name = newName
        updateSQL = "update VehicleStop set name = %s where locationID = %s"
        flag = cursor.execute(updateSQL, (self.__name, self.__id))
        db.commit()
        if flag == 0:
            print("Change unsuccessfully")
            return False
        else:
            print("Change successfully")
            return True

    def updateMaxCapacity(self, newMaxCapacity: int):
        self.__maxCapacity = newMaxCapacity
        updateSQL = "update VehicleStop set maxCapacity = %s where locationID = %s"
        flag = cursor.execute(updateSQL, (self.__maxCapacity, self.__id))
        db.commit()
        if flag == 0:
            print("Change unsuccessfully")
            return False
        else:
            print("Change successfully")
            return True

    def updateAxis(self, newAxis:str):
        self.__axis = newAxis
        deleteSQL = "delete from `VehicleStop` where locationID = %s"
        cursor.execute(deleteSQL, self.__id)
        db.commit()
        par = [self.__name, self.__axis, self.__maxCapacity]
        flag = self.add(par)
        db.commit()

        if flag == 0:
            print("Change unsuccessfully")
            return False
        else:
            print("Change successfully")
            return True

    #更新新的Vechile数量 已经设置了Mysql触发器

    def stopDetails(self):
        cursor.execute("SELECT locationID,name,maxCapacity,currentCapacity from `VehicleStop`")
        details = cursor.fetchall()
        return details

    def stopDetailsOP(self):
        cursor.execute("SELECT * from `VehicleStop`")
        details = cursor.fetchall()
        return details

    def detailsFormat(self, details: tuple):
        detailsList = list(details)
        res = []
        for i in detailsList:
            res.append(list(i))
        return res

    #输出属于该车站的所有可用车辆
    def vehicleToList(self):
        searchSQL = "SELECT * FROM `Vehicle` WHERE locations = %s AND isLocked = 0"
        cursor.execute(searchSQL, self.__id)
        data = cursor.fetchall()
        res = []
        for i in data:
            tupleID = (i[0],i[1],i[3],i[5])
            res.append(tupleID)
        return res

    def vehicleAllList(self):
        searchSQL = "SELECT * FROM `Vehicle`"
        cursor.execute(searchSQL)

        db.commit()

        data = cursor.fetchall()
        res = self.detailsFormat(data)

        for i in res:
            for j in range(6,8):
                if i[j] == 1 or i[j] == '1':
                    i[j] = "False"
            if i[-1] is None:
                i[-1] = "None"
        return res



if __name__ == '__main__':
    #空对象 仅可返回全部的Vehicle Stops
    stop1 = vehicleStop()
    #测试添加
    # par = ['Test2','(55.869，-5.301)',20,5]
    # stop1.add(par)
    #测试对象
    stop2 = vehicleStop(1)
    stop2.vehicleToList()
    #测试删除
    #stop2.delete()

    #测试修改
    # stop2.updateName("TestNameIng")
    # stop2.updateMaxCapacity(30)

    #测试格式化输出
    # details = stop1.stopDetails()
    # res = stop1.detailsFormat(details)
    # for i in res:
    #     print(i)








