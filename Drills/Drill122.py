from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.master.title("Check files")

        self.btnBrowse1 = Button(self.master, text="Browse...", width=15, height=1)
        self.btnBrowse1.grid(row=0, column=1, padx=(20,20), pady=(50,10))
        self.btnBrowse2 = Button(self.master, text="Browse...", width=15, height=1)
        self.btnBrowse2.grid(row=1, column=1, padx=(20,20), pady=(10,10))
        self.btnCheck = Button(self.master, text="Check for files...", width=15, height=2)
        self.btnCheck.grid(row=2, column=1, padx=(20,20), pady=(10,20))
        self.btnClose = Button(self.master, text="Close Program", width=15, height=2)
        self.btnClose.grid(row=2, column=2, padx=(20,20), pady=(10,20), sticky=E)
        

        self.box1 = Entry(self.master, text='', width=60)
        self.box1.grid(row=0, column=2, padx=(20,20), pady=(50,10))
        self.box2 = Entry(self.master, text='', width=60)
        self.box2.grid(row=1, column=2, padx=(20,20), pady=(10,10))



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
