from tkinter import *
import tkintermapview


class MapPage(object):
    def __init__(self, user, master=None):
        self.root = master
        self.user = user
        self.CreatePage()

    def CreatePage(self):
        self.page = Frame(self.root, width = 1000, height = 600)
        self.page.pack()

        # create map widget
        map_widget = tkintermapview.TkinterMapView(self.page, width=1500, height=1000, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

        map_widget.set_position(55.86847776160628, -4.274376402130314)
        map_widget.set_zoom(15)

        vehicle_local_list = self.user.get_locations()
        for row in vehicle_local_list:
            position = row[2]
            str_local_info = "Location_ID:" + row[0] + "  \nLocation_Name:" + row[1]
            xx = float(position.split(', ')[0])
            yy = float(position.split(', ')[1])
            map_widget.set_marker(xx, yy, text=str_local_info)

