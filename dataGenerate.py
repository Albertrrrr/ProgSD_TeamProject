import datetime
import random
import pymysql

def random_time_on_date(date):
    """ 在给定日期生成随机时间 """
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    return datetime.datetime(date.year, date.month, date.day, hours, minutes, seconds)

# 基准日期（可以根据需要更改）

def generateTime(base_date):
    # 生成 startTime 和 createTime
    startTime = random_time_on_date(base_date)
    createTime = startTime  # createTime 等于 startTime

    # 生成 endTime，在 startTime 的 0 到 30 分钟内
    end_delta = datetime.timedelta(minutes=random.randint(0, 30))
    endTime = startTime + end_delta

    # 确保 endTime 不超过当天的最后一刻
    if endTime > datetime.datetime.combine(base_date, datetime.time(23, 59, 59)):
        endTime = datetime.datetime.combine(base_date, datetime.time(23, 59, 59))

    # 生成 finishTime，确保是最晚的时间
    finishTime = random_time_on_date(base_date)
    if finishTime <= endTime:
        finishTime = datetime.datetime.combine(base_date, datetime.time(23, 59, 59))

    return startTime, endTime, createTime, finishTime


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

base_date = datetime.date(2023, 11, 1)
orderID = 170
res = []
for i in range(20):
    orderID += 1
    startTime,endTime,createTime,finishTime = generateTime(base_date)
    # print(f"Start Time: {startTime}")
    # print(f"End Time: {endTime}")
    # print(f"Create Time: {createTime}")
    # print(f"Finish Time: {finishTime}")

    renter = random.randint(1,4)
    bikeId = random.randint(1,24)

    time_difference = endTime - startTime
    seconds = time_difference.total_seconds()
    cost = seconds * 0.02

    isPaid = 1
    status = 1

    startStop = random.randint(1,8)
    endStop = random.randint(1, 8)
    print(orderID,renter,bikeId,startTime,endTime,createTime,finishTime,cost,isPaid,status,startStop,endStop)

    startSQL = "insert into `Order`(orderID,renter,bike,startTime,endTime,createTime,finishTime,cost,isPaid,status,startStop,endStop) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(startSQL, (orderID,renter,bikeId,startTime,endTime,createTime,finishTime,cost,isPaid,status,startStop,endStop))
    db.commit()

    # res = [orderID,renter,bikeId,startTime,endTime,createTime,finishTime,cost,isPaid,status,startStop,endStop]







