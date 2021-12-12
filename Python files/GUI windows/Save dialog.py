from tkinter import *
from tkinter import filedialog
def save():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[("Text file", ".txt"),
                                               ("HTML file",".html"),
                                               ("All files",".*"),
                                               ])
    if file is None:
        return
    #filetext = str(text.get("1,0",END))
    filetext = input("Enter:  ")
    file.write(filetext)
    file.close()

window = Tk()

button = Button(text="save",command=save)
button.pack()
text = Text(window)
text.pack()

window.mainloop()