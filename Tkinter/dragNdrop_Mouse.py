from tkinter import *


def drag(event):
    myLabel_1.startX = event.x
    myLabel_1.startY = event.y
def motion(event):
    x = myLabel_1.winfo_x() - myLabel_1.startX + event.x
    y = myLabel_1.winfo_y() - myLabel_1.startY + event.y
    myLabel_1.place(x=x, y=y)


# Creating a WINDOW to Apply The MENUBAR
myWindow = Tk()                                           # Instantiating a Window
myWindow.geometry("300x150")                              # To Resize The Window




# Creating a LABEL to Move
myLabel_1 = Label(myWindow,
                bg="black",
                width = 5,
                height = 1,
                padx = 20,
                pady = 20)                                # Instantiating a Label 1
myLabel_1.pack()                                          # Applying The Label on The Window
myLabel_1.bind("<Button-1>", drag)  
myLabel_1.bind("<B1-Motion>", motion)           
                                     



myWindow.mainloop()                                       # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)