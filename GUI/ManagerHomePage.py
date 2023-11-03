from tkinter import *
from tkinter import font
from tkmacosx import Button
from app import app
from GUI import ViewCustomer,ViewOperator,ViewVehicle,ViewWorkOrder,ManagerCenter


class ManagerHomePage():

    def __init__(self, app: app, master=None):
        self.__root = master
        self.__app = app
        self.__label2 = None
        self.__scale = None

    def CreatePage(self):

        self.page = Frame(self.__root, width=1000, height=600)
        self.page.pack()

        l1_font = font.Font(family="Helvetica", size=32, weight='bold')
        b2_font = font.Font(family="Helvetica", size=16)
        b_font = font.Font(family="Helvetica", size=14)


        label1 = Label(text="Welcome Manager!", font=l1_font)
        label1.place(x=350, y=80)
        self.__label2 = Label(text="Please wait a few seconds \nwhen you click 'View PDF'",font = b_font)
        self.__label2.place(x = 200, y =190)

        # Sign Out Button
        button1 = Button(text="Sign Out", font=b_font, bg='red', fg='white')
        button1.place(x=900, y=150, width=90, height=40)

        # Operator Buttons
        button2 = Button(text="View PDF", command = self.pdf, font=b2_font, bg='blue', fg='white')
        button2.place(x=200, y=250, width=260, height=50)
        button3 = Button(text="View customers", command=self.customer, font=b2_font, bg='green', fg='white')
        button3.place(x=620, y=250, width=260, height=50)
        button4 = Button(text="View operators", font=b2_font, command = self.operator, bg='orange', fg='white')
        button4.place(x=200, y=350, width=260, height=50)
        button5 = Button(text="View vehicles", font=b2_font, command = self.vehicle, bg='purple', fg='white')
        button5.place(x=620, y=350, width=260, height=50)
        button6 = Button(text="View Work Order", command = self.order, font=b2_font, bg='red', fg='white')
        button6.place(x=200, y=450, width=260, height=50)
        button7 = Button(text="Manager Center", command = self.managerCenter, font=b2_font, bg='green', fg='white')
        button7.place(x=620, y=450, width=260, height=50)

    def pdf(self):
        self.__app.managerViewPdf()

    def customer(self):
        ViewCustomer.ViewCustomerPage(self.__app,self.__root).CreatePage()

    def operator(self):
        ViewOperator.ViewOperatorPage(self.__app,self.__root).CreatePage()

    def vehicle(self):
        ViewVehicle.ViewVehiclePage(self.__app,self.__root).CreatePage()

    def order(self):
        ViewWorkOrder.ViewWorkOrderPage(self.__app,self.__root).CreatePage()

    def managerCenter(self):
        ManagerCenter.ManagerCenterPage(self.__app,self.__root).CreatePage()

