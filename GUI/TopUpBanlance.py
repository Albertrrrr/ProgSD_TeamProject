from tkinter import *
from tkinter import font

window = Tk()
window.geometry("1300x800")
window.title("Bike-sharing system")
l1_font = font.Font(family = "Times New Roman", size = 24)
label1 = Label(text = "Top-up Banlance", font = l1_font)
label1.place(x = 500, y = 100)

l2_font = font.Font(family = "Times New Roman", size = 14)
label2 = Label(text = "Current balance:", font = l2_font)
label2.place(x = 330, y = 200)
label3 = Label(text = "Card holder name:", font = l2_font)
label3.place(x = 315, y = 260)
label4 = Label(text = "Card number:", font = l2_font)
label4.place(x = 350, y = 320)
label5 = Label(text = "Expiration date:", font = l2_font)
label5.place(x = 336, y = 380)
label6 = Label(text = "Top-up amount:", font = l2_font)
label6.place(x = 330, y = 460)
textbox1 = Entry(text = "")
textbox1.place(x = 480, y = 260, width = 350, height = 25)
textbox2 = Entry(text = "")
textbox2.place(x = 480, y = 320, width = 350, height = 25)
textbox3 = Entry(text = "")
textbox3.place(x = 480, y = 380, width = 200, height = 25)
textbox4 = Entry(text = "")
textbox4.place(x = 480, y = 460, width = 350, height = 25)


b_font = font.Font(family = "Times New Roman", size = 13)
button1 = Button(text = "GoBack", font = b_font)
button1.place(x = 400, y = 650, width = 100, height = 40)
button2 = Button(text = "Top-up", font = b_font)
button2.place(x = 700, y = 650, width = 100, height = 40)


window.mainloop()