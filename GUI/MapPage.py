from tkinter import *
import tkintermapview
import pymysql
from tkmacosx import Button
from config import mysql_config

class MapPage(object):
    def __init__(self,  master=None):
        self.__root = master

    def CreatePage(self):
        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("1000x600")

        # create map widget
        map_widget = tkintermapview.TkinterMapView(self.page, width=1500, height=1000, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

        map_widget.set_position(55.86847776160628, -4.274376402130314)
        map_widget.set_zoom(15)

        # vehicle_local_list = self.user.get_locations()

        # connect to mysql
        db = pymysql.connect(**mysql_config)
        cursor = db.cursor()

        cursor.execute("SELECT * from VehicleStop")

        vehicle_local_list = cursor.fetchall()

        for row in vehicle_local_list:
            position = row[2]

            str_local_info = "Location_ID:" + str(row[0]) + "  \n" + str(row[1])
            print(str_local_info)

            xx_str = position.split(',')[0]
            xx = float(xx_str[1:])

            yy_str = position.split(',')[1]
            yy = float(yy_str[:-1])

            print(yy)

            map_widget.set_marker(xx, yy, text=str_local_info)

