from tkinter import *
from tkinter import font

window = Tk()
window.geometry("1300x800")
window.title("Bike-sharing system")
l1_font = font.Font(family = "Times New Roman", size = 24)
label1 = Label(text = "Operator", font = l1_font)
label1.place(x = 500, y = 100)

button1 = Button(text = "Sign out")
button1.place(x = 1050, y = 150, width = 90, height = 40)

b2_font = font.Font(family = "Times New Roman", size = 16)
button2 = Button(text = "Track vehicle", font = b2_font)
button2.place(x = 200, y = 300, width = 260, height = 50)
button3 = Button(text = "Move vehicle", font = b2_font)
button3.place(x = 620, y = 300, width = 260, height = 50)
button4 = Button(text = "Charge vehicle", font = b2_font)
button4.place(x = 200, y = 430, width = 260, height = 50)
button5 = Button(text = "Add new vehicle", font = b2_font)
button5.place(x = 620, y = 430, width = 260, height = 50)
button6 = Button(text = "Repair all", font = b2_font)
button6.place(x = 200, y = 560, width = 260, height = 50)

window.mainloop()