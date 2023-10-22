from tkinter import *
from tkinter import font

window = Tk()
window.geometry("1000x600")
window.title("Bike-sharing System")

# Define fonts
l1_font = font.Font(family="Helvetica", size=32, weight='bold')
l2_font = font.Font(family="Helvetica", size=14)
c_font = font.Font(family="Helvetica", size=14)
b_font = font.Font(family="Helvetica", size=14)

# Label 1
label1 = Label(text="Welcome Customer!", font=l1_font)
label1.place(x=300, y=80)

# Labels for Username, Password, and Repeat Password
label2 = Label(text="Username:", font=l2_font)
label2.place(x=280, y=200)
label3 = Label(text="Password:", font=l2_font)
label3.place(x=280, y=280)
label4 = Label(text="Repeat Password:", font=l2_font)
label4.place(x=213, y=360)

# Entry Widgets
textbox1 = Entry(font=l2_font)
textbox1.place(x=380, y=200, width=350, height=30)
textbox2 = Entry(font=l2_font, show="*")  # Show asterisks for password
textbox2.place(x=380, y=280, width=350, height=30)
textbox3 = Entry(font=l2_font, show="*")
textbox3.place(x=380, y=360, width=350, height=30)

# Checkbuttons for User Type
check_var1 = IntVar()
check1 = Checkbutton(text="Customer", font=c_font, variable=check_var1)
check1.place(x=250, y=450)
check_var2 = IntVar()
check2 = Checkbutton(text="Operator", font=c_font, variable=check_var2)
check2.place(x=450, y=450)
check_var3 = IntVar()
check3 = Checkbutton(text="Manager", font=c_font, variable=check_var3)
check3.place(x=650, y=450)

# Buttons
button1 = Button(text="Go Back", font=b_font, bg='red', fg='white')
button1.place(x=300, y=530, width=100, height=40)
button2 = Button(text="Register", font=b_font, bg='green', fg='white')
button2.place(x=600, y=530, width=100, height=40)

window.mainloop()
