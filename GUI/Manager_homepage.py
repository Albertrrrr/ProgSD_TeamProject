from tkinter import *
from tkinter import font
from app import app
from tkmacosx import Button


class ManagerPage():
    def __init__(self, app:app, master=None):
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
        label1 = Label(text="Welcome manager!", font=l1_font)
        label1.place(x=350, y=80)

        # Operator Buttons
        button2 = Button(text="View PDF", font=b2_font, bg='blue', fg='white')
        button2.place(x=200, y=250, width=260, height=50)
        button3 = Button(text="View customers", font=b2_font, bg='green', fg='white')
        button3.place(x=620, y=250, width=260, height=50)
        button4 = Button(text="View operators", font=b2_font, bg='orange', fg='white')
        button4.place(x=200, y=350, width=260, height=50)
        button5 = Button(text="View vehicles", font=b2_font, bg='purple', fg='white')
        button5.place(x=620, y=350, width=260, height=50)
        button6 = Button(text="View stations", font=b2_font, bg='red', fg='white')
        button6.place(x=200, y=450, width=260, height=50)




