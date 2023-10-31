from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import ttk, scrolledtext
from app import app

class StopPage():
    def __init__(self, app: app, master=None):
        self.__info_list = None
        self.__root = master
        self.__app = app

    def CreatePage(self):
        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("1000x600")

        title_label = Label(self.page, text="🔍 View stops", bg="lightcyan", font=("Arial", 14, "bold"), padx=10,
                               pady=10)
        title_label.place(x=10, y=10)

        # Replace Refresh button with an Entry
        self.__info_text = scrolledtext.ScrolledText(self.page, width=120, height=30)
        self.__info_text.place(x=260, y=10)

        # Replace Back button with Enter button
        enter_btn = Button(self.page, text="Enter", bg='#4CAF50', fg='white', font=("Arial", 12), padx=10, pady=10)
        enter_btn.place(x=400, y=10)

        # Text field
        text_field = Text(self.page, height=26, width=83, relief="solid", borderwidth=1)
        text_field.place(x=25, y=120)