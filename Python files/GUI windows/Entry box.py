from tkinter import *
def submit():
    username= entry.get()  #forms and stores as string
    print("Hello " + username)
    entry.config(state=DISABLED)
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1, END)
window = Tk()
entry = Entry(window,
              text=("arial", 50, "bold"),
              fg="#00FF00",
              bg="black",
              show="*")
#entry.insert(0, "spongebob")
entry.pack(side="left")
submit_button = Button(window,
                       text="submit",
                       command=submit)
submit_button.pack(side="right")
delete_button = Button(window,
                       text="delete",
                       command=delete)
delete_button.pack(side="right")
backspace_button = Button(window,
                       text="backspace",
                       command=backspace)
backspace_button.pack(side="right")

window.mainloop()