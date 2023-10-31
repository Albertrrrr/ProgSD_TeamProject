from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import font
from app import app

class UserCenterPage():
    def __init__(self, app:app, master=None):
        self.__newpassword = StringVar()
        self.__newemail = StringVar()
        self.__newusername = StringVar()
        self.__root = master
        self.__app = app

    def CreatePage(self):

        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("1000x600")

        title_label = Label(self.page, text="User center", bg="#add8e6", font=("Arial", 30, "bold"))
        title_label.pack(pady=20)

        # Back button
        back_button = Button(self.page, text="Back", command = self.quit, bg="#000000", fg="white", font=("Arial", 14))
        back_button.place(x=30, y=30)

        # Change password
        password_lbl = Label(self.page, text="Change password", bg="#add8e6", font=("Arial", 16))
        password_lbl.place(x=300, y=160)
        self.__newpassword = Entry(self.page, width=25)
        self.__newpassword.place(x=480, y=163)
        password_btn = Button(self.page, text="OK", command = self.changepassword, bg="#4CAF50", fg="white", font=("Arial", 12))
        password_btn.place(x=670, y=160)

        # Modify email
        email_lbl = Label(self.page, text="Modify email", bg="#add8e6", font=("Arial", 16))
        email_lbl.place(x=300, y=250)
        self.__newemail = Entry(self.page, width=25)
        self.__newemail.place(x=480, y=253)
        email_btn = Button(self.page, text="OK", command = self.changeemail, bg="#4CAF50", fg="white", font=("Arial", 12))
        email_btn.place(x=670, y=250)

        # Change name
        name_lbl = Label(self.page, text="Change name", bg="#add8e6", font=("Arial", 16))
        name_lbl.place(x=300, y=340)
        self.__newusername = Entry(self.page, width=25)
        self.__newusername.place(x=480, y=343)
        name_btn = Button(self.page, text="OK", command = self.changename, bg="#4CAF50", fg="white", font=("Arial", 12))
        name_btn.place(x=670, y=340)

    def quit(self):
        self.page.destroy()

    def changepassword(self):
        password = self.__newpassword.get()
        print(password)
        flag = self.__app.updateCustomerPassword(password)
        if flag:
            msgbox.showinfo("Success","Successfully Change!",parent= self.page)
        else:
            msgbox.showwarning("Warning","Check your new password!",parent= self.page)
    def changeemail(self):
        email = self.__newemail.get()
        flag = self.__app.updateCustomerEmail(email)
        if flag:
            msgbox.showinfo("Success", "Successfully Change!",parent= self.page)
        else:
            msgbox.showwarning("Warning", "Check your new email!",parent= self.page)

    def changename(self):
        username = self.__newusername.get()
        flag = self.__app.updateCustomerName(username)
        if flag:
            msgbox.showinfo("Success", "Successfully Change!",parent= self.page)
        else:
            msgbox.showwarning("Warning", "Check your new username!",parent= self.page)