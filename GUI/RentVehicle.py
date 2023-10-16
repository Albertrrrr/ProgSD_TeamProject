from tkinter import *
from tkinter import font
from tkinter import ttk


window = Tk()
window.geometry("1300x800")
window.title("Bike-sharing system")
l1_font = font.Font(family = "Times New Roman", size = 24)
label1 = Label(text = "Rent vehicle", font = l1_font)
label1.place(x = 560, y = 80)

l2_font = font.Font(family = "Times New Roman", size = 14)
label2 = Label(text = "Rent localtion", font = l2_font)
label2.place(x = 120, y = 180)
label3 = Label(text = "Vehicle type", font = l2_font)
label3.place(x = 700, y = 280)
label4 = Label(text = "Rent time", font = l2_font)
label4.place(x = 720, y = 480)

def on_select(event):
    selected_value = combo_var.get()
    print("Selected value:", selected_value)

options = ["Option 1", "Option 2", "Option 3", "Option 4"]
combo_var = StringVar(value=options[0])
combobox = ttk.Combobox(textvariable=combo_var, values=options)
combobox.bind("<<ComboboxSelected>>", on_select)
combobox.place(x = 860, y = 280)

label5 = Label(text="Min：",font = 15)
text = Text(height=1, width=10)
text.insert("1.0", "Min：")
text.place(x = 850, y = 480, width = 180,height = 25)

scrollbar = Scrollbar(window, orient=VERTICAL, command=text.yview)
scrollbar.place(x=120, y=220, height=80)
text.config(yscrollcommand=scrollbar.set)

b_font = font.Font(family = "Times New Roman", size = 13)
button1 = Button(text = "GoBack", font = b_font)
button1.place(x = 400, y = 650, width = 100, height = 40)
button2 = Button(text = "Request Rent", font = b_font)
button2.place(x = 700, y = 650, width = 120, height = 40)

window.mainloop()