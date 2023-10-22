from tkinter import *
from tkinter import font
from tkinter import ttk

window = Tk()
window.geometry("1000x600")
window.title("Bike-sharing system")

# Define fonts
l1_font = font.Font(family="Helvetica", size=32, weight='bold')
l2_font = font.Font(family="Helvetica", size=16)
b_font = font.Font(family="Helvetica", size=16)

# Label 1 - Welcome Customer
label1 = Label(text="Move Vehicle", font=l1_font, fg="black")
label1.place(x=350, y=50)

label2 = Label(text="Vehicle ID", font=l2_font)
label2.place(x=220, y=185)
label3 = Label(text="City Location", font=l2_font)
label3.place(x=220, y=285)

options = ["Option 1", "Option 2", "Option 3", "Option 4"]
combo_var1 = StringVar(value=options[0])
combobox1 = ttk.Combobox(textvariable=combo_var1, values=options)
combobox1.place(x=430, y=185,width=200,height=30)
combo_var2 = StringVar(value=options[0])
combobox2 = ttk.Combobox(textvariable=combo_var2, values=options)
combobox2.place(x=430, y=285,width=200,height=30)

# Sign Out Button
button1 = Button(text="Charge", font=b_font, bg='red', fg='white')
button1.place(x=220, y = 440, width=120, height=40)

# Rent Vehicle Button
button2 = Button(text="Back", font=b_font, bg='green', fg='white')
button2.place(x=550, y = 440, width=120, height=40)


window.mainloop()