from tkinter import *
#label= an area widget that hold text and/or image within a window
window = Tk()
photo= PhotoImage(file='../../IMAGES/Tokyo ghoul.png')
label = Label(window,
              text="There's no such thing as fate.\n"
                   "It's simply a combination of one circumstance and the next.....",
              font= ('GB18030 Bitmap', 10 , 'bold'),
              relief=RAISED,
              bg="black",
              fg="white",
              bd=10,
              padx=10,
              pady=10,
              image=photo,
              compound="bottom")
label.pack()
window.mainloop()