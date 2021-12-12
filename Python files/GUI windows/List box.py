#listbox= A listing of selectable texts items within its own container.
from tkinter import *

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You ordered: ",end="")

    for index in food:
        print(index+" ",end="")

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())
window = Tk()

listbox = Listbox(window,bg="#f7ffde",font=("constantia",40,"bold"),width=12,selectmode=MULTIPLE)
listbox.pack()
listbox.insert(1,"Idli")
listbox.insert(2,"Dosa")
listbox.insert(3,"Pongal")
listbox.insert(4,"Poori")
listbox.config(height=listbox.size())

submitButton = Button(window,text="SUBMIT",command=submit)
submitButton.pack(side="left")
deleteButton = Button(window,text="DELETE",command=delete)
deleteButton.pack(side="right")

entrybox = Entry(window)
entrybox.pack()

addButton = Button(window,text="ADD",command=add)
addButton.pack()


