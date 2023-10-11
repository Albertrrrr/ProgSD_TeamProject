from tkinter import *
from tkinter import font

window = Tk()
window.geometry("1300x800")
window.title("Bike-sharing system")
l1_font = font.Font(family = "Registration", size = 24)
label1 = Label(text = "Welcome customer!", font = l1_font)
label1.place(x = 500, y = 100)

l2_font = font.Font(family = "Times New Roman", size = 14)
label2 = Label(text = "Username:", font = l2_font)
label2.place(x = 380, y = 250)
l3_font = font.Font(family = "Times New Roman", size = 14)
label3 = Label(text = "Password:", font = l3_font)
label3.place(x = 380, y = 330)
l4_font = font.Font(family = "Times New Roman", size = 14)
label4 = Label(text = "Repeat Password:", font = l4_font)
label4.place(x = 325, y = 410)

textbox1 = Entry(text = "")
textbox1.place(x = 480, y = 250, width = 350, height = 25)
textbox2 = Entry(text = "")
textbox2.place(x = 480, y = 330, width = 350, height = 25)
textbox3 = Entry(text = "")
textbox3.place(x = 480, y = 410, width = 350, height = 25)

c_font = font.Font(family = "Times New Roman", size = 15)
check1 = Checkbutton(text=" Costumer", font = c_font)
check1.place(x = 400, y = 500)
check2 = Checkbutton(text=" Operator", font = c_font)
check2.place(x = 600, y = 500)
check3 = Checkbutton(text=" Manager", font = c_font)
check3.place(x = 800, y = 500)

b_font = font.Font(family = "Times New Roman", size = 13)
button1 = Button(text = "GoBack", font = b_font)
button1.place(x = 400, y = 650, width = 100, height = 40)
button2 = Button(text = "Register", font = b_font)
button2.place(x = 700, y = 650, width = 100, height = 40)


window.mainloop()