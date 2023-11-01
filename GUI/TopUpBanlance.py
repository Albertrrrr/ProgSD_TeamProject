from tkinter import *
from tkinter import font

from PIL import ImageTk

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
label2 = Label(text="Recharge amount:", font=l2_font)
label2.place(x=180, y=200)
label3 = Label(text="QR code:", font=l2_font)
label3.place(x=600, y=200)

label6 = Label(text="Notification:", font=l2_font)
label6.place(x=180, y=250)

# Entry Widgets
# textbox1 = Entry(font=l2_font)
# textbox1.place(x=480, y=260, width=350, height=30)
# textbox2 = Entry(font=l2_font)
# textbox2.place(x=480, y=320, width=350, height=30)
textbox3 = Entry(font=l2_font)
textbox3.place(x=360, y=200, width=68, height=30)
textbox4 = Entry(font=l2_font)
textbox4.place(x=180, y=280, width=250, height=200)

# Buttons
button1 = Button(text="Go Back", font=b_font, bg='red', fg='white')
button1.place(x=300, y=525, width=100, height=40)
button2 = Button(text="Top-up", font=b_font, bg='green', fg='white')
button2.place(x=600, y=525, width=100, height=40)


# Load and display an image
image_path = r"C:\Users\zyj_8\Documents\GitHub\ProgSD_TeamProject\qrcode_image\qr_test_ali_20231024202355_1.png"  # Change this to your image file path
img = PhotoImage(file=image_path)
img = img.subsample(2)  # Adjust the subsample factor to resize the image (e.g., 2 halves the size)

image_label = Label(image=img)
image_label.place(x=620, y=270)

window.mainloop()
