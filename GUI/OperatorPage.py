from tkinter import *
from tkinter import font

from app import app
from GUI import VehicleManagement,StationManagement, StationPropertyPage, RepairManagement, OperatorCenter


class OperatorPage():
    def __init__(self, app:app, master = None):
        self.__root = master
        self.__app = app
        self.CreatePage()

    def CreatePage(self):

        self.page = Frame(self.__root, width=1000, height=600)
        self.page.pack()


        # Define fonts
        l1_font = font.Font(family="Helvetica", size=32, weight='bold')
        b2_font = font.Font(family="Helvetica", size=16)
        b_font = font.Font(family="Helvetica", size=14)

        # Label for Operator
        label1 = Label(text="Operator", font=l1_font)
        label1.place(x=400, y=80)

        # Sign Out Button
        button1 = Button(text="Sign Out", font=b_font, bg='red', fg='white')
        button1.place(x=900, y=150, width=90, height=40)

        # Operator Buttons
        button2 = Button(text="Vehicle Management", command = self.vehicle_management, font=b2_font, bg='blue', fg='white')
        button2.place(x=200, y=250, width=260, height=50)
        button3 = Button(text="Stop Management", command = self.move, font=b2_font, bg='green', fg='white')
        button3.place(x=620, y=250, width=260, height=50)
        button4 = Button(text="Stop Property Management", command=self.property, font=b2_font, bg='orange', fg='white')
        button4.place(x=200, y=350, width=260, height=50)
        button5 = Button(text="Repair Management", command = self.repair, font=b2_font, bg='purple', fg='white')
        button5.place(x=620, y=350, width=260, height=50)
        button6 = Button(text="Operator Center", command = self.center, font=b2_font, bg='red', fg='white')
        button6.place(x=200, y=450, width=260, height=50)

    def vehicle_management(self):
        VehicleManagement.VehicleManagementPage(self.__app,self.__root).CreatePage()

    def move(self):
        StationManagement.StationManagementPage(self.__app,self.__root).CreatePage()

    def property(self):
        StationPropertyPage.StationPropertyPage(self.__app,self.__root).CreatePage()

    def repair(self):
        RepairManagement.RepairManagementPage(self.__app,self.__root).CreatePage()

    def center(self):
        OperatorCenter.OperatorCenterPage(self.__app,self.__root).CreatePage()








