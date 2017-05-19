# main.py
from tkinter import *
import ui
if __name__ == "__main__":
    top = Tk()
    ui.Application(top).mainloop()
    try:
        top.destroy()
    except:
        pass
