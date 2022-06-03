from tkinter import *
from tkinter import messagebox

root =Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert Box","Stop Virus found")


but= Button(root,text="ok",command=msg)
but.place(x=100,y=100)
root.mainloop()                                                                                   
