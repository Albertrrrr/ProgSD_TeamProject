from tkinter import *
from tkinter import font

window = Tk()
window.geometry("1000x600")
window.title("Bike-sharing system")

# Define fonts
l1_font = font.Font(family="Helvetica", size=32, weight='bold')
l2_font = font.Font(family="Helvetica", size=16)
b_font = font.Font(family="Helvetica", size=16)

# Label 1 - Welcome Customer
label1 = Label(text="Charge Vehicle", font=l1_font, fg="black")
label1.place(x=300, y=50)

label2 = Label(text="Threshold(0-1)", font=l2_font)
label2.place(x=280, y=185)

textbox1 = Entry(font=l2_font)
textbox1.place(x=450, y=185, width=220, height=30)

label3 = Label(text="Note: battery less than or equal to threshold value will be charged", font = l2_font)
label3.place(x = 150, y = 300)

# Sign Out Button
button1 = Button(text="Charge", font=b_font, bg='red', fg='white')
button1.place(x=220, y = 440, width=120, height=40)

# Rent Vehicle Button
button2 = Button(text="Back", font=b_font, bg='green', fg='white')
button2.place(x=550, y = 440, width=120, height=40)


window.mainloop()
