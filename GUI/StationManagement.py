from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import ttk, scrolledtext
from app import app

class StationManagementPage():
    def __init__(self, app:app, master=None):
        self.__info_list = None
        self.__root = master
        self.__app = app

    def CreatePage(self):

        top_bar = Label(self.page, bg="lightcyan", height=3, width=800)
        top_bar.place(x=0, y=0)

        # Top title
        title_label = Label(top_bar, text="🔍 Property Management", bg="lightcyan", font=("Arial", 12, "bold"))
        title_label.place(x=10, y=5)

        # Buttons
        refresh_btn = Button(top_bar, text="Refresh", bg='#4CAF50', fg='white', font=("Arial", 10))
        refresh_btn.place(x=230, y=5)

        back_btn = Button(top_bar, text="Back", bg='#4CAF50', fg='white', font=("Arial", 10))
        back_btn.place(x=320, y=5)

        # Huge display box (Text widget)
        display_box = Text(self.page, width=100, height=15)
        display_box.place(x=50, y=80)

        # Delete vehicle operation
        del_lbl = Label(self.page, text="Add a new bike:", bg='white', font=("Arial", 12))
        del_lbl.place(x=50, y=350)
        del_entry_lbl = Label(self.page, text="place", bg='white', font=("Arial", 10))
        del_entry_lbl.place(x=50, y=390)
        del_entry = Entry(window, width=20)
        del_entry.place(x=85, y=390)
        del_enter_btn = Button(self.page, text="Enter", bg='#4CAF50', fg='white', font=("Arial", 10))
        del_enter_btn.place(x=250, y=390)
        del_clear_btn = Button(self.page, text="Clear", bg='#4CAF50', fg='white', font=("Arial", 10))
        del_clear_btn.place(x=320, y=390)

        # Change battery operation
        battery_lbl = Label(self.page, text="delete station:", bg='white', font=("Arial", 12))
        battery_lbl.place(x=50, y=510)
        battery_entry_lbl = Label(self.page, text="name", bg='white', font=("Arial", 10))
        battery_entry_lbl.place(x=50, y=550)
        battery_entry = Entry(self.page, width=20)
        battery_entry.place(x=85, y=550)
        battery_enter_btn = Button(self.page, text="Enter", bg='#4CAF50', fg='white', font=("Arial", 10))
        battery_enter_btn.place(x=250, y=550)
        battery_clear_btn = Button(self.page, text="Clear", bg='#4CAF50', fg='white', font=("Arial", 10))
        battery_clear_btn.place(x=320, y=550)

        # Move vehicle operation
        move_lbl = Label(self.page, text="Add a new station:", bg='white', font=("Arial", 12))
        move_lbl.place(x=400, y=350)
        move_entry_lbl = Label(self.page, text="name", bg='white', font=("Arial", 10))
        move_entry_lbl.place(x=400, y=400)
        move_entry = Entry(self.page, width=20)
        move_entry.place(x=435, y=400)
        move_entry_lbl = Label(self.page, text="place", bg='white', font=("Arial", 10))
        move_entry_lbl.place(x=400, y=450)
        move_entry = Entry(self.page, width=20)
        move_entry.place(x=435, y=450)
        move_entry_lbl = Label(self.page, text="Max", bg='white', font=("Arial", 10))
        move_entry_lbl.place(x=400, y=500)
        move_entry = Entry(self.page, width=20)
        move_entry.place(x=435, y=500)

        move_enter_btn = Button(self.page, text="Enter", bg='#4CAF50', fg='white', font=("Arial", 10))
        move_enter_btn.place(x=600, y=390)
        move_clear_btn = Button(self.page, text="Clear", bg='#4CAF50', fg='white', font=("Arial", 10))
        move_clear_btn.place(x=670, y=390)

        # Radio buttons for Add a new bike section
        bike_type = StringVar()  # Variable to hold the selected value

        bike_radio = Radiobutton(self.page, text="bike", variable=bike_type, value="bike", bg="white")
        ebike_radio = Radiobutton(self.page, text="e-bike", variable=bike_type, value="e-bike", bg="white")

        bike_radio.place(x=85, y=420)
        ebike_radio.place(x=135, y=420)
