#text widget = functions like a text area,
# you can enter a multiple lines of text
from tkinter import *
def submit():
    input = text.get("1.0", END)
    print(input)

window = Tk()
text = Text(window,bg="light yellow",font=("Ink Free",20),
            fg="Purple",
            height=8,
            width=20,
            padx=20,
            pady=20)
text.pack()
submit_button= Button(window, text="submit",command=submit)
submit_button.pack()
window.mainloop()