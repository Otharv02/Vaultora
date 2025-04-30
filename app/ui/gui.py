# GUI code goes here.
import os
import shutil # for peroforming operation like copy and paste on files
from tkinter import *
from tkinter import filedialog, messagebox

destinationdirectory = os.path.abspath(os.path.join("data")) ## <- DO NOT EDIT
selected_file = []

def uploadAction(event=None):
    
    global selected_file
    selected_file = list(filedialog.askopenfilenames())
    print(selected_file)

    if not selected_file:
        messagebox.showerror("Error, No file selected")
        return
    
    if not os.path.exists(destinationdirectory):
        os.makedirs(destinationdirectory)

    for file in selected_file:
        try:
            filename = os.path.basename(file) #file name
            dest_path = os.path.join(destinationdirectory,filename) # destinationdirectory + filename 
            shutil.copy2(file, dest_path) # this will vopy and then move
        except Exception as e:
            messagebox.showerror("Error", f"Failed to move file: {file}\n{e}")
            return

    



def launch_gui(root,username):
    root.title("Vaultora")

    # create a frame and place color in the window (Main)
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
    setting_button = Button(left_Frame, text="Setting",width=15)
    setting_button.pack(pady=10)


    # # Preview + View side 
    # right_Frame = Frame(root, bg="black")
    # right_Frame.place(x=0,y=0,relheight=1,relwidth=0.75)





