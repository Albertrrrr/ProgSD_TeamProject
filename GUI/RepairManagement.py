from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import ttk, scrolledtext
from app import app


class RepairManagementPage():
    def __init__(self, app: app, master=None):
        self.__info_list = None
        self.__root = master
        self.__repairID = StringVar()
        self.__overRepairBike = StringVar()
        self.__overRepairID = StringVar()
        self.__info_list = StringVar()
        self.__info_list_2 = StringVar()
        self.__app = app

    def CreatePage(self):

        self.page = Toplevel(self.__root)
        self.page.attributes('-topmost', 1)
        self.page.geometry("1000x600")

        top_bar = Label(self.page, bg="lightcyan", height=3, width=800)
        top_bar.place(x=0, y=0)

        # Top title
        title_label = Label(top_bar, text="🔍 Repair Management", bg="lightcyan", font=("Arial", 12, "bold"))
        title_label.place(x=10, y=5)

        # Buttons
        refresh_btn = Button(top_bar, command = self.refresh, text="Refresh", bg='#4CAF50', fg='white', font=("Arial", 10))
        refresh_btn.place(x=230, y=5)

        back_btn = Button(top_bar, command = self.quit, text="Back", bg='#4CAF50', fg='white', font=("Arial", 10))
        back_btn.place(x=320, y=5)

        # Huge display box (Text widget)
        self.__info_list = scrolledtext.ScrolledText(self.page, width=130, height=15)
        self.__info_list.place(x=50, y=80)

        # Start Fix
        del_lbl = Label(self.page, text="Start repair:", bg="#add8e6", font=("Arial", 12))
        del_lbl.place(x=50, y=320)
        del_entry_lbl = Label(self.page, text="bikeID", font=("Arial", 10))
        del_entry_lbl.place(x=50, y=360)
        self.__repairID = Entry(self.page, width=10)
        self.__repairID.place(x=90, y=360)
        del_enter_btn = Button(self.page, command = self.startRepair, text="Enter", bg='#4CAF50', fg='white', font=("Arial", 10))
        del_enter_btn.place(x=180, y=360)
        del_clear_btn = Button(self.page, command = self.clear_1,text="Clear", bg='#4CAF50', fg='white', font=("Arial", 10))
        del_clear_btn.place(x=250, y=360)

        # Move vehicle operation
        move_lbl = Label(self.page, text="Over repair:", bg="#add8e6", font=("Arial", 12))
        move_lbl.place(x=470, y=320)
        move_entry_lbl = Label(self.page, text="bikeID",  font=("Arial", 10))
        move_entry_lbl.place(x=462, y=360)
        self.__overRepairBike = Entry(self.page, width=10)
        self.__overRepairBike.place(x=515, y=360)
        move_entry_lbl = Label(self.page, text="reportID", font=("Arial", 10))
        move_entry_lbl.place(x=462, y=390)
        self.__overRepairID = Entry(self.page, width=10)
        self.__overRepairID.place(x=515, y=390)

        move_enter_btn = Button(self.page, command = self.overRepair, text="Enter", bg='#4CAF50', fg='white', font=("Arial", 10))
        move_enter_btn.place(x=600, y=360)
        move_clear_btn = Button(self.page, command=self.clear_2, text="Clear", bg='#4CAF50', fg='white', font=("Arial", 10))
        move_clear_btn.place(x=670, y=360)

        self.__info_list_2 = scrolledtext.ScrolledText(self.page, width=130, height=10)
        self.__info_list_2.place(x=50, y=430)

    def quit(self):
        self.page.destroy()

    def refresh(self):
        content = self.__info_list.get('1.0', END)
        if content.strip():
            self.__info_list.delete('1.0', END)
        list = self.__app.getALLReportOP()
        for i in list:
            self.__info_list.insert(END, i + "\n")

        content_2 = self.__info_list_2.get('1.0', END)
        if content_2.strip():
            self.__info_list_2.delete('1.0', END)
        res = self.__app.getAllVehicleOP()
        for i in res:
            self.__info_list_2.insert(END, i + "\n")

    def startRepair(self):
        id = self.__repairID.get()
        flag = self.__app.fixBikeOP(int(id))
        print(flag)
        if flag:
            msgbox.showinfo("Success", "Successfully change!", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Please Check!", parent=self.page)

    def overRepair(self):
        bike = self.__overRepairBike.get()
        id = self.__overRepairID.get()
        flag = self.__app.endFixBikeOP(int(bike),int(id))
        if flag:
            msgbox.showinfo("Success", "Successfully change!", parent=self.page)
        else:
            msgbox.showwarning("Warning", "Please Check!", parent=self.page)

    def clear_1(self):
        self.__repairID.delete(0,END)

    def clear_2(self):
        self.__overRepairID.delete(0,END)
        self.__overRepairBike.delete(0,END)