from tkinter import *
from tkinter import font

window = Tk()
window.geometry("1300x800")
window.title("Bike-sharing system")
l1_font = font.Font(family = "Times New Roman", size = 24)
label1 = Label(text = "Rent vehicle", font = l1_font)
label1.place(x = 560, y = 80)

l2_font = font.Font(family = "Times New Roman", size = 14)
label2 = Label(text = "Rent localtion", font = l2_font)
label2.place(x = 120, y = 280)
label3 = Label(text = "Rent time(min):", font = l2_font)
label3.place(x = 700, y = 380)
label4 = Label(text = "Total cost(£):", font = l2_font)
label4.place(x = 720, y = 480)

l3_font = font.Font(family = "Times New Roman", size = 18)
label6 = Label(text = "Journey details", font = l3_font)
label6.place(x = 680, y = 300)
label7 = Label(text = "Your rented vehicle(ID of vehicle):",font = l3_font)
label7.place(x = 350, y = 200)

textbox1 = Entry(text = "")
textbox1.place(x = 860, y = 380, width = 180, height = 25)
textbox2 = Entry(text = "")
textbox2.place(x = 720, y = 200, width = 80, height = 25)

label5 = Label(text="Min：",font = 15)
text = Text(height=1, width=10)
text.insert("1.0", "Min：")
text.place(x = 860, y = 480, width = 180,height = 25)

scrollbar = Scrollbar(window, orient=VERTICAL, command=text.yview)
scrollbar.place(x=120, y=420, height=80)
text.config(yscrollcommand=scrollbar.set)

b_font = font.Font(family = "Times New Roman", size = 13)
button1 = Button(text = "Return Vehicle", font = b_font)
button1.place(x = 550, y = 650, width = 180, height = 40)


window.mainloop()