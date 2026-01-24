from tkinter import *




# Creating a WINDOW to Apply The MENUBAR
myWindow = Tk()                                           # Instantiating a Window
myWindow.geometry("300x150")                              # To Resize The Window




# Creating a LABEL
myLabel = Label(myWindow,
                text=" Hello Fellas ",
                font=("Arial", 10, "bold"),
                fg="tan",
                bg="#28221E",
                relief=RAISED,
                padx=10,
                pady=10)                                  # Instantiating a Label
myLabel.pack()                                            # Applying The Label on The Window




myWindow.mainloop()                                       # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)