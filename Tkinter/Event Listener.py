from tkinter import *



# Creating Some Functions to do Some Job
def someFunc_1_1(event):
    mylabel.config(text = "w")
def someFunc_1_2(event):
    mylabel.config(text = "s")
def someFunc_2_1(event):
    mylabel.config(text = "LMB")
def someFunc_2_2(event):
    mylabel.config(text = "MMB")
def someFunc_2_3(event):
    mylabel.config(text = "RMB")
def someFunc_3_1(event):
    text = " Co-or when Entered "+str(event.x)+" ,"+str(event.y)
    mylabel.config(text = text)
def someFunc_3_2(event):
    text = " Co-or when Left "+str(event.x)+" ,"+str(event.y)
    mylabel.config(text = text)
def someFunc_3_3(event):
    text = " Co-or when Moved "+str(event.x)+" ,"+str(event.y)
    mylabel.config(text = text)



# Creating a WINDOW & LABEL to Apply The Keyboard Listener
myWindow = Tk()                                                                 # Instantiating a Window
myWindow.geometry("300x150")                                                    # To Resize The Window

mylabel = Label(myWindow, 
                font=("Arial", 15, "bold"),
                fg="tan")
mylabel.pack()


# Creating a Keyboard Listener
myWindow.bind("<w>", someFunc_1_1)
myWindow.bind("<s>", someFunc_1_2)
# Creating a Mouse Listener
myWindow.bind("<Button-1>", someFunc_2_1)
myWindow.bind("<Button-2>", someFunc_2_2)
myWindow.bind("<Button-3>", someFunc_2_3)
myWindow.bind("<Enter>", someFunc_3_1)
myWindow.bind("<Leave>", someFunc_3_2)
myWindow.bind("<Motion>", someFunc_3_3)



myWindow.mainloop()                                                             # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)