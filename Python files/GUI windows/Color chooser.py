from tkinter import *
from tkinter import colorchooser #submodule
def click():
    window.config(bg=colorchooser.askcolor()[1])
window = Tk()
window.geometry("420x420")
button = Button(window,text="click me",command=click)
button.pack()
window.mainloop()