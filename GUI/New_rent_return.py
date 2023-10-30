
import tkinter as tk
from tkinter import messagebox

def ask_confirmation():
    response = messagebox.askyesno("Confirmation", "Do you want to proceed with this operation?")
    if response:
        print("User confirmed the operation.")
    else:
        print("User canceled the operation.")

def create_app():
    root = tk.Tk()
    root.title("Vehicle information")


    scale_factor = 1.1
    background_color = "#ADD8E6"
    button_color = "#2E8B57"


    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # 第一部分
    frame1 = tk.Frame(root, bg=background_color)
    frame1.grid(row=0, column=0, padx=15 * scale_factor, pady=15 * scale_factor, sticky="nsew")

    tk.Label(frame1, text="Stop:", bg=background_color, fg="black", font=("Arial", int(14*scale_factor))).place(x=130 * scale_factor, y=30 * scale_factor)
    tk.Entry(frame1, width=int(10*scale_factor), font=("Arial", int(12*scale_factor))).place(x=190 * scale_factor, y=30 * scale_factor)
    tk.Button(frame1, text="Back", bg=button_color, fg="white", font=("Arial", int(12*scale_factor)), command=ask_confirmation).place(x=180 * scale_factor, y=150 * scale_factor)

    frame2 = tk.Frame(root, bg=background_color)
    frame2.grid(row=0, column=1, padx=15 * scale_factor, pady=15 * scale_factor, sticky="nsew")
    tk.Label(frame2, text="Vehicle information", bg=background_color, fg="black", font=("Arial", int(14*scale_factor))).pack(pady=15 * scale_factor)
    tk.Text(frame2, width=int(53*scale_factor), height=int(8*scale_factor), font=("Arial", int(12*scale_factor))).pack(pady=20 * scale_factor)

    # 第二部分
    frame3 = tk.Frame(root, bg=background_color, width=400 * scale_factor, height=150 * scale_factor)
    frame3.grid(row=1, column=0, padx=15 * scale_factor, pady=15 * scale_factor, sticky="nsew")
    tk.Label(frame3, text="Rent:", bg=background_color, fg="black", font=("Arial", int(14*scale_factor))).place(x=20 * scale_factor, y=20 * scale_factor)
    tk.Entry(frame3, width=int(20*scale_factor), font=("Arial", int(12*scale_factor))).place(x=80 * scale_factor, y=20 * scale_factor)
    tk.Button(frame3, text="Enter", bg=button_color, fg="white", font=("Arial", int(10*scale_factor)), command=ask_confirmation).place(x=270 * scale_factor, y=20 * scale_factor)
    tk.Button(frame3, text="Report damage", bg=button_color, fg="white", font=("Arial", int(12*scale_factor)), command=ask_confirmation).place(x=100 * scale_factor, y=90 * scale_factor)

    frame4 = tk.Frame(root, bg=background_color, width=400 * scale_factor, height=150 * scale_factor)
    frame4.grid(row=1, column=1, padx=15 * scale_factor, pady=15 * scale_factor, sticky="nsew")
    tk.Label(frame4, text="Return:", bg=background_color, fg="black", font=("Arial", int(14*scale_factor))).place(x=20 * scale_factor, y=20 * scale_factor)
    tk.Entry(frame4, width=int(20*scale_factor), font=("Arial", int(12*scale_factor))).place(x=90 * scale_factor, y=20 * scale_factor)
    tk.Button(frame4, text="Enter", bg=button_color, fg="white", font=("Arial", int(10*scale_factor)), command=ask_confirmation).place(x=280 * scale_factor, y=20 * scale_factor)
    tk.Button(frame4, text="Pay", bg=button_color, fg="white", font=("Arial", int(12*scale_factor)), command=ask_confirmation).place(x=100 * scale_factor, y=90 * scale_factor)

    root.mainloop()

create_app()