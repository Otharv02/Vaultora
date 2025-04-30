from tkinter import *
from tkinter import messagebox
from ui.auth import authenticate
from ui.gui import launch_gui  # Main Gui file

def launch_login_gui(root):
    root.title("Vaultora")
    root.geometry("1050x700")  # Window Size
    root.minsize(1050, 700)
    root.maxsize(1050, 700)

    # Create a background frame
    frame = Frame(root, bg="black")
    frame.place(relwidth=1, relheight=1)

    # Splash Screen
    splash_label = Label(root, text="Vaultora", font=("Roboto", 32, "bold"), fg="white", bg="black")
    splash_label.pack(expand=True)

    def login():
        splash_label.destroy()

        # Frame for login
        login_frame = Frame(root, bg="black")
        login_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

        # Username label and entry
        usernameLabel = Label(login_frame, text="Username", bg="black", fg="white", font=("Roboto", 12))
        usernameLabel.grid(row=0, column=0, padx=20, pady=10, sticky="e")
        username_entry = Entry(login_frame, width=30)
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password label and entry
        passwordLabel = Label(login_frame, text="Password", bg="black", fg="white", font=("Roboto", 12))
        passwordLabel.grid(row=1, column=0, padx=20, pady=10, sticky="e")
        password_entry = Entry(login_frame, show="*", width=30)
        password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Login function
        def on_login():
            username = username_entry.get()
            password = password_entry.get()
            if authenticate(username, password):
                for widget in root.winfo_children():
                    widget.destroy()
                launch_gui(root, username)
            else:
                messagebox.showerror("Login Failed", "Invalid Username or Password")

        # Login button
        login_button = Button(login_frame, text="Login", command=on_login, width=20)
        login_button.grid(row=2, column=0, columnspan=2, pady=20)

    # Trigger login after splash
    root.after(2500, login)
    root.mainloop()
