from tkinter import *
def display():
    if(x.get()):
       print("You agree!!")
    else:
       print("you don't agree :(")

window = Tk()
x = BooleanVar()
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=("Arial",20),
                           fg="#00FF00",
                           bg="black")
check_button.pack()
window.mainloop()