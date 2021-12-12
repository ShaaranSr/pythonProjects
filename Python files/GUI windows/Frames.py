#frame = a rectangular container to group and hold widget together
from tkinter import *
window = Tk()
frame = Frame(window,bg="pink",bd=5,relief=RAISED)
frame.pack()
Button(frame,text="W",font=("consolas",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("consolas",25),width=3).pack(side=LEFT)

window.mainloop()