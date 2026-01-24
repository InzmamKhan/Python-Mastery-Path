from tkinter import *


# Creating a WINDOW
myWindow = Tk()                                           # Instantiating a Window
myWindow.geometry("300x300")                              # To Resize The Window
myWindow.title("My First Window")                         # To Change The Title of The Window
myWindow.config(background="#CECBC8")                     # To Change The Background Color


@staticmethod
def settingImagesAndIcons():                              # To Change The Top Corner Icon 
    cornericon = PhotoImage(file="Sample_Image_1.jpg")    
    myWindow.iconphoto(True, cornericon)

myWindow.mainloop()                                       # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)