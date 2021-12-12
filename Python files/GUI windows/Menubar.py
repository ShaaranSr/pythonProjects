from tkinter import *

def openFile():
    print("The file is opened!")
def saveFile():
    print("The file is saved!")
def cutFile():
    print("The file is cut!")
def copyFile():
    print("The file is copied!")
def pasteFile():
    print("The file is pasted!")

window = Tk()
menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="file",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu) #add image compound="left"
editMenu.add_command(label="Cut",command=cutFile)
editMenu.add_command(label="Copy",command=copyFile)
editMenu.add_command(label="Paste",command=pasteFile)
window.mainloop()