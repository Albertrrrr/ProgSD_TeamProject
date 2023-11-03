import pymysql
import datetime
from config import mysql_config


class Records:
    def __init__(self,operator,vehicle,status: str):
        self.__db = pymysql.connect(**mysql_config)
        self.__cursor = self.__db.cursor()

        self.__cursor.execute("SELECT * from Records")
        # 使用 fetchone() 方法获取单条数据.
        data = self.__cursor.fetchall()
        # 拿到属于数据库的最后一个id

        if operator is None:
            self.__id = None
            self.__email = None
            self.__date = None
            self.__bikeID = None
            self.__status = None

        else:
            self.__cursor.execute("SELECT * from Records")
            # 使用 fetchone() 方法获取单条数据.
            data = self.__cursor.fetchall()

            try:
                currentID = data[-1][0]
            except:
                currentID = 0

            self.__id = currentID + 1
            self.__email = operator.email

            current_time = datetime.datetime.now()
            startTime = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.__date = startTime
            self.__bikeID = vehicle.vehicleID
            self.__status = status
            print("Records:", self.__id)

    def add(self):
        saveSQL = "insert ignore into Records(recordID,operator,`date`,bikeID,status)" \
                  "values(%s,%s,%s,%s,%s)"
        addFlag = self.__cursor.execute(saveSQL, (self.__id,self.__email,self.__date,self.__bikeID,self.__status ))
        self.__db.commit()
        if addFlag:
            print("Add a new log successfully", self.__id,self.__email,self.__date,self.__bikeID,self.__status)
            return True
        else:
            print("Unsuccessfully")
            return False







