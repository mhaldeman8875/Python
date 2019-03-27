
import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)
        
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        
        self.varFname = StringVar()
        self.varLname = StringVar()
        self.varFname.set('First Name')
        self.varLname.set('Last Name')

        self.txtFname = Entry(self.master, text=self.varFname, bg='lightblue')
        self.txtFname.pack()
        self.txtLname = Entry(self.master, text=self.varLname, bg='lightblue')
        self.txtLname.pack()
                   

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
