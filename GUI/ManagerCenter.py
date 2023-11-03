from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import ttk, scrolledtext
from app import app
from tkmacosx import Button

class ManagerCenterPage():
    def __init__(self, app: app, master=None):
        self.__info_list = None
        self.__root = master
        self.__password = StringVar()
        self.__email = StringVar()
        self.__username = StringVar()
        self.__app = app

    def CreatePage(self):
        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("1000x600")

        title_label = Label(self.page, text="Manager Center", bg="#add8e6", font=("Arial", 30, "bold"))
        title_label.pack(pady=20)

        # Back button
        back_button = Button(self.page,command=self.quit, text="Back", bg="#4CAF50", fg="white", font=("Arial", 14))
        back_button.place(x=30, y=30)

        # Change password
        password_lbl = Label(self.page, text="Change password", bg="#add8e6", font=("Arial", 16))
        password_lbl.place(x=300, y=160)
        self.__password = Entry(self.page, width=25)
        self.__password.place(x=480, y=163)
        password_btn = Button(self.page, command = self.changePassword, text="OK", bg="#4CAF50", fg="white", font=("Arial", 12))
        password_btn.place(x=670, y=160)

        # Modify email
        email_lbl = Label(self.page, text="Modify email", bg="#add8e6", font=("Arial", 16))
        email_lbl.place(x=350, y=250)
        self.__email = Entry(self.page, width=25)
        self.__email.place(x=480, y=253)
        email_btn = Button(self.page, text="OK", command=self.changeEmail,bg="#4CAF50", fg="white", font=("Arial", 12))
        email_btn.place(x=670, y=250)

        # Change name
        name_lbl = Label(self.page, text="Change name", bg="#add8e6", font=("Arial", 16))
        name_lbl.place(x=340, y=340)
        self.__username = Entry(self.page, width=25)
        self.__username.place(x=480, y=343)
        name_btn = Button(self.page, command=self.changeName, text="OK", bg="#4CAF50", fg="white", font=("Arial", 12))
        name_btn.place(x=670, y=340)

    def quit(self):
        self.page.destroy()

    def changePassword(self):
        p = self.__password.get()
        flag = self.__app.updatePasswordOM(str(p))
        if flag:
            msgbox.showinfo("Success", "Successfully Change!", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Please Check!", parent=self.page)

    def changeEmail(self):
        e = self.__email.get()
        flag = self.__app.updateEmailOM(str(e))
        if flag:
            msgbox.showinfo("Success", "Successfully Change!", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Please Check!", parent=self.page)

    def changeName(self):
        n = self.__username.get()
        flag = self.__app.updateNameOM(str(n))
        if flag:
            msgbox.showinfo("Success", "Successfully Change!", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Please Check!!", parent=self.page)
