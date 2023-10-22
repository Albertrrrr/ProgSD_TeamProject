from tkinter import *
from GUI import LoginPage

def main():
    root = Tk()
    root.title("Vehicle Sharing System")
    LoginPage.LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
