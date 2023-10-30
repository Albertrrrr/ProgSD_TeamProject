import tkinter as tk

def refresh():
    pass

def station_property_change():
    pass

def clear_content(entry_widget):
    entry_widget.delete(0, tk.END)

root = tk.Tk()
root.geometry("650x450")
root.title("View all vehicles")

# Top frame
top_frame = tk.Frame(root, bg="#4682B4")
top_frame.grid(row=0, column=0, sticky='ew', padx=20, pady=10, columnspan=4)

tk.Label(top_frame, text="View all vehicles", font=("Arial", 14, "bold"), bg="#4682B4", width=20, height=2).grid(row=0, column=0, padx=5, pady=5)
tk.Button(top_frame, text="Refresh", bg="#3CB371", font=("Arial", 12), command=refresh).grid(row=0, column=2, padx=5, pady=5)
tk.Button(top_frame, text="Back", bg="#3CB371", font=("Arial", 12)).grid(row=0, column=3,padx=5, pady=5)

# Middle frame for display
middle_frame = tk.Frame(root, bd=2, relief="groove")
middle_frame.grid(row=1, column=0, sticky='nsew', padx=20, pady=10, columnspan=4)
text_display = tk.Text(middle_frame, wrap=tk.WORD)
text_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
