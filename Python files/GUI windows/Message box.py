from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title="Info message box",message="You are a human")
    messagebox.showwarning(title="WARNING!", message="You have a VIRUS! ! !")
    messagebox.showerror(title="whatever",message="There is something wrong")
    if messagebox.askokcancel(title="thing", message="Do you want to do the thing"):
           print("You did the thing!")
    else:
           print("You didn't do the thing!")
    #messagebox.askretrycancel
    #messagebox.askyesno
    #messagebox.askquestion
    #messagebox.askeyesnocancel  icon="warning","info","error"
window = Tk()
window.title("Are you human?")
button = Button(window, text="YES", command=click)
button.pack()
window.mainloop()