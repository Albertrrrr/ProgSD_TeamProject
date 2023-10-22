from tkinter import *
from tkinter import font

window = Tk()
window.geometry("1000x600")
window.title("Bike-sharing System")

# Define fonts
l1_font = font.Font(family="Helvetica", size=36, weight='bold')
l2_font = font.Font(family="Helvetica", size=16)
b_font = font.Font(family="Helvetica", size=14)

# Label 1
label1 = Label(text="Top-up Balance", font=l1_font)
label1.place(x=350, y=50)

# Labels for Current Balance, Card Holder Name, Card Number, Expiration Date, and Top-up Amount
label2 = Label(text="Current Balance:", font=l2_font)
label2.place(x=320, y=200)
label3 = Label(text="Card Holder:", font=l2_font)
label3.place(x=358, y=260)
label4 = Label(text="Card Number:", font=l2_font)
label4.place(x=348, y=320)
label5 = Label(text="Expiration Date:", font=l2_font)
label5.place(x=325, y=380)
label6 = Label(text="Top-up Amount:", font=l2_font)
label6.place(x=328, y=460)

# Entry Widgets
textbox1 = Entry(font=l2_font)
textbox1.place(x=480, y=260, width=350, height=30)
textbox2 = Entry(font=l2_font)
textbox2.place(x=480, y=320, width=350, height=30)
textbox3 = Entry(font=l2_font)
textbox3.place(x=480, y=380, width=200, height=30)
textbox4 = Entry(font=l2_font)
textbox4.place(x=480, y=460, width=350, height=30)

# Buttons
button1 = Button(text="Go Back", font=b_font, bg='red', fg='white')
button1.place(x=300, y=525, width=100, height=40)
button2 = Button(text="Top-up", font=b_font, bg='green', fg='white')
button2.place(x=600, y=525, width=100, height=40)

window.mainloop()
