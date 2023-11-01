from tkinter import *
from tkinter import scrolledtext
from app import app
import tkinter.messagebox as msgbox

class HistoryPage(object):
    def __init__(self, app:app, master=None):
        self.__root = master
        self.__info_list = None
        self.__info_list_2 = None
        self.__app = app
        self.__info = None

    def CreatePage(self):

        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("1300x600")

        # Oder history information
        label1 = Label(self.page, text="Order history information", bg="lightcyan", font=("Arial", 18))
        label1.place(x=20, y=90)

        back_button = Button(self.page, text="Back", command = self.quit, bg='#000000', fg='white')
        back_button.place(x=50, y=20, width = 80, height = 30)

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

        self.__info_list_2 = scrolledtext.ScrolledText(self.page, width=50, height=8)
        self.__info_list_2.place(x=10, y=300)

        pay_button = Button(self.page, command = self.pay, text="Pay", bg='#4CAF50', fg='white')
        pay_button.place(x=100, y=460,width = 120, height = 60)

        res = self.__app.getOrderList()
        unpaidlist = self.__app.getUnfilledOrder()

        for i in res:
            self.__info_list.insert(END, i + "\n")

        for r in unpaidlist:
            self.__info_list_2.insert(END, r + "\n")



    def pay(self):
        flag = self.__app.payToOrder()
        if(flag):
            msgbox.showinfo("Success", "Successfully pay!",parent=self.page)
        else:
            msgbox.showwarning("Warning","Unable to pay",parent=self.page)


    def quit(self):
        self.page.destroy()

    def refresh(self):
        content = self.__info_list.get('1.0', END)
        if content.strip():
            self.__info_list.delete('1.0', END)

        content_2 = self.__info_list_2.get('1.0', END)
        if content_2.strip():
            self.__info_list_2.delete('1.0', END)

        res = self.__app.getOrderList()
        unpaidlist = self.__app.getUnfilledOrder()

        for i in res:
            self.__info_list.insert(END, i + "\n")

        for r in unpaidlist:
            self.__info_list_2.insert(END, r + "\n")

