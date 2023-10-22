from tkinter import *
# import tkinter.messagebox as msgbox
from tkinter import font
from . import Registration
from . import MapPage


class LoginPage(object):
    def __init__(self, master = None):
        self.root = master
        self.root.geometry("1000x600")
        self.CreatePage()

    def CreatePage(self):

        #self.page = Frame(self.root)
        #self.page.pack()

        # Define fonts
        l1_font = font.Font(family="Helvetica", size=32, weight='bold')
        l2_font = font.Font(family="Helvetica", size=14)
        c_font = font.Font(family="Helvetica", size=14)
        b_font = font.Font(family="Helvetica", size=14)

        # Label 1
        label1 = Label(text="Bike-sharing", font=l1_font)
        label1.place(x=320, y=50)

        check_var1 = IntVar()
        check1 = Checkbutton(text="Customer", font=c_font, variable=check_var1)
        check1.place(x=250, y=160)
        check_var2 = IntVar()
        check2 = Checkbutton(text="Operator", font=c_font, variable=check_var2)
        check2.place(x=450, y=160)
        check_var3 = IntVar()
        check3 = Checkbutton(text="Manager", font=c_font, variable=check_var3)
        check3.place(x=650, y=160)

        # Labels for Username, Password, and Repeat Password
        label2 = Label(text="Username:", font=l2_font)
        label2.place(x=280, y=250)
        label3 = Label(text="Password:", font=l2_font)
        label3.place(x=280, y=330)

        # Entry Widgets
        textbox1 = Entry(font=l2_font)
        textbox1.place(x=380, y=250, width=300, height=30)
        textbox2 = Entry(font=l2_font, show="*")  # Show asterisks for password
        textbox2.place(x=380, y=330, width=300, height=30)


        # Buttons
        button1 = Button(text="Login", font=b_font)
        button1.place(x=380, y=420, width=100, height=40)
        button2 = Button(text="Register", command = self.register, font=b_font)
        button2.place(x=380, y=500, width=100, height=40)
        button3 = Button(text="Map", command = self.map, font = b_font)
        button3.place(x = 600, y = 500)
    def register(self):
        Registration.RegisterPage(self.root)

    def map(self):
        MapPage.MapPage(self.root)


