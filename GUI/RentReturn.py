from tkinter import *
from app import app

class RentReturnPage(object):
    def __init__(self, app: app, master=None):
        self.__root = master
        self.__app = app

    def CreatePage(self):
        self.page = Toplevel(self.__root)
        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("1000x600")

        # Stop
        stop_label = Label(self.page, text="Stop:", bg="lightcyan", font=("Arial", 14))
        stop_label.place(x=50, y=60)
        stop_entry = Entry(self.page)
        stop_entry.place(x=110, y=60, width=50)

        # Back button
        back_button = Button(self.page, text="Back", bg='#4CAF50', fg='white')
        back_button.place(x=100, y=130)

        # Vehicle information
        vehicle_label = Label(self.page, text="Vehicle information", bg="lightcyan", font=("Arial", 14))
        vehicle_label.place(x=500, y=30)
        vehicle_info = Text(self.page, height=15, width=60)
        vehicle_info.place(x=440, y=70)

        # Rent
        rent_label = Label(self.page, text="Rent:", bg="lightcyan", font=("Arial", 14))
        rent_label.place(x=50, y=280)
        rent_entry = Entry(self.page)
        rent_entry.place(x=110, y=280, width=220)
        rent_button = Button(self.page, text="Enter", bg='#4CAF50', fg='white')
        rent_button.place(x=350, y=280)

        # Report damage button
        report_button = Button(self.page, text="Report damage", bg='#4CAF50', fg='white')
        report_button.place(x=100, y=320)

        # Return
        return_label = Label(self.page, text="Return:", bg="lightcyan", font=("Arial", 14))
        return_label.place(x=500, y=280)
        return_entry = Entry(self.page)
        return_entry.place(x=580, y=280, width=220)
        return_button = Button(self.page, text="Pay", bg='#4CAF50', fg='white')
        return_button.place(x=820, y=280)

        # Enter button for Return
        return_enter_button = Button(self.page, text="Enter", bg='#4CAF50', fg='white')
        return_enter_button.place(x=820, y=320)
