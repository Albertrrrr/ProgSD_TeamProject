import tkinter as tk

def refresh():
    pass

def station_property_change():
    pass

def clear_content(entry_widget):
    entry_widget.delete(0, tk.END)

root = tk.Tk()
root.geometry("700x650")
root.title("Repair Management")

# Top frame
top_frame = tk.Frame(root, bg="#4682B4")
top_frame.grid(row=0, column=0, sticky='ew', padx=20, pady=10, columnspan=4)

tk.Label(top_frame, text="Repair Management", font=("Arial", 14, "bold"), bg="#4682B4", width=20, height=2).grid(row=0, column=0, padx=5, pady=5)
tk.Button(top_frame, text="Refresh", bg="#3CB371", font=("Arial", 12), command=refresh).grid(row=0, column=2, padx=5, pady=5)
tk.Button(top_frame, text="Back", bg="#3CB371", font=("Arial", 12)).grid(row=0, column=3,padx=5, pady=5)

# Middle frame for display
middle_frame = tk.Frame(root, bd=2, relief="groove")
middle_frame.grid(row=1, column=0, sticky='nsew', padx=20, pady=10, columnspan=4)
text_display = tk.Text(middle_frame, wrap=tk.WORD)
text_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Bottom frames
bottom_frames_padding = {"pady": 10, "padx": 20}

def generate_frame(root, title, labels):
    frame = tk.Frame(root, bg="#4682B4")
    frame.grid(sticky='ewns', **bottom_frames_padding)
    tk.Label(frame, text=title, font=("Arial", 12), bg="#4682B4").pack(pady=5)
    entries = []
    for label_text in labels:
        inner_frame = tk.Frame(frame, bg="#4682B4")
        inner_frame.pack(fill=tk.X, pady=5, padx=50)  # Added padx to center the content within the frame
        tk.Label(inner_frame, text=label_text, bg="#4682B4", width=6).pack(side=tk.LEFT)
        entry = tk.Entry(inner_frame, width=7)
        entry.pack(side=tk.LEFT)
        entries.append(entry)
    tk.Button(frame, text="Enter", bg="#3CB371").pack(pady=5, side=tk.LEFT, padx=5)
    tk.Button(frame, text="Clear", bg="#FF4500", command=lambda: [e.delete(0, tk.END) for e in entries]).pack(pady=5, side=tk.LEFT, padx=5)
    return frame

# Only keep "Start repair" and "Over repair"
left_frame = generate_frame(root, "Start repair:", ["report:"])
left_frame.grid(row=2, column=1)
middle_right_frame = generate_frame(root, "Over repair:", ["bikeID:", "report:"])
middle_right_frame.grid(row=2, column=2)

root.mainloop()
