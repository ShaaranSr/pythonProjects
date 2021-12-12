#radio button = it is just like checkbox but you can only select one option
from tkinter import *
food = ["Pizza","Hamburger","Hotdog"]
def order():
    if (x.get()==0):
        print("You ordered a Pizza!")
    elif (x.get()==1):
        print("You ordered a Hamburger!")
    elif (x.get()==2):
        print("You ordered a Hotdog!")

window = Tk()

pizzaImage = PhotoImage(file='')      #unfortunately image is not working as it
HamburgerImage = PhotoImage(file='')  # it is not icon (transparent)
HotdogImage = PhotoImage(file='')
food_image = [pizzaImage,HamburgerImage,HotdogImage]

x = IntVar()
for index in range(len(food)):
   radio_buttons = Radiobutton(window,
                            text=food[index],
                            variable=x,
                            value=index,
                            padx=25,  #adds padding on x axis
                            font=("impact",50),
                            image=food_image[index],
                            fg="green",
                            bg="black",
                            compound="left",
                            command=order,
                            indicatoron=0,
                            width=400)
   radio_buttons.pack(anchor=W)
window.mainloop()