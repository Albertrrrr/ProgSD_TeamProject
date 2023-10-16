from tkinter import *
from tkinter import font

window = Tk()
window.geometry("1300x800")
window.title("Bike-sharing system")
l1_font = font.Font(family = "Times New Roman", size = 24)
label1 = Label(text = "Welcome customer!", font = l1_font)
label1.place(x = 500, y = 100)

l2_font = font.Font(family = "Times New Roman", size = 14)
label2 = Label(text = "What do you want?", font = l2_font)
label2.place(x = 100, y = 250)

button1 = Button(text = "Sign out")
button1.place(x = 1050, y = 150, width = 90, height = 40)
b2_font = font.Font(family = "Times New Roman", size = 16)
button2 = Button(text = "Rent Vehicle", font = b2_font)
button2.place(x = 520, y = 320, width = 200, height = 100)
b3_font = font.Font(family = "Times New Roman", size = 16)
button3 = Button(text = "Top-up Banlance", font = b3_font)
button3.place(x = 520, y = 550, width = 200, height = 100)

window.mainloop()