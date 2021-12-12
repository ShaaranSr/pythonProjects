from tkinter import *
from tkinter import filedialog

def openFile():
    filepath= filedialog.askopenfilename(initialdir="C:\\Users\\KavinShaaran\\PycharmProjects\\pythonProjects",
                                         filetypes=(("text files","*.txt"),
                                                   ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())

window = Tk()

button = Button(window, text="open", command=openFile) 
button.pack()
window.mainloop()