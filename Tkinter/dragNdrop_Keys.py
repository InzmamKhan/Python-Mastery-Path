from tkinter import *


def up(event):
    myLabel_1.place(x=myLabel_1.winfo_x(), y=myLabel_1.winfo_y()-100)
def left(event):
    myLabel_1.place(x=myLabel_1.winfo_x(), y=myLabel_1.winfo_y()+100)
def down(event):
    myLabel_1.place(x=myLabel_1.winfo_x()-100, y=myLabel_1.winfo_y()-100)
def right(event):
    myLabel_1.place(x=myLabel_1.winfo_x()+100, y=myLabel_1.winfo_y()-100)




# Creating a WINDOW to Apply The MENUBAR
myWindow = Tk()                                           # Instantiating a Window
myWindow.geometry("300x150")                              # To Resize The Window




# Creating a LABEL to Move
myLabel_1 = Label(myWindow,
                bg="black",
                width = 5,
                height = 1)                                # Instantiating a Label 1
myLabel_1.pack()                                          # Applying The Label on The Window  
myLabel_1.bind("<w>", up) 
myLabel_1.bind("<a>", left)  
myLabel_1.bind("<s>", down)            
myLabel_1.bind("<d>", right)  
                                     



myWindow.mainloop()                                       # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)