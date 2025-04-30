from tkinter import *
from tkinter import messagebox
from ui.auth import authenticate
from ui.gui import launch_gui # Main Gui file

def launch_login_gui(root):
    root.title("Vaultora")

    # create a frame and place color in the window
    frame = Frame(root, bg="black")
    frame.place(relwidth=1, relheight=1)

    root.geometry(("1050x700")) # Window Size
    root.minsize(1050,700)
    root.maxsize(1050,700)  

    # Splash Screen 
    splash_label = Label(root, text="Vaultora", font=("Helvetica", 32, "bold"), fg="white", bg="black")
    splash_label.pack(expand=True)

    def login():
        # Remove splash
        splash_label.destroy()

        root.grid_columnconfigure((0,1), weight=1)

        # Username label and entry
        usernameLabel = Label(root, text="Username", bg="black", fg="white", font=("Helvetica", 12), justify="center")
        usernameLabel.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        username_entry = Entry(root)
        username_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        # Password label and entry
        passwordLabel = Label(root, text="Password", bg="black", fg="white", font=("Helvetica", 12), justify="center")
        passwordLabel.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        password_entry = Entry(root, show="*")  # Add show="*" to hide password input
        password_entry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        def on_login():
            username = username_entry.get()      
            password = password_entry.get()

            if authenticate(username, password):
                for widget in root.winfo_children(): # Clear all widgets from root instead of destroying it
                    widget.destroy()
                launch_gui(root,username)
            else:
                messagebox.showerror("Login Failed", "Invalid Username or Password")
        # loing button

        login_button = Button(root, text="Login", command=on_login)
        login_button.grid(row=5, column=0, columnspan=2, pady=20)
    
    # Wait 2.5s
    root.after(2500, login)
    root.mainloop()
