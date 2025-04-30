# Run this file for launching the application.
# ui/gui       -> have the main gui
# ui/login_gui -> have the login logic
# ui/auth      -> have the username, password stored (for testing only)

from ui.login_gui import launch_login_gui
from tkinter import Tk

def main():
    root = Tk()
    launch_login_gui(root)

if __name__ == "__main__":
    main()