# GUI code goes here.

from tkinter import *

def uploadAction(event=None):
    from tkinter import filedialog
    filename = filedialog.askopenfilename()
    # print("Selected :", filename)





def launch_gui(root,username):
    root.title("Vaultora")

    # create a frame and place color in the window
    frame = Frame(root, bg="black")
    frame.place(relwidth=1, relheight=1)

    root.geometry(("1050x700")) # Window Size
    root.minsize(1050,700)
    root.maxsize(1050,700)

    Label(root, text=f"Hello, {username}", bg="black", fg="white", font=("Roboto", 12)).pack(pady=5)

    # Action (Load File/History/Setting)
    left_Frame = Frame(root, bg="lightblue")
    left_Frame.place(x=0,y=0,relheight=1,relwidth=0.15)

    #Upload Button 
    upload_button = Button(left_Frame, text="Upload",width=15,command=uploadAction)
    upload_button.pack(pady=10)

    # log   
    log_button = Button(left_Frame, text="History",width=15)
    log_button.pack(pady=10)

    # Setting
    setting_button = Button(left_Frame, text="Upload",width=15)
    setting_button.pack(pady=10)


