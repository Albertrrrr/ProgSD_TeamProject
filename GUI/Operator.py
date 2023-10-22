from tkinter import *
from tkinter import font

window = Tk()
window.geometry("1000x600")
window.title("Bike-sharing System")

# Define fonts
l1_font = font.Font(family="Helvetica", size=32, weight='bold')
b2_font = font.Font(family="Helvetica", size=16)
b_font = font.Font(family="Helvetica", size=14)

# Label for Operator
label1 = Label(text="Operator", font=l1_font)
label1.place(x=400, y=80)

# Sign Out Button
button1 = Button(text="Sign Out", font=b_font, bg='red', fg='white')
button1.place(x=900, y=150, width=90, height=40)

# Operator Buttons
button2 = Button(text="Track Vehicle", font=b2_font, bg='blue', fg='white')
button2.place(x=200, y=250, width=260, height=50)
button3 = Button(text="Move Vehicle", font=b2_font, bg='green', fg='white')
button3.place(x=620, y=250, width=260, height=50)
button4 = Button(text="Charge Vehicle", font=b2_font, bg='orange', fg='white')
button4.place(x=200, y=350, width=260, height=50)
button5 = Button(text="Add New Vehicle", font=b2_font, bg='purple', fg='white')
button5.place(x=620, y=350, width=260, height=50)
button6 = Button(text="Repair All", font=b2_font, bg='red', fg='white')
button6.place(x=200, y=450, width=260, height=50)

window.mainloop()
