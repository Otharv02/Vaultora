# GUI code goes here.

from tkinter import *



def launch_gui(root,username):
    root.title("Vaultora")

    # create a frame and place color in the window
    frame = Frame(root, bg="black")
    frame.place(relwidth=1, relheight=1)

    root.geometry(("1050x700")) # Window Size
    root.minsize(1050,700)
    root.maxsize(1050,700)

    Label(root, text=f"Hello, {username}", bg="black", fg="white", font=("Helvetica", 12)).pack(pady=5)



