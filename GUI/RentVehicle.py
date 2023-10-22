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
label1 = Label(text="Rent Vehicle", font=l1_font)
label1.place(x=370, y=50)

# Labels for Rent Location, Rent Time, and Total Cost
label2 = Label(text="Rent Location", font=l3_font)
label2.place(x=100, y=200)
label3 = Label(text="Vehicle type:", font=l2_font)
label3.place(x=642, y=270)
label4 = Label(text="Rent time (min):", font=l2_font)
label4.place(x=618, y=350)


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



# Entry for Vehicle ID


# Scrollbar for Journey Details


# Text for Journey Details





# Button - Return Vehicle
button1 = Button(text="Return Vehicle", font=b_font, bg='red', fg='white')
button1.place(x=420, y=500, width=160, height=40)

window.mainloop()
