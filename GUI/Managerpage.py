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
label1 = Label(text="Welcome manager!", font=l1_font)
label1.place(x=330, y=80)

# Sign Out Button
button1 = Button(text="Sign Out", font=b_font, bg='red', fg='white')
button1.place(x=900, y=150, width=90, height=40)

# Operator Buttons

button4 = Button(text="View pdf", font=b2_font, bg='orange', fg='white')
button4.place(x=180, y=350, width=260, height=50)
button5 = Button(text="Back", font=b2_font, bg='purple', fg='white')
button5.place(x=600, y=350, width=260, height=50)


window.mainloop()
