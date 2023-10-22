from tkinter import *
from tkinter import font
from tkinter import ttk

window = Tk()
window.geometry("1000x600")
window.title("Bike-sharing System")

# Define fonts
l1_font = font.Font(family="Helvetica", size=36, weight='bold')
l2_font = font.Font(family="Helvetica", size=16)
b_font = font.Font(family="Helvetica", size=14)

# Label 1
label1 = Label(text="Track Vehicle", font=l1_font)
label1.place(x=350, y=50)

# Labels for Vehicle ID and City Location
label2 = Label(text="Vehicle ID", font=l2_font)
label2.place(x=150, y=200)
label3 = Label(text="City Location", font=l2_font)
label3.place(x=150, y=250)

# Comboboxes
options = ["Option 1", "Option 2", "Option 3", "Option 4"]
# combo_var1 = StringVar(value=options[0])
# combobox1 = ttk.Combobox(textvariable=combo_var1, values=options)
# combobox1.place(x=300, y=200)
combo_var2 = StringVar(value=options[0])
combobox2 = ttk.Combobox(textvariable=combo_var2, values=options)
combobox2.place(x=300, y=250)

# Track and Back Buttons
button1 = Button(text="Track", font=b_font, bg='green', fg='white')
button1.place(x=700, y=190, width=100, height=40)
button2 = Button(text="Back", font=b_font, bg='red', fg='white')
button2.place(x=700, y=250, width=100, height=40)

# Text Box
text_box = Text(window, wrap=WORD, height=10, width=40, font=l2_font)
text_box.place(x=300, y=350, height=200, width=400)
textbox3 = Entry(font=l2_font)
textbox3.place(x=300, y=200, width=162, height=23)

window.mainloop()
