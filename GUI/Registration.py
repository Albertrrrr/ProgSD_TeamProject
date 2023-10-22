from tkinter import *
import tkinter as tk
from tkinter import font

class RegisterPage(object):
    def __init__(self, master=None):

        self.root = master
        self.CreatePage()

    def CreatePage(self):

        self.page = Frame(self.root, width = 1000, height = 600)
        self.page.pack()

        # Define fonts
        l1_font = font.Font(family="Helvetica", size=32, weight='bold')
        l2_font = font.Font(family="Helvetica", size=14)
        c_font = font.Font(family="Helvetica", size=14)
        b_font = font.Font(family="Helvetica", size=14)

        # Label 1
        label1 = Label(self.page, text="Welcome Customer!", font=l1_font)
        label1.place(x=300, y=40)

        # Labels for Username, Password, and Repeat Password
        label2 = Label(self.page, text="Username:", font=l2_font)
        label2.place(x=280, y=120)
        label3 = Label(self.page, text="Password:", font=l2_font)
        label3.place(x=280, y=190)
        label4 = Label(self.page,text="Repeat Password:", font=l2_font)
        label4.place(x=213, y=270)
        label5 = Label(self.page, text="Email:", font=l2_font)
        label5.place(x=305, y=330)
        label6 = Label(self.page, text="CAPTCHA:", font=l2_font)
        label6.place(x=270, y=400)

        # Entry Widgets
        textbox1 = Entry(font=l2_font)
        textbox1.place(x=380, y=120, width=350, height=30)
        textbox2 = Entry(font=l2_font, show="*")  # Show asterisks for password
        textbox2.place(x=380, y=190, width=350, height=30)
        textbox3 = Entry(font=l2_font, show="*")
        textbox3.place(x=380, y=270, width=350, height=30)
        textbox4 = Entry(font=l2_font)
        textbox4.place(x=380, y=330, width=350, height=30)
        textbox5 = Entry(font=l2_font)
        textbox5.place(x=380, y=400, width=350, height=30)

        # Checkbuttons for User Type
        check_var1 = IntVar()
        check1 = Checkbutton(text="Customer", font=c_font, variable=check_var1)
        check1.place(x=250, y=470)
        check_var2 = IntVar()
        check2 = Checkbutton(text="Operator", font=c_font, variable=check_var2)
        check2.place(x=450, y=470)
        check_var3 = IntVar()
        check3 = Checkbutton(text="Manager", font=c_font, variable=check_var3)
        check3.place(x=650, y=470)

        # Buttons
        button1 = Button(text="Go Back", font=b_font, bg='red', fg='white')
        button1.place(x=300, y=530, width=100, height=40)
        button2 = Button(text="Register", font=b_font, bg='green', fg='white')
        button2.place(x=600, y=530, width=100, height=40)
        button2 = Button(text="Get verification_code", font=b_font)
        button2.place(x=760, y=400, width=200, height=30)

