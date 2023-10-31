from tkinter import *
from app import app
import pymysql
import tkinter.messagebox as msgbox

class HistoryPage(object):
    def __init__(self, app:app, master=None):
        self.__root = master
        self.__app = app
        self.__info = None

    def CreatePage(self):

        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("1100x600")

        # window.config(bg='lightcyan')

        # Oder history information
        label1 = Label(self.page, text="Order history information", bg="lightcyan", font=("Arial", 14))
        label1.place(x=50, y=50)

        back_button = Button(self.page, text="Back", command = self.quit, bg='#4CAF50', fg='white')
        back_button.place(x=50, y=150, width = 80, height = 30)

        # Oder information
        label2 = Label(self.page, text="Order information", font=("Arial", 14))
        label2.place(x=400, y=20)


        refresh_button = Button(self.page, text="Refresh history", command = self.refresh)
        refresh_button.place(x = 50, y = 200, width = 100, height = 30)

        self.__info_list = Listbox(self.page)
        self.__info_list.place(x=300, y=60, width=780, height=520)

        # Unfilled orders
        label3 = Label(self.page, text="Unfilled orders", font=("Arial", 14))
        label3.place(x=50, y=250)

        self.__info_list2 = Listbox(self.page)
        self.__info_list2.place(x=50, y=300, width=200, height=30)


        # You have successfully paid order
        label4 = Label(self.page, text="You have successfully paid order", font=("Arial", 14))
        label4.place(x=50, y=450)

        pay_button = Button(self.page, command = self.pay, text="Pay", bg='#4CAF50', fg='white')
        pay_button.place(x=50, y=550)

        entry3 = Entry(self.page)
        entry3.place(x=70, y=550, width=200, height=30)

    def pay(self):
        flag = self.__app.payToOrder()
        if(flag):
            msgbox.showinfo("Success", "Successfully pay!")
        else:
            msgbox.showwarning("Warning","Unable to pay")


    def quit(self):
        self.page.destroy()

    def refresh(self):
        res = self.__app.getOrderList()
        unpaidlist = self.__app.getUnfilledOrder()
        for i in res:
            self.__info_list.insert(END, i)
        for i in unpaidlist:
            self.__info_list2.insert(END,i)

