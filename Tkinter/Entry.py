from tkinter import *




# Creating a WINDOW to Apply The MENUBAR
myWindow = Tk()                                           # Instantiating a Window
myWindow.geometry("300x150")                              # To Resize The Window




# Creating an Entry
myEntry = Entry(myWindow,
                font=("Arial", 20, "bold"))              # Instantiating an Entry
myEntry.pack()                                           # Applying The Entry on The Window




myWindow.mainloop()                                       # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)