import tkinter as tk

def refresh():
    pass

def station_property_change():
    pass

def add_station():
    pass

def delete_station():
    pass

def clear_content(entry_widget):
    entry_widget.delete(0, tk.END)

root = tk.Tk()
root.geometry("700x720")
root.title("Station Management")

# Top frame
top_frame = tk.Frame(root, bg="#4682B4")
top_frame.grid(row=0, column=0, sticky='ew', padx=20, pady=10, columnspan=3)

tk.Label(top_frame, text="Station management", font=("Arial", 14, "bold"), bg="#4682B4", width=20, height=2).grid(row=0, column=0, padx=5, pady=5)
tk.Button(top_frame, text="Station property change", bg="#3CB371", font=("Arial", 12), command=station_property_change).grid(row=0, column=1, padx=5, pady=5)
tk.Button(top_frame, text="Refresh", bg="#3CB371", font=("Arial", 12), command=refresh).grid(row=0, column=2, padx=5, pady=5)
tk.Button(top_frame, text="Back", bg="#3CB371", font=("Arial", 12)).grid(row=0, column=3,padx=5, pady=5)

# Middle frame for display
middle_frame = tk.Frame(root, bd=2, relief="groove")
middle_frame.grid(row=1, column=0, sticky='nsew', padx=20, pady=10, columnspan=3)
text_display = tk.Text(middle_frame, wrap=tk.WORD)
text_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Bottom frames
bottom_frames_padding = {"pady": 10, "padx": 20}

# Left frame
left_frame = tk.Frame(root, bg="#4682B4")
left_frame.grid(row=2, column=0, sticky='ewns', **bottom_frames_padding)
tk.Label(left_frame, text="Add a new bike:", font=("Arial", 12), bg="#4682B4").pack(pady=5)
tk.Label(left_frame, text="Type", bg="#4682B4").pack(anchor='w', padx=5)
tk.Radiobutton(left_frame, text="E-bike", bg="#4682B4", value=1).pack(anchor='w', padx=5)
tk.Radiobutton(left_frame, text="Bike", bg="#4682B4", value=2).pack(anchor='w', padx=5)
tk.Label(left_frame, text="Station", bg="#4682B4").pack(anchor='w', padx=5)
entry = tk.Entry(left_frame)
entry.pack(fill=tk.X, padx=10, pady=5)
tk.Label(left_frame, text="Status:", bg="#4682B4").pack(anchor='w', padx=5)
tk.Radiobutton(left_frame, text="Normal", bg="#4682B4", value=1).pack(anchor='w', padx=5)
tk.Button(left_frame, text="Enter", bg="#3CB371").pack(pady=5, side=tk.LEFT, padx=5)
tk.Button(left_frame, text="Clear", bg="#FF4500", command=lambda: clear_content(entry)).pack(pady=5, side=tk.LEFT, padx=5)

# Middle frame
middle_bottom_frame = tk.Frame(root, bg="#4682B4")
middle_bottom_frame.grid(row=2, column=1, sticky='ewns', **bottom_frames_padding)
tk.Label(middle_bottom_frame, text="Add a new station:", font=("Arial", 12), bg="#4682B4").pack(pady=5)
for label_text in ["Name:", "Position:", "Max:"]:
    frame = tk.Frame(middle_bottom_frame, bg="#4682B4")
    frame.pack(pady=5)
    tk.Label(frame, text=label_text, bg="#4682B4", width=6).pack(side=tk.LEFT)
    tk.Entry(frame, width=15).pack(side=tk.LEFT, padx=5)  # Set width to 15
tk.Button(middle_bottom_frame, text="Enter", bg="#3CB371").pack(pady=5, side=tk.LEFT, padx=5)
tk.Button(middle_bottom_frame, text="Clear", bg="#FF4500", command=lambda: clear_content(tk.Entry(middle_bottom_frame))).pack(pady=5, side=tk.LEFT, padx=5)

# Right frame
right_frame = tk.Frame(root, bg="#4682B4")
right_frame.grid(row=2, column=2, sticky='ewns', **bottom_frames_padding)
tk.Label(right_frame, text="Delete station:", font=("Arial", 12), bg="#4682B4").pack(pady=5)
frame = tk.Frame(right_frame, bg="#4682B4")
frame.pack(pady=5)
tk.Label(frame, text="ID:", bg="#4682B4", width=6).pack(side=tk.LEFT)
tk.Entry(frame, width=15).pack(side=tk.LEFT, padx=5)  # Set width to 15
tk.Button(right_frame, text="Enter", bg="#3CB371").pack(pady=5, side=tk.LEFT, padx=5)
tk.Button(right_frame, text="Clear", bg="#FF4500", command=lambda: clear_content(tk.Entry(right_frame))).pack(pady=5, side=tk.LEFT, padx=5)

root.mainloop()
