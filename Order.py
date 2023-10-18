import pymysql
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

cursor.execute("SELECT * from `Order`")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
# 拿到属于数据库的最后一个id
currentID = data[-1][0]

class Order:
    # par 格式 email, vehicleID
    def __init__(self, par: list):
        email = par[0]
        oneSQL = "SELECT * FROM Customers WHERE email = %s"
        cursor.execute(oneSQL, email)
        oneData = cursor.fetchone()
        renter_id = oneData[0]

        flagSQL = 'SELECT * FROM `Order` WHERE renter = %s'
        cursor.execute(flagSQL,renter_id)
        orderList = cursor.fetchall()

        isFlag = True
        for i in orderList:
            print(i[9])
            if i[9] == '0':
                isFlag = False

        if isFlag:
            current_time = datetime.datetime.now()
            startTime = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.__id = currentID + 1
            self.__renterID = renter_id
            self.__bikeID = par[0]
            self.__startTime = startTime
            self.__endTime = ""

            current_time = datetime.datetime.now()
            creatTime = current_time.strftime("%Y-%m-%d %H:%M:%S")

            self.__createTime = creatTime
            self.__finishTime = ""
            self.__cost = 0
            self.__isPaid = 0
            self.__isFlag = isFlag
            self.__status = 0

        else:
            self.__isFlag = isFlag

    def startRent(self):
        startSQL = ""



if __name__ == '__main__':
  key = ["zhangyujia@gmail.com",'1']
  order1 = Order(key)
  print(order1)






