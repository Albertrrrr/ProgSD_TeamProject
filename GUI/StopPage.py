from tkinter import *
# import tkinter.messagebox as msgbox
from tkinter import ttk, scrolledtext

from GUI import RentReturn
from app import app

class StopPage():
    def __init__(self, app: app, master=None):
        self.__info_list = None
        self.__info_text = None
        self.__entry = StringVar()
        self.__root = master
        self.__app = app

    def CreatePage(self):
        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("800x600")

        title_label = Label(self.page, text="🔍 View stops", bg="lightcyan", font=("Arial", 18, "bold"), padx=10,
                               pady=10)
        title_label.place(x=10, y=10)

        title_label = Label(self.page, text="Input stop ID:",  font=("Arial", 12))
        title_label.place(x=500, y=20)

        self.__entry = Entry(self.page, width=10)
        self.__entry.place(x=600, y=21)

        # Replace Back button with Enter button
        enter_btn = Button(self.page, command = self.rentReturn, text="Enter", bg='#4CAF50', fg='white', font=("Arial", 12), padx=10, pady=10)
        enter_btn.place(x=400, y=10)

        b2 = Button(self.page, command = self.refresh, text = "Refresh",bg='#4CAF50', fg='white', font=("Arial", 12), padx=10, pady=10)
        b2.place(x=300, y=10)

        b3 = Button(self.page, command=self.quit, text="back", bg='#000000', fg='white', font=("Arial", 12),
                    padx=10, pady=10)
        b3.place(x=220, y=10)

        self.__info_text = scrolledtext.ScrolledText(self.page, width = 100, height = 30)
        self.__info_text.place(x=25, y=120)

    def rentReturn(self):
        stopID = self.__entry.get()
        self.__app.stopID = stopID
        RentReturn.RentReturnPage(self.__app,self.__root).CreatePage()


    def refresh(self):
        res = self.__app.getAllStopsCU()
        for i in res:
            self.__info_text.insert(END, i + "\n")

    def quit(self):
        self.page.destroy()