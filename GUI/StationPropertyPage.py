from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import ttk, scrolledtext
from app import app


class StationPropertyPage():
    def __init__(self, app: app, master=None):
        self.__info_list = None
        self.__root = master
        self.__changeName = StringVar()
        self.__changePosition = StringVar()
        self.__changeCapacity = StringVar()
        self.__changeStationID = StringVar()
        self.__info_list = StringVar()
        self.__app = app

    def CreatePage(self):

        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("1000x600")
        # Top bar
        top_bar = Label(self.page, bg="lightcyan", height=3, width=800)
        top_bar.place(x=0, y=0)

        # Top title
        title_label = Label(top_bar, text="🔍 Property Management", bg="lightcyan", font=("Arial", 12, "bold"))
        title_label.place(x=10, y=5)

        # Buttons
        refresh_btn = Button(top_bar, command=self.refresh, text="Refresh", bg='#4CAF50', fg='white',
                             font=("Arial", 10))
        refresh_btn.place(x=230, y=5)

        back_btn = Button(top_bar, text="Back", command=self.quit, bg='#4CAF50', fg='white', font=("Arial", 10))
        back_btn.place(x=320, y=5)

        # Huge display box (Text widget)
        self.__info_list = scrolledtext.ScrolledText(self.page, width=130, height=15)
        self.__info_list.place(x=50, y=80)

        # Delete vehicle operation
        del_lbl = Label(self.page, text="Change station name:", bg='white', font=("Arial", 12))
        del_lbl.place(x=50, y=350)
        del_entry_lbl = Label(self.page, text="name", bg='white', font=("Arial", 10))
        del_entry_lbl.place(x=50, y=390)
        self.__changeName = Entry(self.page, width=20)
        self.__changeName.place(x=85, y=390)
        del_enter_btn = Button(self.page, command=self.changeName, text="Enter", bg='#4CAF50', fg='white',
                               font=("Arial", 10))
        del_enter_btn.place(x=250, y=390)
        del_clear_btn = Button(self.page, command=self.clear_1, text="Clear", bg='#4CAF50', fg='white',
                               font=("Arial", 10))
        del_clear_btn.place(x=320, y=390)

        label = Label(text="放到change name旁边")
        label.place(x=600, y=500)
        self.__changeStationID = Entry(self.page, width=20)
        self.__changeStationID.place(x=600, y=550)

        # Change battery operation
        battery_lbl = Label(self.page, text="Change station position:", bg='white', font=("Arial", 12))
        battery_lbl.place(x=50, y=450)
        battery_entry_lbl = Label(self.page, text="name", bg='white', font=("Arial", 10))
        battery_entry_lbl.place(x=50, y=490)

        self.__changePosition = Entry(self.page, width=20)
        self.__changePosition.place(x=85, y=490)
        battery_enter_btn = Button(self.page, command=self.changePosition, text="Enter", bg='#4CAF50', fg='white',
                                   font=("Arial", 10))
        battery_enter_btn.place(x=250, y=490)
        battery_clear_btn = Button(self.page, command=self.clear_3, text="Clear", bg='#4CAF50', fg='white',
                                   font=("Arial", 10))
        battery_clear_btn.place(x=320, y=490)

        # Move vehicle operation
        move_lbl = Label(self.page, text="Change capacity:", bg='white', font=("Arial", 12))
        move_lbl.place(x=400, y=350)
        move_entry_lbl = Label(self.page, text="name", bg='white', font=("Arial", 10))
        move_entry_lbl.place(x=400, y=390)
        self.__changeCapacity = Entry(self.page, width=20)
        self.__changeCapacity.place(x=435, y=390)

        move_enter_btn = Button(self.page, command=self.changeCapacity, text="Enter", bg='#4CAF50', fg='white',
                                font=("Arial", 10))
        move_enter_btn.place(x=600, y=390)
        move_clear_btn = Button(self.page, command=self.clear_2, text="Clear", bg='#4CAF50', fg='white',
                                font=("Arial", 10))
        move_clear_btn.place(x=670, y=390)

    def refresh(self):
        content = self.__info_list.get('1.0', END)
        if content.strip():
            self.__info_list.delete('1.0', END)
        list = self.__app.getAllStopsOP()
        for i in list:
            self.__info_list.insert(END, i + "\n")

    def changeName(self):
        id = self.__changeStationID.get()
        name = self.__changeName.get()
        flag = self.__app.updateVehicleStopNameOP(int(id), name)
        if flag:
            msgbox.showinfo("Success", "Successfully change!", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Please Check!", parent=self.page)

    def changeCapacity(self):
        id = self.__changeStationID.get()
        max = self.__changeCapacity.get()
        flag = self.__app.updateVehicleStopMaxCapacityOP(int(id), int(max))
        if flag:
            msgbox.showinfo("Success", "Successfully change!", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Please Check!", parent=self.page)

    def changePosition(self):
        id = self.__changeStationID.get()
        axis = self.__changePosition.get()
        flag = self.__app.updateVehicleStopAxisOP(int(id), axis)
        if flag:
            msgbox.showinfo("Success", "Successfully change!", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Please Check!", parent=self.page)

    def clear_1(self):
        self.__changeName.delete(0, END)
        self.__changeStationID.delete(0,END)

    def clear_2(self):
        self.__changeCapacity.delete(0, END)
        self.__changeStationID.delete(0, END)

    def clear_3(self):
        self.__changePosition.delete(0, END)
        self.__changeStationID.delete(0, END)

    def quit(self):
        self.page.destroy()
