from tkinter import *
import tkinter.messagebox as msgbox
from modules import
from GUI import CustomerIndex

class LoginPage(object):
    def __init__(self):
        self.root = master
        self.root.geometry("1600x1200")
        self.username = StringVar()
        self.password = StringVar()
        self.CreatePage()

    def CreatePage(self):
        self.page = Frame(self.root)
        self.page.pack()

        Label(self.page).grid(row=0, stick=W)
        Button(self.page, text='Customers')
        Button(self.page, text='Operators')
        Button(self.page, text='Managers')
        Label(self.page, text='Username: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='Password: ').grid(row=3, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='Log in', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='Register', command=self.register).grid(row=3, column=1)

    def wrongPassword(self):
        self.username.initialize("")
        self.password.initialize("")
        msgbox.showwarning("WARNING","The username or password you entered in incorrect! Please try again!")
    def loginCheck(self):
        username = self.username.get()
        password = self.password.get()

        if username == "":
            msgbox.showwarning("WARNING", "Please Enter your Username to Log in!")
        elif password == "":
            msgbox.showwarning("WARNING","Please Enter your Password to Log in")
        else:
            user = User.User(username)
            role = user.login(password)
            if role:
                self.page.destroy()
                if role == 'C':
                    customer = Customer.Customer(username)
                    CustomerPage.CustomerPage(customer, self.root)
                elif role == 'M'
                    manager = Manager.Manager(username)
                    ManagerPage.ManagerPage(manager, self.root)
                else:
                    operator = Operator.Operator(username)
                    OperatorPage.OperatorPage(operator, self.root)
            else:
                self.wrongPassowrd()
    def register(self):
        RegisterPage.RegisterPage(self.root)


