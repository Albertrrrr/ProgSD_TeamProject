from tkinter import *
from tkinter import font

window = Tk()
window.geometry("1000x600")
window.title("Bike-sharing system")

# Define fonts
l1_font = font.Font(family="Helvetica", size=32, weight='bold')
l2_font = font.Font(family="Helvetica", size=20)
b_font = font.Font(family="Helvetica", size=16)

# Label 1 - Welcome Customer
label1 = Label(text="Welcome Customer!", font=l1_font, fg="black")
label1.place(x=300, y=50)

# Label 2 - What do you want?
label2 = Label(text="What do you want?", font=l2_font)
label2.place(x=100, y=150)

# Sign Out Button
button1 = Button(text="Sign Out", font=b_font, bg='red', fg='white')
button1.place(x=880, y=150, width=100, height=40)

# Rent Vehicle Button
button2 = Button(text="Rent Vehicle", font=b_font, bg='green', fg='white')
button2.place(x=400, y=250, width=200, height=80)

# Top-up Balance Button
button3 = Button(text="Top-up Balance", font=b_font, bg='blue', fg='white')
button3.place(x=400, y=400, width=200, height=80)

window.mainloop()
