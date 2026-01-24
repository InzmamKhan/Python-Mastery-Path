from tkinter import *




# Creating a Variable to Check The Active State of Widget
x = IntVar()                                  

# Creating a Command to Get Specific Job Done
@staticmethod                                                                   
def mycheckboxCommand():
    if x==1:
         print("You've Agreed to Terms and Conditions")
    elif x!=1:
        print("You've Not Agreed to Terms and Conditions")




# Creating a WINDOW to Apply The MENUBAR
myWindow = Tk()                                           # Instantiating a Window
myWindow.geometry("300x150")                              # To Resize The Window




# Creating a Check Box
mycheckbox = Checkbutton(myWindow,
                         text="I am Agreeing on T&C",
                         variable=x,
                         onvalue=1,
                         offvalue=0,
                         font=("Arial", 10, "bold"),
                         fg="tan",
                         bg="black",
                         command=mycheckboxCommand)                             # Instantiating The Check Box Button
mycheckbox.pack()                                                               # Applying on The Window




myWindow.mainloop()                                                             # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)