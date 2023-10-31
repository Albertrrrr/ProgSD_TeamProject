from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import font
from GUI import Registration, customer_homapage, Operator, Manager_homepage,MapPage
from app import app


class LoginPage(object):
    def __init__(self,  master = None):
        self.__root = master
        self.__email = StringVar()
        self.__password = StringVar()
        self.__selected_value = IntVar()
        self.__root.geometry("1000x600")
        self.__app = app()

    def CreatePage(self):

        self.page = Frame(self.__root)
        self.page.pack()

        # Define fonts
        l1_font = font.Font(family="Helvetica", size=32, weight='bold')
        l2_font = font.Font(family="Helvetica", size=14)
        c_font = font.Font(family="Helvetica", size=14)
        b_font = font.Font(family="Helvetica", size=14)

        # Label 1
        label1 = Label(text="Bike-sharing", font=l1_font)
        label1.place(x=320, y=50)

        # Radio_button
        radio_button1 = Radiobutton(text="Customer",font = c_font, variable=self.__selected_value, value=1)
        radio_button1.place(x=250, y=160)
        radio_button2 = Radiobutton(text="Operator", font = c_font, variable=self.__selected_value, value=2)
        radio_button2.place(x=450, y=160)
        radio_button3 = Radiobutton(text="Manager", font = c_font, variable=self.__selected_value, value=3)
        radio_button3.place(x=650, y=160)

        # Labels for Username, Password, and Repeat Password
        label2 = Label(text="Email:", font=l2_font)
        label2.place(x=285, y=250)
        label3 = Label(text="Password:", font=l2_font)
        label3.place(x=280, y=330)

        # Entry Widgets
        self.__email = Entry(font=l2_font)
        self.__email.place(x=380, y=250, width=300, height=30)
        self.__password = Entry(font=l2_font, show="*")  # Show asterisks for password
        self.__password.place(x=380, y=330, width=300, height=30)

        # Buttons
        button1 = Button(text="Login", command = self.loginCheck, font=b_font)
        button1.place(x=450, y=420, width=100, height=40)
        button2 = Button(text="Register", command = self.register, font=b_font)
        button2.place(x=450, y=500, width=100, height=40)

    def register(self):
        Registration.RegisterPage(self.__root).CreatePage()

    def loginCustomer(self):
        self.page.destroy()
        customer_homapage.CustomerPage(self.__app,self.__root).CreatePage()

    def loginOperator(self):
        self.page.destroy()
        Operator.OperatorPage(self.__app,self.__root).CreatePage()

    def loginManager(self):
        Manager_homepage.ManagerPage(self.__app,self.__root).CreatePage()

    def loginCheck(self):
        email = self.__email.get()
        password = self.__password.get()

        selected = self.__selected_value.get()
        str_selected = str(selected)

        par = [email,password,str_selected]

        if selected == 1:
            flag = self.__app.login(par=par)
            if (flag):
                self.loginCustomer()
            else:
                msgbox.showwarning("Warning", "Check your email and password!")

        elif selected == 2:
            flag = self.__app.login(par=par)
            if (flag):
                self.loginOperator()
            else:
                msgbox.showwarning("Warning", "Check your email and password!")



        # elif selected == 3:
        #     flag = self.__app.login(par=par)
        #     if (flag):
        #         self.loginManager()
        #     else:
        #         msgbox.showwarning("Warning", "Check your email and password!")




