from tkinter import *
from tkinter import font
from tkinter import ttk

window = Tk()
window.geometry("1300x800")
window.title("Bike-sharing system")
l1_font = font.Font(family = "Times New Roman", size = 24)
label1 = Label(text = "Track Vehicle", font = l1_font)
label1.place(x = 500, y = 100)

l2_font = font.Font(family = "Times New Roman", size = 14)
label2 = Label(text = "Vehicle ID", font = l2_font)
label2.place(x = 200, y = 220)
label3 = Label(text = "City Location", font = l2_font)
label3.place(x = 180, y = 280)

def on_select(event):
    selected_value = combo_var.get()
    print("Selected value:", selected_value)

options = ["Option 1", "Option 2", "Option 3", "Option 4"]
combo_var = StringVar(value=options[0])
combobox = ttk.Combobox(textvariable=combo_var, values=options)
combobox.bind("<<ComboboxSelected>>", on_select)
combobox.place(x = 350, y = 220)

combobox2 = ttk.Combobox(textvariable=combo_var, values=options)
combobox2.bind("<<ComboboxSelected>>", on_select)
combobox2.place(x = 350, y = 280)

b_font = font.Font(family = "Times New Roman", size = 13)
button1 = Button(text = "Track", font = b_font)
button1.place(x = 800, y = 200, width = 100, height = 40)
button2 = Button(text = "Back", font = b_font)
button2.place(x = 800, y = 280, width = 100, height = 40)

text_box = Text(window, height=10, width=40)
text_box.place(x=300, y=400, height=300, width=500)

window.mainloop()