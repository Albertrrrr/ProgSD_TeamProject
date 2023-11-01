from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import ttk, scrolledtext
from app import app

class VehicleManagementPage():
    def __init__(self, app:app, master=None):
        self.__info_list = None
        self.__delete = StringVar()
        self.__battery = StringVar()
        self.__vehicle = StringVar()
        self.__vehicle_move = StringVar()
        self.__track = StringVar()
        self.__track_message = None
        self.__root = master
        self.__app = app

    def CreatePage(self):

        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("800x600")

        top_bar = Label(self.page, bg="lightcyan", height=3, width=800)
        top_bar.place(x=0, y=0)

        # Top title
        title_label = Label(top_bar, text="🔍 Vehicle Management", bg="lightcyan", font=("Arial", 12, "bold"))
        title_label.place(x=10, y=5)

        # Buttons
        refresh_btn = Button(top_bar, command = self.refresh,text="Refresh", bg='#4CAF50', fg='white', font=("Arial", 10))
        refresh_btn.place(x=230, y=5)

        back_btn = Button(top_bar, text="Back", command = self.quit, bg='#4CAF50', fg='white', font=("Arial", 10))
        back_btn.place(x=320, y=5)



        self.__info_text = scrolledtext.ScrolledText(self.page, width=100, height=15)
        self.__info_text.place(x=50, y=80)

        # Delete vehicle operation
        del_lbl = Label(self.page, text="Delete vehicle:", bg="#add8e6", font=("Arial", 12))
        del_lbl.place(x=50, y=350)
        del_entry_lbl = Label(self.page, text="ID:", font=("Arial", 10))
        del_entry_lbl.place(x=50, y=390)
        self.__delete = Entry(self.page, width=20)
        self.__delete.place(x=85, y=390)
        del_enter_btn = Button(self.page, text="Enter", command = self.delete_vehicle, bg='#4CAF50', fg='white', font=("Arial", 10))
        del_enter_btn.place(x=250, y=390)
        del_clear_btn = Button(self.page, text="Clear", command = self.clear_vehicle, bg='#4CAF50', fg='white', font=("Arial", 10))
        del_clear_btn.place(x=320, y=390)

        # Change battery operation
        battery_lbl = Label(self.page, text="Change battery:", bg="#add8e6", font=("Arial", 12))
        battery_lbl.place(x=50, y=450)
        battery_entry_lbl = Label(self.page, text="ID:", font=("Arial", 10))
        battery_entry_lbl.place(x=50, y=490)
        self.__battery = Entry(self.page, width=20)
        self.__battery.place(x=85, y=490)
        battery_enter_btn = Button(self.page, command = self.change_battery,text="Enter", bg='#4CAF50', fg='white', font=("Arial", 10))
        battery_enter_btn.place(x=250, y=490)
        battery_clear_btn = Button(self.page,  text="Clear", command = self.clear_battery ,bg='#4CAF50', fg='white', font=("Arial", 10))
        battery_clear_btn.place(x=320, y=490)

        # Move vehicle operation
        move_lbl = Label(self.page, text="Move vehicle:", bg="#add8e6", font=("Arial", 12))
        move_lbl.place(x=400, y=350)
        move_entry_lbl = Label(self.page, text="ID:", font=("Arial", 10))
        move_entry_lbl.place(x=400, y=390)
        self.__vehicle = Entry(self.page, width=20)
        self.__vehicle.place(x=435, y=390)
        move_input_lbl = Label(self.page, text="Move:", font=("Arial", 10))
        move_input_lbl.place(x=400, y=430)
        self.__vehicle_move = Entry(self.page, width=20)
        self.__vehicle_move.place(x=435, y=430)
        move_enter_btn = Button(self.page, command = self.move_vehicle,text="Enter", bg='#4CAF50', fg='white', font=("Arial", 10))
        move_enter_btn.place(x=600, y=390)
        move_clear_btn = Button(self.page, command = self.clear_move, text="Clear", bg='#4CAF50', fg='white', font=("Arial", 10))
        move_clear_btn.place(x=670, y=390)

        # Track vehicle operation
        track_lbl = Label(self.page, text="Track vehicle:", bg="#add8e6", font=("Arial", 12))
        track_lbl.place(x=400, y=470)
        track_entry_lbl = Label(self.page, text="ID:", font=("Arial", 10))
        track_entry_lbl.place(x=400, y=510)
        self.__track = Entry(self.page, width=20)
        self.__track.place(x=435, y=510)
        track_enter_btn = Button(self.page, command = self.track_vehicle,text="Enter", bg='#4CAF50', fg='white', font=("Arial", 10))
        track_enter_btn.place(x=600, y=510)
        track_clear_btn = Button(self.page, command = self.clear_track,text="Clear", bg='#4CAF50', fg='white', font=("Arial", 10))
        track_clear_btn.place(x=670, y=510)
        self.__track_message = Label(self.page,font = ("Arial",12))
        self.__track_message.place(x = 400, y = 545)

    def refresh(self):
        content = self.__info_text.get('1.0', END)
        if content.strip():
            self.__info_text.delete('1.0', END)
        res = self.__app.getAllVehicleOP()
        for i in res:
            self.__info_text.insert(END, i + "\n")

    def delete_vehicle(self):
        bikeID = self.__delete.get()
        flag = self.__app.deleteVehicleOP(int(bikeID))
        if (flag):
            msgbox.showinfo("Success", "Successfully delete!",parent = self.page)
        else:
            msgbox.showwarning("Warning", "Unable to delete",parent = self.page)

    def quit(self):
        self.page.destroy()

    def clear_vehicle(self):
        self.__delete.delete(0,END)
    def clear_battery(self):
        self.__battery.delete(0,END)
    def clear_move(self):
        self.__vehicle.delete(0,END)
        self.__vehicle_move.delete(0,END)
    def clear_track(self):
        self.__track.delete(0,END)

    def change_battery(self):
        bikeID = self.__battery.get()
        flag = self.__app.changeBatteryOP(int(bikeID))
        if (flag):
            msgbox.showinfo("Success", "Successfully change!",parent = self.page)
        else:
            msgbox.showwarning("Warning", "Unable to change",parent = self.page)

    def move_vehicle(self):
        bikeID = self.__vehicle.get()
        stopID = self.__vehicle_move.get()
        flag = self.__app.changeLocationOP(int(bikeID),int(stopID))
        if (flag):
            msgbox.showinfo("Success", "Successfully change!",parent = self.page)
        else:
            msgbox.showwarning("Warning", "Unable to change",parent = self.page)

    def track_vehicle(self):
        bikeID = self.__track.get()

        flag = self.__app.track(int(bikeID))

        if flag:
            finalstr = "bikeID: "+ str(bikeID) + "  Current Stop is : " + str(flag)
            self.__track_message.config(text = finalstr)
            print(flag)

        else:
            msgbox.showwarning("Warning", "Unable to track",parent = self.page)



