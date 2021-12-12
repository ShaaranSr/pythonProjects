from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("1080x720")
window.title("My first GUI box")
window.config(background='grey')
icon = PhotoImage(file='../../IMAGES/kavin.png')
window.iconphoto(True,icon)
window.mainloop() #place window on computer screen