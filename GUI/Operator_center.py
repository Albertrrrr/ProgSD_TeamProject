from tkinter import *
from tkinter import font
from app import app

class OperatorPage():
    def __init__(self, app:app, master = None):
        self.__root = master
        self.__app = app
        self.CreatePage()

    def CreatePage(self):
        # Create main window
        self.page = Frame(self.__root, width=1000, height=600)
        self.page.pack()

        # User center label
        Label(text="Operator center", bg="#4A90E2", fg="white", font=("Arial", 24)).place(x=30, y=30,
                                                                                                   width=250,
                                                                                                   height=60)

        # Back button
        Button(text="Back", bg="#2ECC71", fg="white", font=("Arial", 18)).place(x=70, y=130, width=120,
                                                                                         height=50)  # Green button

        # Functions to create sections
        def create_section(y_position, title):
            Label(text=title, bg="#4A90E2", fg="white", font=("Arial", 18)).place(x=250, y=y_position)
            Entry(font=("Arial", 16)).place(x=250, y=y_position + 50, width=350, height=40)
            Button(text="OK", bg="#2ECC71", fg="white", font=("Arial", 16)).place(x=610, y=y_position + 50,
                                                                                           width=80, height=40)
        # Change password section
        create_section(150, "Change password")

        # Modify email section
        create_section(260, "Modify email")

        # Change name section
        create_section(370, "Change name")



