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
root.geometry("750x720")
root.title("Station property Management")

# Top frame
top_frame = tk.Frame(root, bg="#4682B4")
top_frame.grid(row=0, column=0, sticky='ew', padx=20, pady=10, columnspan=3)

tk.Label(top_frame, text="Station property", font=("Arial", 14, "bold"), bg="#4682B4", width=20, height=2).grid(row=0, column=0, padx=5, pady=5)
tk.Button(top_frame, text="Station property change", bg="#3CB371", font=("Arial", 12), command=station_property_change).grid(row=0, column=1, padx=5, pady=5)
tk.Button(top_frame, text="Refresh", bg="#3CB371", font=("Arial", 12), command=refresh).grid(row=0, column=2, padx=5, pady=5)
tk.Button(top_frame, text="Back", bg="#3CB371", font=("Arial", 12)).grid(row=0, column=3, padx=5, pady=5)

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
tk.Label(left_frame, text="Change station name:", font=("Arial", 12), bg="#4682B4").pack(pady=5)

name_frame = tk.Frame(left_frame, bg="#4682B4")
name_frame.pack(padx=15, pady=2, fill=tk.X)
tk.Label(name_frame, text="Name:", bg="#4682B4").pack(side=tk.LEFT, padx=5)
entry = tk.Entry(name_frame, width=6)
entry.pack(side=tk.LEFT, padx=5)

tk.Button(left_frame, text="Enter", bg="#3CB371").pack(pady=5, side=tk.LEFT, padx=5)
tk.Button(left_frame, text="Clear", bg="#FF4500", command=lambda: clear_content(entry)).pack(pady=5, side=tk.LEFT, padx=5)

# Middle frame
middle_bottom_frame = tk.Frame(root, bg="#4682B4")
middle_bottom_frame.grid(row=2, column=1, sticky='ewns', **bottom_frames_padding)
tk.Label(middle_bottom_frame, text="Change station position:", font=("Arial", 12), bg="#4682B4").pack(pady=5)
frame = tk.Frame(middle_bottom_frame, bg="#4682B4")
frame.pack(pady=5)
tk.Label(frame, text="Position:", bg="#4682B4", width=6).pack(side=tk.LEFT)
tk.Entry(frame, width=6).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(middle_bottom_frame, text="Enter", bg="#3CB371").pack(pady=5, side=tk.LEFT, padx=5)
tk.Button(middle_bottom_frame, text="Clear", bg="#FF4500").pack(pady=5, side=tk.LEFT, padx=5)

# Right frame
right_frame = tk.Frame(root, bg="#4682B4")
right_frame.grid(row=2, column=2, sticky='ewns', **bottom_frames_padding)
tk.Label(right_frame, text="Change station capacity:", font=("Arial", 12), bg="#4682B4").pack(pady=5)
frame = tk.Frame(right_frame, bg="#4682B4")
frame.pack(pady=5)
tk.Label(frame, text="Num:", bg="#4682B4", width=6).pack(side=tk.LEFT)
tk.Entry(frame, width=6).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(right_frame, text="Enter", bg="#3CB371").pack(pady=5, side=tk.LEFT, padx=5)
tk.Button(right_frame, text="Clear", bg="#FF4500").pack(pady=5, side=tk.LEFT, padx=5)

root.mainloop()
