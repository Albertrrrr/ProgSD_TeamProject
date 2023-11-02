from tkinter import *
from tkinter import scrolledtext
import tkinter.messagebox as msgbox

from app import app

class RentReturnPage(object):
    def __init__(self, app: app, master=None):
        self.__root = master
        self.__report = StringVar()
        self.__rent = StringVar()
        self.__return = StringVar()
        self.__info_text = None
        self.__app = app

    def CreatePage(self):
        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("1000x600")

        # Stop
        stop_label = Label(self.page, text="Current Stop:", bg="lightcyan", font=("Arial", 14))
        stop_label.place(x=50, y=60)

        label = Label(self.page, text = str(self.__app.stopID), font=("Arial", 20))
        label.place(x=210, y = 50)

        # Back button
        back_button = Button(self.page,command = self.quit, text="Back", bg='#000000', fg='white')
        back_button.place(x=60, y=130)

        # Vehicle information
        vehicle_label = Label(self.page, text="Vehicle information", bg="lightcyan", font=("Arial", 14,"bold"))
        vehicle_label.place(x=500, y=60)

        self.__info_text = scrolledtext.ScrolledText(self.page, width= 60 , height = 15)
        self.__info_text.place(x=500, y=100)

        r_button = Button(self.page,command = self.refresh, text = "Refresh",bg='#4CAF50', fg='white')
        r_button.place(x = 130, y = 130)


        # Rent
        rent_label = Label(self.page, text="Rent:", bg="lightcyan", font=("Arial", 14))
        rent_label.place(x=50, y=350)
        rent_label = Label(self.page, text="ID", font=("Arial", 10))
        rent_label.place(x=125, y=350)
        rent_label = Label(self.page, text="Report:", bg="lightcyan", font=("Arial", 14))
        rent_label.place(x=50, y=400)
        rent_label = Label(self.page, text="ID", font=("Arial", 10))
        rent_label.place(x=125, y=400)
        self.__rent = Entry(self.page)
        self.__rent.place(x=160, y=350, width=120)
        rent_button = Button(self.page, command = self.rent, text="Enter", bg='#4CAF50', fg='white')
        rent_button.place(x=350, y=350)

        # Report damage button
        report_button = Button(self.page, command= self.reportDamage, text="Report damage", bg='#4CAF50', fg='white')
        report_button.place(x=350, y=400)

        # Return
        return_label = Label(self.page, text="Return:", bg="lightcyan", font=("Arial", 14))
        return_label.place(x=500, y=350)
        return_label = Label(self.page, text="ID", font=("Arial", 10))
        return_label.place(x=600, y=350)
        self.__return = Entry(self.page)
        self.__return.place(x=620, y=350, width=110)
        return_button = Button(self.page, command = self.pay, text="Pay", bg='#4CAF50', fg='white')
        return_button.place(x=620, y=390,width = 100)

        # Enter button for Return
        return_enter_button = Button(self.page, command = self.returnBike, text="Enter", bg='#4CAF50', fg='white')
        return_enter_button.place(x=820, y=350)

        self.__report = Entry(self.page)
        self.__report.place(x=160, y=400, width=120)

        res = self.__app.getAvailableVehicle()
        for i in res:
            self.__info_text.insert(END, i + "\n")

    def refresh(self):
        content = self.__info_text.get('1.0', END)
        if content.strip():
            self.__info_text.delete('1.0', END)
        res = self.__app.getAvailableVehicle()
        for i in res:
            self.__info_text.insert(END, i + "\n")

    def quit(self):
        self.page.destroy()

    def rent(self):
        bikeID = self.__rent.get()
        flag = self.__app.rentVehicle(bikeID)
        print(flag)
        if flag:
            msgbox.showinfo("Success", "Successfully rent!",parent=self.page)
        else:
            msgbox.showwarning("Warning", "Check your unpaid order",parent=self.page)

    def returnBike(self):
        stopID = self.__return.get()
        flag = self.__app.returnVehicle(stopID)
        if flag:
            msgbox.showinfo("Success", "Successfully return!",parent = self.page)
        else:
            msgbox.showwarning("Warning", "Please retry!",parent = self.page)

    def pay(self):
        flag = self.__app.payOrder()
        if flag:
            msgbox.showinfo("Success", "Successfully pay!",parent = self.page)
        else:
            msgbox.showwarning("Warning", "Please retry!",parent = self.page)

    def reportDamage(self):
        bikeID = self.__report.get()
        flag = self.__app.reportCustomer(bikeID)
        if flag:
            msgbox.showinfo("Success", "Successfully report!",parent = self.page)
        else:
            msgbox.showwarning("Warning", "Please retry!",parent = self.page)