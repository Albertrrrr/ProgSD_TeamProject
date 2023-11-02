from tkinter import *
from tkinter import font
from app import app
import tkinter.messagebox as msgbox
from pathlib import Path
from PIL import Image,ImageTk


class TopUpBanlancePage():

    def __init__(self, app: app, master=None):
        current_file_path = Path(__file__).resolve()
        self.__dir = str(current_file_path.parent.parent) + "\\"
        self.__url = None
        self.__root = master
        self.__app = app
        self.__amount = StringVar()
        self.__finalURL = None
        self.__img = None
        self.__image_label = None

    def CreatePage(self):

        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("1000x600")

        l1_font = font.Font(family="Helvetica", size=36, weight='bold')
        l2_font = font.Font(family="Helvetica", size=16)
        b_font = font.Font(family="Helvetica", size=14)

        # Label 1
        label1 = Label(self.page, text="Top-up Balance", font=l1_font)
        label1.place(x=350, y=50)

        # Labels for Current Balance, Card Holder Name, Card Number, Expiration Date, and Top-up Amount
        label2 = Label(self.page, text="Recharge amount:", font=l2_font)
        label2.place(x=120, y=200)
        label3 = Label(self.page, text="QR code:", font=l2_font)
        label3.place(x=600, y=200)

        self.__amount = Entry(self.page, font=l2_font)
        self.__amount.place(x=300, y=200, width=68, height=30)

        # Buttons
        button1 = Button(self.page, command=self.quit, text="Go Back", font=b_font, bg='red', fg='white')
        button1.place(x=150, y=325, width=100, height=40)
        button2 = Button(self.page, command=self.top_up, text="Generate", font=b_font, bg='green', fg='white')
        button2.place(x=400, y=190, width=100, height=40)

        button3 = Button(self.page, command=self.refresh, text="Refresh", font=b_font)
        button3.place(x=700, y=200, width=100, height=40)

        button4 = Button(self.page, command=self.true, text="Top-up", font=b_font)
        button4.place(x=300, y=325, width=100, height=40)



    def quit(self):
        self.page.destroy()

    def refresh(self):
        image = Image.open(self.__finalURL)

        self.__img = ImageTk.PhotoImage(image)

        self.__image_label = Label(self.page, image=self.__img)

        self.__image_label.place(x=590, y=280)
        self.__image_label.config(x=590,y=280)
        self.__image_label.pack()

    def true(self):
        paidFlag = self.__app.topUp()

        if paidFlag:
            msgbox.showinfo("Success", "Successfully top up", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Try again!", parent=self.page)

    def top_up(self):
        amount = self.__amount.get()
        flag = self.__app.generateQRcodeString(float(amount))
        self.__url = self.__app.QRcodeURL

        if flag:
            msgbox.showinfo("Success", "Successfully generate!", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Check again!", parent=self.page)

        self.__finalURL = self.__dir + self.__url
