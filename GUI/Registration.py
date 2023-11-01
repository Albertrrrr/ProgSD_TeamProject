from tkinter import *
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import font
from . import LoginPage
from app import app

class RegisterPage():
    def __init__(self, master=None):
        self.__root = master
        self.__username = StringVar()
        self.__password = StringVar()
        self.__email = StringVar()
        self.__captcha = StringVar()
        self.__selected_value = IntVar()
        self.__app = app()


    def CreatePage(self):
        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("1000x600")


        # Define fonts
        l1_font = font.Font(family="Helvetica", size=32, weight='bold')
        l2_font = font.Font(family="Helvetica", size=14)
        c_font = font.Font(family="Helvetica", size=14)
        b_font = font.Font(family="Helvetica", size=14)
        e_font = font.Font(family="Helvetica", size=12)

        # Label 1
        label1 = Label(self.page, text="Welcome!", font=l1_font)
        label1.place(x=400, y=40)

        # Labels for Username, Password, and Repeat Password
        label2 = Label(self.page, text="Username:", font=l2_font)
        label2.place(x=280, y=150)
        label3 = Label(self.page, text="Password:", font=l2_font)
        label3.place(x=280, y=230)

        label5 = Label(self.page, text="Email:", font=l2_font)
        label5.place(x=305, y=310)
        label6 = Label(self.page, text="CAPTCHA:", font=l2_font)
        label6.place(x=270, y=390)

        label7 = Label(self.page, text="Note:If you are customer, you don't need to user captcha to register.", font=e_font)
        label7.place(x=320, y=100)

        # Entry Widgets
        self.__username = Entry(self.page,font=l2_font)
        self.__username.place(x=380, y=150, width=350, height=30)


        self.__password= Entry(self.page,font=l2_font, show="*")  # Show asterisks for password
        self.__password.place(x=380, y=230, width=350, height=30)


        self.__email = Entry(self.page,font=l2_font)
        self.__email.place(x=380, y=310, width=350, height=30)


        self.__captcha = Entry(self.page,font=l2_font)
        self.__captcha.place(x=380, y=390, width=350, height=30)

        # Checkbuttons for User Type

        radio_button1 = Radiobutton(self.page,text="Customer", font=c_font, variable=self.__selected_value, value=1)
        radio_button1.place(x=250, y=470)
        radio_button2 = Radiobutton(self.page,text="Operator", font=c_font, variable=self.__selected_value, value=2)
        radio_button2.place(x=450, y=470)
        radio_button3 = Radiobutton(self.page,text="Manager", font=c_font, variable=self.__selected_value, value=3)
        radio_button3.place(x=650, y=470)

        button2 = Button(self.page, text="Register" , command=self.registerCheck, font=b_font, bg='green', fg='white')
        button2.place(x=450, y=530, width=100, height=40)
        button2 = Button(self.page,command = self.Code, text="Get verification_code", font=b_font)
        button2.place(x=760, y=400, width=200, height=30)

    def Code(self):
        username = self.__username.get()
        password = self.__password.get()
        email = self.__email.get()

        par = [username, password, email]

        selected = self.__selected_value.get()
        k = self.__app.generateCodeOP(par, str(selected))
        print("k",k)
        flagCode = self.__app.flagCode()
        if flagCode:
            msgbox.showinfo("Success", "Successfully generate Code!", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Check your email and password!", parent=self.page)

    def registerCheck(self):
        username =  self.__username.get()
        password = self.__password.get()
        email = self.__email.get()

        par = [username, password, email]

        selected = self.__selected_value.get()

        if selected == 1:
            flag = self.__app.register(par=par)
            if flag:
                msgbox.showinfo("Success","Successfully Register!",parent = self.page)
            else:
                msgbox.showwarning("Warning","Check your email and password!",parent = self.page)

        elif selected == 2:
            code = self.__captcha.get()
            flag = self.__app.registerOM(par,code,str(selected))
            if flag:
                msgbox.showinfo("Success","Successfully Register!",parent = self.page)
            else:
                msgbox.showwarning("Warning","Check your CAPTCHA!",parent = self.page)

        elif selected == 3:
            code = self.__captcha.get()
            flag = self.__app.registerOM(par, code, str(selected))
            if flag:
                msgbox.showinfo("Success", "Successfully Register!", parent=self.page)
            else:
                msgbox.showwarning("Warning", "Check your CAPTCHA!", parent=self.page)






