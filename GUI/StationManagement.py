from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import ttk, scrolledtext
from app import app

class StationManagementPage():
    def __init__(self, app:app, master=None):
        self.__info_list = None
        self.__root = master
        self.__addPlace = StringVar()
        self.__statioName = StringVar()
        self.__stationPlace = StringVar()
        self.__stationMax = StringVar()
        self.__delete_stationName = StringVar()
        self.__bike_type = StringVar()
        self.__app = app

    def CreatePage(self):

        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("1000x600")

        top_bar = Label(self.page, bg="lightcyan", height=3, width=800)
        top_bar.place(x=0, y=0)

        # Top title
        title_label = Label(top_bar, text="🔍 Stop Management", bg="lightcyan", font=("Arial", 12, "bold"))
        title_label.place(x=10, y=5)

        # Buttons
        refresh_btn = Button(top_bar, command = self.refresh, text="Refresh", bg='#4CAF50', fg='white', font=("Arial", 10))
        refresh_btn.place(x=230, y=5)

        back_btn = Button(top_bar, command = self.quit, text="Back", bg='#4CAF50', fg='white', font=("Arial", 10))
        back_btn.place(x=320, y=5)


        self.__info_list = scrolledtext.ScrolledText(self.page, width = 130, height = 15)
        self.__info_list.place(x=50, y=80)

        # Delete vehicle operation
        del_lbl = Label(self.page, text="Add a new bike:", bg="#add8e6", font=("Arial", 12))
        del_lbl.place(x=50, y=350)
        del_entry_lbl = Label(self.page, text="place", font=("Arial", 10))
        del_entry_lbl.place(x=50, y=390)
        self.__addPlace = Entry(self.page, width=20)
        self.__addPlace.place(x=85, y=390)
        del_enter_btn = Button(self.page, command = self.addBike, text="Enter", bg='#4CAF50', fg='white', font=("Arial", 10))
        del_enter_btn.place(x=250, y=390)
        del_clear_btn = Button(self.page, text="Clear", command=self.clear_1, bg='#4CAF50', fg='white', font=("Arial", 10))
        del_clear_btn.place(x=320, y=390)

        # Change battery operation
        battery_lbl = Label(self.page, text="delete station:", bg="#add8e6", font=("Arial", 12))
        battery_lbl.place(x=50, y=510)
        battery_entry_lbl = Label(self.page, text="id", font=("Arial", 10))
        battery_entry_lbl.place(x=50, y=550)
        self.__delete_stationName = Entry(self.page, width=20)
        self.__delete_stationName.place(x=85, y=550)
        battery_enter_btn = Button(self.page, command=self.delete, text="Enter", bg='#4CAF50', fg='white', font=("Arial", 10))
        battery_enter_btn.place(x=250, y=550)
        battery_clear_btn = Button(self.page, command=self.clear_2, text="Clear", bg='#4CAF50', fg='white', font=("Arial", 10))
        battery_clear_btn.place(x=320, y=550)

        # Move vehicle operation
        move_lbl = Label(self.page, text="Add a new station:", bg="#add8e6" ,font=("Arial", 12))
        move_lbl.place(x=400, y=350)
        move_entry_lbl = Label(self.page, text="name",  font=("Arial", 10))
        move_entry_lbl.place(x=400, y=400)
        self.__statioName = Entry(self.page, width=20)
        self.__statioName.place(x=435, y=400)
        move_entry_lbl = Label(self.page, text="place",  font=("Arial", 10))
        move_entry_lbl.place(x=400, y=450)
        self.__stationPlace = Entry(self.page, width=20)
        self.__stationPlace.place(x=435, y=450)
        move_entry_lbl = Label(self.page, text="Max",  font=("Arial", 10))
        move_entry_lbl.place(x=400, y=500)
        self.__stationMax = Entry(self.page, width=20)
        self.__stationMax.place(x=435, y=500)

        move_enter_btn = Button(self.page, command=self.addStation, text="Enter", bg='#4CAF50', fg='white', font=("Arial", 10))
        move_enter_btn.place(x=600, y=390)
        move_clear_btn = Button(self.page, command = self.clear_3,text="Clear", bg='#4CAF50', fg='white', font=("Arial", 10))
        move_clear_btn.place(x=670, y=390)



        bike_radio = Radiobutton(self.page, text="bike", variable=self.__bike_type, value=1, bg="white")
        ebike_radio = Radiobutton(self.page, text="E-bike", variable=self.__bike_type, value=2, bg="white")

        bike_radio.place(x=85, y=420)
        ebike_radio.place(x=135, y=420)

    def quit(self):
        self.page.destroy()

    def refresh(self):
        content = self.__info_list.get('1.0',END)
        if content.strip():
            self.__info_list.delete('1.0',END)
        list = self.__app.getAllStopsOP()
        for i in list:
            self.__info_list.insert(END, i + "\n")

    def addBike(self):
        place = self.__addPlace.get()
        selected = self.__bike_type.get()
        str_selected = str(selected)
        par = [str_selected, int(place), "normal"]
        flag = self.__app.addVehicleOP(par)
        if flag:
            msgbox.showinfo("Success", "Successfully add!", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Please Check!", parent=self.page)

    def delete(self):
        id = self.__delete_stationName.get()
        flag = self.__app.deleteVehicleStopOP(int(id))
        if flag:
            msgbox.showinfo("Success", "Successfully delete!", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Please Check!", parent=self.page)

    def addStation(self):
        name = self.__statioName.get()
        place = self.__stationPlace.get()
        Max = self.__stationMax
        par = [name,place,Max]
        flag = self.__app.addVehicleStopOP(par)
        if flag:
            msgbox.showinfo("Success", "Successfully add!", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Please Check!", parent=self.page)

    def clear_1(self):
        self.__addPlace.delete(0, END)

    def clear_2(self):
        self.__delete_stationName.delete(0,END)

    def clear_3(self):
        self.__stationPlace.delete(0,END)
        self.__statioName.delete(0, END)
        self.__stationMax.delete(0, END)






