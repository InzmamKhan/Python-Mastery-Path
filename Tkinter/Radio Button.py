from tkinter import *




# Creating a WINDOW to Apply The MENUBAR
myWindow = Tk()                                           # Instantiating a Window
myWindow.geometry("300x150")                              # To Resize The Window




# Creating a Radio Button
food = ["Pizza", "Hamburger", "Ice-Cream"]
y = IntVar                                                                      # Creating a Variable to Check The Active State of Widget
for i in range(len(food)):
     myradiobuttons = Radiobutton(myWindow, 
                                  text=food[i],
                                  variable=y,
                                  value=i)                                      # Instantiating The RadioButtons
     myradiobuttons.pack()                                                      # Applying on The Window




myWindow.mainloop()                                       # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)