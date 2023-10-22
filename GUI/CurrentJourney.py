from tkinter import *
from tkinter import font

window = Tk()
window.geometry("1000x600")
window.title("Bike-sharing System")

# Define fonts
l1_font = font.Font(family="Helvetica", size=32, weight='bold')
l2_font = font.Font(family="Helvetica", size=14)
l3_font = font.Font(family="Helvetica", size=18)
b_font = font.Font(family="Helvetica", size=14)

# Label 1 - Current Journey
label1 = Label(text="Current Journey", font=l1_font)
label1.place(x=320, y=50)

# Labels for Rent Location, Rent Time, and Total Cost
label2 = Label(text="Return Location", font=l3_font)
label2.place(x=100, y=200)
label3 = Label(text="Rent Time (min):", font=l2_font)
label3.place(x=597, y=270)
label4 = Label(text="Total Cost (£):", font=l2_font)
label4.place(x=618, y=350)
label5 = Label(text="Your rented vehicle ID:", font=l2_font)
label5.place(x=350, y=130)
label6 = Label(text="Journey details", font=l3_font)
label6.place(x=570, y=200)

# Label 5 - "Min:"
# label5 = Label(text="Min:", font=l2_font)
# label5.place(x=850, y=400)

# Entry for Rent Time
textbox1 = Entry(font=l2_font)
textbox1.place(x=760, y=270, width=130, height=30)

textbox2 = Entry(font=l2_font)
textbox2.place(x=760, y=350, width=130, height=30)

textbox3 = Entry(font=l2_font)
textbox3.place(x=100, y=250, width=350, height=200)

textbox3 = Entry(font=l2_font)
textbox3.place(x=550, y=130, width=30, height=30)

# Entry for Vehicle ID


# Scrollbar for Journey Details


# Text for Journey Details





# Button - Return Vehicle
button1 = Button(text="Return Vehicle", font=b_font, bg='red', fg='white')
button1.place(x=420, y=500, width=160, height=40)

window.mainloop()
