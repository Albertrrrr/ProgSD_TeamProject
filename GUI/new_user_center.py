import tkinter as tk


def user_center():
    # Create main window
    root = tk.Tk()
    root.title("User Center")

    # Set the window size and background color
    root.geometry("800x600")
    root.configure(bg="#4A90E2")  # Blue background color

    # User center label
    tk.Label(root, text="User center", bg="#4A90E2", fg="white", font=("Arial", 24)).place(x=30, y=30, width=250,
                                                                                           height=60)

    # Back button
    tk.Button(root, text="Back", bg="#2ECC71", fg="white", font=("Arial", 18)).place(x=70, y=130, width=120,
                                                                                     height=50)  # Green button

    # Functions to create sections
    def create_section(y_position, title):
        tk.Label(root, text=title, bg="#4A90E2", fg="white", font=("Arial", 18)).place(x=250, y=y_position)
        tk.Entry(root, font=("Arial", 16)).place(x=250, y=y_position + 50, width=350, height=40)
        tk.Button(root, text="OK", bg="#2ECC71", fg="white", font=("Arial", 16)).place(x=610, y=y_position + 50,
                                                                                       width=80, height=40)

    # Change password section
    create_section(150, "Change password")

    # Modify email section
    create_section(260, "Modify email")

    # Change name section
    create_section(370, "Change name")

    root.mainloop()


user_center()
