from tkinter import *
from tkinter import scrolledtext

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
        self.page.geometry("1300x600")

        # window.config(bg='lightcyan')

        # Oder history information
        label1 = Label(self.page, text="Order history information", bg="lightcyan", font=("Arial", 18))
        label1.place(x=20, y=40)

        back_button = Button(self.page, text="Back", command = self.quit, bg='#000000', fg='white')
        back_button.place(x=50, y=120, width = 80, height = 30)

        # Oder information
        label2 = Label(self.page, text="Order information", font=("Arial", 16))
        label2.place(x=600, y=20)


        refresh_button = Button(self.page, text="Refresh",bg='#4CAF50', fg='white', command = self.refresh)
        refresh_button.place(x = 50, y = 170, width = 100, height = 30)

        self.__info_list = scrolledtext.ScrolledText(self.page, width = 125, height = 36)
        self.__info_list.place(x=400, y=60)

        # Unfilled orders
        label3 = Label(self.page, text="Unfilled orders",bg="lightcyan", font=("Arial", 16))
        label3.place(x=50, y=250)

        self.__info_list2 = scrolledtext.ScrolledText(self.page, width=50, height=8)
        self.__info_list2.place(x=10, y=300)


        # You have successfully paid order


        pay_button = Button(self.page, command = self.pay, text="Pay", bg='#4CAF50', fg='white')
        pay_button.place(x=100, y=460,width = 120, height = 60)



    def pay(self):
        flag = self.__app.payToOrder()
        if(flag):
            msgbox.showinfo("Success", "Successfully pay!",parent=self.page)
        else:
            msgbox.showwarning("Warning","Unable to pay",parent=self.page)


    def quit(self):
        self.page.destroy()

    def refresh(self):
        res = self.__app.getOrderList()
        unpaidlist = self.__app.getUnfilledOrder()
        for i in res:
            self.__info_list.insert(END, i + "\n")
        for i in unpaidlist:
            self.__info_list2.insert(END, i + "\n")

