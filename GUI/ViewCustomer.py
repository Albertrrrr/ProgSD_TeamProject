from tkinter import *
from tkinter import scrolledtext
from app import app
from tkmacosx import Button


class ViewCustomerPage():
    def __init__(self, app: app, master=None):
        self.__root = master
        self.__app = app

    def CreatePage(self):

        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("700x600")

        title_label = Label(self.page, text="🔍 View all customers", bg="lightcyan", font=("Arial", 14, "bold"),
                               padx=10,
                               pady=10)
        title_label.place(x=10, y=10)

        # Buttons

        refresh_btn = Button(self.page, command = self.refresh, text="Refresh", bg='#4CAF50', fg='white', font=("Arial", 12), padx=10, pady=10)
        refresh_btn.place(x=260, y=10)

        back_btn = Button(self.page, text="Back", command=self.quit, bg='#4CAF50', fg='white', font=("Arial", 12), padx=10, pady=10)
        back_btn.place(x=400, y=10)

        self.__info_list = scrolledtext.ScrolledText(self.page, width=90, height=26)
        self.__info_list.place(x=25, y=120)

        list = self.__app.getALLCustomerOM()
        for i in list:
            self.__info_list.insert(END, i + "\n")

    def quit(self):
        self.page.destroy()

    def refresh(self):
        content = self.__info_list.get('1.0', END)
        if content.strip():
            self.__info_list.delete('1.0', END)
        list = self.__app.getALLCustomerOM()
        for i in list:
            self.__info_list.insert(END, i + "\n")
