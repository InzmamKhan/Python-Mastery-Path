from tkinter import *




# Creating a WINDOW to Apply The MENUBAR
myWindow = Tk()                                           # Instantiating a Window




# Creating an Canvas
myCanvas  = Canvas(myWindow,
                   height=500,
                   width=500)                              # Applying The Entry on The Window
myCanvas.create_line(0,0,100,100,fill="black", width=10)




myWindow.mainloop()                                        # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)