import matplotlib.dates
import pymysql
import pandas as pd
import mysql.connector
# pip install mysql
# pip install scikit-learn
# pip install pandas
# pip install pymysql
# pip install tensorflow==2.14.0

from sqlalchemy import create_engine
# pip install sqlalchemy

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error, mean_absolute_error
from datetime import timedelta
from datetime import datetime
import webbrowser
from matplotlib.backends.backend_pdf import PdfPages
from Records import Records
from Vehicle import Vehicle, VehicleCapacityError


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
cursor.execute("SELECT * from Managers")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
# 拿到属于数据库的最后一个id
try:
    currentID = data[-1][0]
except:
    currentID = 0


class OperatorError(Exception):
    pass

class Manager:
    def __init__(self, email=None):
        if email is None:
            self.__id = None
            self.__name = None
            self.__password = None
            self.__email = None
            self.__par = []
            pass
        else:
            oneSQL = "SELECT * FROM Managers WHERE email = %s"
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

        cursor.execute("SELECT * from Managers_ver")
        data = cursor.fetchall()
        try:
            currentID = data[-1][0]
        except:
            currentID = 0

        self.__id = currentID + 1
        self.__name = self.__par[0]
        self.__password = self.__par[1]
        self.__email = self.__par[2]

        saveSQL = "insert ignore into Managers_ver(managerID,name,password,email,code_ver)" \
                  "values(%s,%s,%s,%s,(LPAD(FLOOR(RAND() * 10000), 4, '0')))"
        addFlag = cursor.execute(saveSQL, (self.__id, self.__name, self.__password, self.__email))
        db.commit()

        if addFlag:
            print("Add a new Managers_ver successfully", self.__id, self.__name, self.__password, self.__email)
            return True
        else:
            print("Change another email")
            return False

    def add(self, code: str):

        codeSQL = "SELECT * FROM `Managers_ver` WHERE managerID = %s"
        cursor.execute(codeSQL, self.__id)
        data = cursor.fetchone()
        code_ver = data[-1]

        if code == code_ver:
            saveSQL = "insert ignore into Managers(managerID,name,password,email)" \
                      "values(%s,%s,%s,%s)"
            addFlag = cursor.execute(saveSQL, (self.__id, self.__name, self.__password, self.__email))
            db.commit()
            if addFlag:
                print("Add a new Manager successfully", self.__id, self.__name, self.__password, self.__email)
                return True
            else:
                print("Change another email")
                return False

    def delete(self):
        deleteSQL = "delete from Managers where managerID = %s"
        cursor.execute(deleteSQL, self.__id)
        db.commit()
        print("Delete operator successfully", self.__id)

    # 更新名字
    def updateName(self, newName: str):
        self.__name = newName
        updateSQL = "update Managers set name = %s where managerID = %s"
        flag = cursor.execute(updateSQL, (self.__name, self.__id))
        db.commit()
        if flag == 0:
            print("Change unsuccessfully")
            return False
        else:
            print("Change successfully")
            return True


    # 更新密码
    def updatePassword(self, newPassword: str):
        self.__password = newPassword
        updateSQL = "update Managers set password = %s where managerID = %s"
        flag = cursor.execute(updateSQL, (self.__password, self.__id))
        db.commit()
        if flag == 0:
            print("Change unsuccessfully")
            return False
        else:
            print("Change successfully")
            return True

    # 更新邮件 主键
    def updateEmail(self, newEmail: str):
        self.__email = newEmail
        deleteSQL = "delete from Managers where managerID = %s"
        cursor.execute(deleteSQL, self.__id)
        db.commit()

        saveSQL = "insert ignore into Managers(managerID,name,password,email)" \
                  "values(%s,%s,%s,%s)"
        flag = cursor.execute(saveSQL, (self.__id, self.__name, self.__password, self.__email))
        db.commit()

        if flag == 0:
            print("Change unsuccessfully")
            return False
        else:
            print("Change successfully")
            return True

    def exportToCSV(self,table_name, output_csv_file):
        try:

            db_uri = "mysql+pymysql://root:3022008a@35.246.24.203:3306/progSDTeamProject"
            engine = create_engine(db_uri)

            # mysql_config = mysql.connector.connect (
            #     host = '35.246.24.203',
            #     port = '3306',
            #     user = 'root',
            #     password = "3022008a",
            #     database = "progSDTeamProject"
            # )

            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql_query(query, engine)

            # Save the data to a CSV file
            df.to_csv(output_csv_file, index=False)

        except Exception as e:
            print(f"An error occurred: {e}")

    def getAllCustomer(self):
        flagSQL = 'SELECT customerID,name,email,accountBalance FROM `Customers`'
        cursor.execute(flagSQL)
        details = cursor.fetchall()
        res = self.detailsFormatOM(details)
        return res


    # 获得全部Operator
    def getAllOperator(self):
        flagSQL = 'SELECT operatorID,name,email FROM `Operators`'
        cursor.execute(flagSQL)
        details = cursor.fetchall()
        res = self.detailsFormatOM(details)
        return res

    def detailsFormatOM(self, details: tuple):
        detailsList = list(details)
        res = []
        for i in detailsList:
            res.append(list(i))
        return res

    # 获得全部的Order
    def getAllOrder(self):
        flagSQL = 'SELECT orderID,bike,renter,startStop,endStop,startTime,endTime,createTime,finishTime,cost,isPaid,status FROM `Order`'
        cursor.execute(flagSQL)
        details = cursor.fetchall()
        res = self.detailsFormatOM(details)
        for i in res:
            for k in range(5, 9):
                i[k] = i[k].strftime("%Y-%m-%d %H:%M:%S")

            for j in range(10, 12):
                if i[j] == 1 or i[j] == '1':
                    i[j] = "True"
        return res

    # 获得全部的Records
    def getAllRecord(self):
        flagSQL = 'SELECT * FROM `Records`'
        cursor.execute(flagSQL)
        details = cursor.fetchall()
        res = self.detailsFormatOM(details)
        for i in res:
            i[2] = i[2].strftime("%Y-%m-%d %H:%M:%S")

        return res

    def reportAllDetailsOM(self):
        flagSQL = 'SELECT * FROM `Report`'
        cursor.execute(flagSQL)
        details = cursor.fetchall()
        res = self.detailsFormatReportOM(details)
        return res

    def detailsFormatReportOM(self, details: tuple):
        detailsList = list(details)
        res = []
        for i in detailsList:
            for j in range(3, 5):
                i = list(i)
                i[j] = i[j].strftime("%Y-%m-%d %H:%M:%S")
            res.append(i)
        return res


    def load_data(self, filename):
        data = pd.read_csv(filename)
        data['startTime'] = pd.to_datetime(data['startTime'])
        data['endTime'] = pd.to_datetime(data['endTime'])
        return data

    def visualizeStartStopDistribution(self, data):
        start_stop_counts = data['startStop'].value_counts()
        return start_stop_counts

    def visualizeEndStopDistribution(self, data):
        end_stop_counts = data['endStop'].value_counts()
        return end_stop_counts

    def visualizeCountRentals(self, data):
        daily_rental_counts = data.groupby(data['startTime'].dt.date)['orderID'].count()

        return daily_rental_counts

    def visualizeTimeIntervals(self, data):
        data['startTime'] = pd.to_datetime(data['startTime'], format='%d/%m/%Y %H:%M')
        data['endTime'] = pd.to_datetime(data['endTime'], format='%d/%m/%Y %H:%M')

        time_intervals = []
        start_time = datetime(2023, 10, 16, 0, 0)
        end_time = datetime(2023, 10, 22, 0, 0)
        interval = (end_time - start_time) / 8

        for i in range(8):
            time_intervals.append((start_time + i * interval, start_time + (i + 1) * interval))

        order_counts = []

        for start, end in time_intervals:
            count = ((data['startTime'] >= start) & (data['endTime'] <= end)).sum()
            order_counts.append(count)

        return order_counts

    def visualizeCapacityPrediction(self, data, stationStopNo, sequence_length=3):
        data.set_index('startTime', inplace=True)

        endStopData = data[data['endStop'] == stationStopNo]
        startStopData = data[data['startStop'] == stationStopNo]
        dailyRentals = endStopData['orderID'].resample('D').count() - startStopData['orderID'].resample(
            'D').count()
        dailyRentals[np.isnan(dailyRentals)] = 0

        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(dailyRentals.values.reshape(-1, 1))

        X, y = [], []

        for i in range(len(scaled_data) - sequence_length):
            X.append(scaled_data[i:i + sequence_length])
            y.append(scaled_data[i + sequence_length])

        X = np.array(X)
        y = np.array(y)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = Sequential()
        model.add(LSTM(units=50, activation='relu', input_shape=(sequence_length, 1)))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse')

        model.fit(X_train, y_train, epochs=68, batch_size=32)

        y_pred = model.predict(X_test)
        # rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        # mae = mean_absolute_error(y_test, y_pred)
        #
        # print(f'RMSE: {rmse}')
        # print(f'MAE: {mae}')

        last_sequence = scaled_data[-sequence_length:]
        predictions = []

        for i in range(7):
            next_day = model.predict(last_sequence.reshape(1, sequence_length, 1))
            predictions.append(next_day[0][0])
            last_sequence = np.roll(last_sequence, -1)
            last_sequence[-1] = next_day[0][0]

        predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
        return dailyRentals, predictions
    def visualizeCapacityPrediction2(self, data, stationStopNo,sequence_length=3):
        # data.set_index('startTime', inplace=True)

        endStopData = data[data['endStop'] == stationStopNo]
        startStopData = data[data['startStop'] == stationStopNo]
        dailyRentals = endStopData['orderID'].resample('D').count() - startStopData['orderID'].resample(
            'D').count()
        dailyRentals[np.isnan(dailyRentals)] = 0

        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(dailyRentals.values.reshape(-1, 1))

        X, y = [], []

        for i in range(len(scaled_data) - sequence_length):
            X.append(scaled_data[i:i + sequence_length])
            y.append(scaled_data[i + sequence_length])

        X = np.array(X)
        y = np.array(y)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = Sequential()
        model.add(LSTM(units=50, activation='relu', input_shape=(sequence_length, 1)))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse')

        model.fit(X_train, y_train, epochs=68, batch_size=32)

        y_pred = model.predict(X_test)
        # rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        # mae = mean_absolute_error(y_test, y_pred)
        #
        # print(f'RMSE: {rmse}')
        # print(f'MAE: {mae}')

        last_sequence = scaled_data[-sequence_length:]
        predictions = []

        for i in range(7):
            next_day = model.predict(last_sequence.reshape(1, sequence_length, 1))
            predictions.append(next_day[0][0])
            last_sequence = np.roll(last_sequence, -1)
            last_sequence[-1] = next_day[0][0]

        predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
        return dailyRentals, predictions
    def saveToPdf(self,filename):
        p = PdfPages(filename)
        fig_nums = plt.get_fignums()
        figs = [plt.figure(n) for n in fig_nums]
        for fig in figs:
            fig.savefig(p, format='pdf')
        p.close()

    def visualizePlotting(self, data):
        # End-Start-Stop Distribution
        plt.rcParams["figure.figsize"] = [12.00, 8.00]
        plt.rcParams["figure.autolayout"] = True
        fig, ax1 = plt.subplots(3, 2)
        ax1[0, 0].bar(self.visualizeStartStopDistribution(data).index, self.visualizeStartStopDistribution(data).values, color='coral')
        ax1[0, 0].set_title("Start Stop Distribution")
        ax1[0, 0].set_xlabel("Start Stop")
        ax1[0, 0].set_ylabel("Count")
        ax1[0, 1].bar(self.visualizeEndStopDistribution(data).index, self.visualizeEndStopDistribution(data).values, color='lightskyblue')
        ax1[0, 1].set_title("End Stop Distribution")
        ax1[0, 1].set_xlabel("End Stop")
        ax1[0, 1].set_ylabel("Count")

        # Count Rentals
        ax1[1, 0].bar(self.visualizeCountRentals(data).index, self.visualizeCountRentals(data).values)
        ax1[1, 0].set_xticklabels(self.visualizeCountRentals(data).index, rotation=30)
        ax1[1, 0].set_title('Number of Rentals Each Day')
        ax1[1, 0].set_xlabel('Date')
        ax1[1, 0].set_ylabel('Number of Rentals')

        # Time Intervals
        ax1[1, 1].bar(range(1, 9), self.visualizeTimeIntervals(data),
                tick_label=['00:00-03:00', '03:00-06:00', '06:00-09:00', '09:00-12:00', '12:00-15:00', '15:00-18:00',
                            '18:00-21:00', '21:00-00:00'])
        ax1[1, 1].set_xticklabels(['00:00-03:00', '03:00-06:00', '06:00-09:00', '09:00-12:00', '12:00-15:00', '15:00-18:00',
                            '18:00-21:00', '21:00-00:00'], rotation=30)
        ax1[1, 1].set_xlabel('Time Intervals')
        ax1[1, 1].set_ylabel('Order Count')
        ax1[1, 1].set_title('Order Count in 8 Time Intervals')

        actualRental1, predictedRental1 = self.visualizeCapacityPrediction(data, 1)

        # Prediction
        ax1[2, 0].plot(pd.to_datetime(actualRental1.index), np.array(actualRental1), label='Actual Rentals')
        ax1[2, 0].plot(pd.date_range(start = pd.to_datetime(actualRental1.index[0]) + pd.Timedelta(days=8), periods=7), predictedRental1,
                 label='Predicted Rentals')
        ax1[2, 0].tick_params(axis='x', labelrotation=30)
        ax1[2, 0].set_xlabel('Date')
        ax1[2, 0].set_ylabel('Rental Count')
        ax1[2, 0].set_title('Predicted Rentals for the Next 7 Days for Rental Stop 1')

        actualRental2, predictedRental2 = self.visualizeCapacityPrediction2(data,2)

        # Prediction
        ax1[2, 1].plot(pd.to_datetime(actualRental2.index), np.array(actualRental2), label='Actual Rentals')
        ax1[2, 1].plot(pd.date_range(start = pd.to_datetime(actualRental2.index[0]) + pd.Timedelta(days=8), periods=7), predictedRental2,
                 label='Predicted Rentals')
        ax1[2, 1].tick_params(axis='x', labelrotation=30)
        ax1[2, 1].set_xlabel('Date')
        ax1[2, 1].set_ylabel('Rental Count')
        ax1[2, 1].set_title('Predicted Rentals for the Next 7 Days for Rental Stop 2')

        plt.rcParams["figure.figsize"] = [12.00, 8.00]
        plt.rcParams["figure.autolayout"] = True
        fig, ax2 = plt.subplots(3, 2)

        actualRental3, predictedRental3 = self.visualizeCapacityPrediction2(data,3)

        # Prediction
        ax2[0, 0].plot(pd.to_datetime(actualRental3.index), np.array(actualRental3), label='Actual Rentals')
        ax2[0, 0].plot(pd.date_range(start = pd.to_datetime(actualRental3.index[0]) + pd.Timedelta(days=8), periods=7), predictedRental3,
                 label='Predicted Rentals')
        ax2[0, 0].tick_params(axis='x', labelrotation=30)
        ax2[0, 0].set_xlabel('Date')
        ax2[0, 0].set_ylabel('Rental Count')
        ax2[0, 0].set_title('Predicted Rentals for the Next 7 Days for Rental Stop 3')

        actualRental4, predictedRental4 = self.visualizeCapacityPrediction2(data,4)

        # Prediction
        ax2[0, 1].plot(pd.to_datetime(actualRental4.index), np.array(actualRental4), label='Actual Rentals')
        ax2[0, 1].plot(pd.date_range(start = pd.to_datetime(actualRental4.index[0]) + pd.Timedelta(days=8), periods=7), predictedRental4,
                 label='Predicted Rentals')
        ax2[0, 1].tick_params(axis='x', labelrotation=30)
        ax2[0, 1].set_xlabel('Date')
        ax2[0, 1].set_ylabel('Rental Count')
        ax2[0, 1].set_title('Predicted Rentals for the Next 7 Days for Rental Stop 4')

        actualRental5, predictedRental5 = self.visualizeCapacityPrediction2(data,5)

        # Prediction
        ax2[1, 0].plot(pd.to_datetime(actualRental5.index), np.array(actualRental5), label='Actual Rentals')
        ax2[1, 0].plot(pd.date_range(start = pd.to_datetime(actualRental5.index[0]) + pd.Timedelta(days=8), periods=7), predictedRental5,
                 label='Predicted Rentals')
        ax2[1, 0].tick_params(axis='x', labelrotation=30)
        ax2[1, 0].set_xlabel('Date')
        ax2[1, 0].set_ylabel('Rental Count')
        ax2[1, 0].set_title('Predicted Rentals for the Next 7 Days for Rental Stop 5')

        actualRental6, predictedRental6 = self.visualizeCapacityPrediction2(data,1)

        # Prediction
        ax2[1, 1].plot(pd.to_datetime(actualRental6.index), np.array(actualRental6), label='Actual Rentals')
        ax2[1, 1].plot(pd.date_range(start = pd.to_datetime(actualRental6.index[0]) + pd.Timedelta(days=8), periods=7), predictedRental6,
                 label='Predicted Rentals')
        ax2[1, 1].tick_params(axis='x', labelrotation=30)
        ax2[1, 1].set_xlabel('Date')
        ax2[1, 1].set_ylabel('Rental Count')
        ax2[1, 1].set_title('Predicted Rentals for the Next 7 Days for Rental Stop 6')

        actualRental7, predictedRental7 = self.visualizeCapacityPrediction2(data,2)

        # Prediction
        ax2[2, 0].plot(pd.to_datetime(actualRental7.index), np.array(actualRental7), label='Actual Rentals')
        ax2[2, 0].plot(pd.date_range(start = pd.to_datetime(actualRental7.index[0]) + pd.Timedelta(days=8), periods=7), predictedRental7,
                 label='Predicted Rentals')
        ax2[2, 0].tick_params(axis='x', labelrotation=30)
        ax2[2, 0].set_xlabel('Date')
        ax2[2, 0].set_ylabel('Rental Count')
        ax2[2, 0].set_title('Predicted Rentals for the Next 7 Days for Rental Stop 7')

        actualRental8, predictedRental8 = self.visualizeCapacityPrediction2(data,3)

        # Prediction
        ax2[2, 1].plot(pd.to_datetime(actualRental8.index), np.array(actualRental8), label='Actual Rentals')
        ax2[2, 1].plot(pd.date_range(start = pd.to_datetime(actualRental8.index[0]) + pd.Timedelta(days=8), periods=7), predictedRental8,
                 label='Predicted Rentals')
        ax2[2, 1].tick_params(axis='x', labelrotation=30)
        ax2[2, 1].set_xlabel('Date')
        ax2[2, 1].set_ylabel('Rental Count')
        ax2[2, 1].set_title('Predicted Rentals for the Next 7 Days for Rental Stop 8')

        plt.savefig('multi_plot_image.pdf')
        plt.show()

        # filename = ('multi_plot_image')
        # p = PdfPages(filename)
        # fig_nums = plt.get_fignums()
        # figs = [plt.figure(n) for n in fig_nums]
        # for fig in figs:
        #     fig.savefig(p, format='pdf')
        # p.close()

    def openPdfInBrowser(self, filename):
        webbrowser.open(filename)

if __name__ == '__main__':
    manager = Manager()
    # data = manager.load_data("visualizationOrder.csv")
    # print(data.head())
    # print(data.columns)

    # manager = Manager()
    #
    # # export csv
    # table_name = '`Order`'
    # output_csv_file = 'visualizationOrder.csv'
    # manager.exportToCSV(table_name, output_csv_file)

    # generate pdf
    data = manager.load_data('visualizationOrder.csv')
    manager.visualizePlotting(data)
    filename = "multi_plot_image.pdf"
    # manager.saveToPdf(filename)
    manager.openPdfInBrowser(filename)

    # 新用户
    # manager = Manager()
    # par = ['RRR', '3022008a', 'zhangruixian98@gmail.com']
    # manager.generateCode(par)
    # flag = False
    # while not flag:
    #     code = input("Enter code: ")
    #     flag = manager.add(code)