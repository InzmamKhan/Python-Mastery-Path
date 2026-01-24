from tkinter import *




# Creating a WINDOW to Apply The MENUBAR
myWindow = Tk()                                           # Instantiating a Window
myWindow.geometry("300x150")                              # To Resize The Window




# Creating a Scale 
myScale = Scale(myWindow,
                from_=0,
                to=100,
                length=250,
                width=25,
                tickinterval=5,
                resolution=5)                              # Instantiating The Scale
myScale.pack()                                             # Applying on The Window



myWindow.mainloop()                                        # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)