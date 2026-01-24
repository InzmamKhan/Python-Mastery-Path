from tkinter import *




# Creating a WINDOW to Apply The MENUBAR
myWindow = Tk()                                           # Instantiating a Window




# Creating The MENUBAR
mymenubar = Menu(myWindow)                               # Creating a Menu and Pasting it to the Specific Window
myWindow.config(menu=mymenubar)

myfilemenu = Menu(mymenubar)                  # Adding an Option to The Menubar
mymenubar.add_cascade(label="File", menu=myfilemenu)     # Labeling that Option




myWindow.mainloop()                                       # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)