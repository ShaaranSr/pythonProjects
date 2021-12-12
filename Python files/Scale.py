from tkinter import *
def submit():
    print('The temperature is '+ str(scale.get())+ ' degree celcius')
    pass
window = Tk()
scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,       #orientation of scale
              font=("consolas",20),
              tickinterval=10,       #adds numeric indicator of value
              showvalue=0,           #hide current value
              resolution=5,
              troughcolor="yellow",
              fg="red",
              bg="black")          #increment slider
scale.set(100)
button = Button(window, text="submit", command=submit)
scale.pack()
button.pack()
window.mainloop()
