#button = when you click, it does stuff
from tkinter import *
count = 0
def click():
    global count
    count += 1
    print(count)
    print("You clicked the button")

window = Tk()
button= Button(window,
               text="cLiCk mE",
               command=click,
               font=("comic sans",20,"bold"),
               fg="#00FF00",
               bg="black",
               bd=10,
               relief=RAISED,
               activeforeground="red",
               activebackground="black",
               state=ACTIVE) #you can also add image by using image=
button.pack()
window.mainloop()