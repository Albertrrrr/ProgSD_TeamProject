import tkinter as tk
from tkinter import messagebox

def clear_content():
    report_content.delete(1.0, tk.END)

def enter_content():
    # Here, you can add logic to submit the content to the backend
    pass

def refresh_content():
    response = messagebox.askyesno("Confirmation", "Are you sure you want to refresh the content?")
    if response:
        # Here, you can add logic to refresh the content
        pass

def go_back():
    response = messagebox.askyesno("Confirmation", "Are you sure you want to go back?")
    if response:
        # Here, you can add logic to go back or close the window
        root.destroy()

root = tk.Tk()
root.geometry("1000x600")
root.title("Customer Report")

# Set background color
bg_color = "#ADD8E6"

# Create the top part with label and text box
frame_top = tk.Frame(root, bg=bg_color)
frame_top.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

label_frame = tk.Frame(frame_top, bg=bg_color)
label_frame.pack(pady=10, fill=tk.X, expand=True)
tk.Label(label_frame, text="My report", bg=bg_color, font=("Arial", 14)).pack(side=tk.LEFT, padx=10, expand=True)
tk.Button(label_frame, text="Back", command=go_back).pack(side=tk.LEFT, padx=5)
tk.Button(label_frame, text="Refresh", command=refresh_content).pack(side=tk.LEFT, padx=5)

report_display = tk.Text(frame_top, width=130, height=20)
report_display.pack(pady=10)

# Create the bottom part with label, text box, and buttons
frame_bottom = tk.Frame(root, bg=bg_color)
frame_bottom.pack(pady=20, padx=20, fill=tk.BOTH)

tk.Label(frame_bottom, text="Content to be reported:", bg=bg_color, font=("Arial", 12)).pack(pady=10)
report_content = tk.Text(frame_bottom, width=50, height=5)
report_content.pack(pady=10)

button_frame = tk.Frame(frame_bottom, bg=bg_color)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Enter", bg="#2E8B57", fg="white", font=("Arial", 12), command=enter_content).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Clear", bg="#FF4500", fg="white", font=("Arial", 12), command=clear_content).pack(side=tk.LEFT, padx=5)

root.mainloop()
