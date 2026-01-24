from tkinter import *



# Creating a Command to Get Specific Job Done
@staticmethod                                       
def myButtonCommand():
    print(f"Greetings")





# Creating a WINDOW to Apply The MENUBAR
myWindow = Tk()                                     # Instantiating a Window
myWindow.geometry("300x150")                        # To Resize The Window




# Creating a Button
myButton1 = Button(myWindow,
                  text="SUBMIT",
                  command=myButtonCommand,
                  font=("Arial", 20, "bold"),
                  fg="tan",
                  bg="black",
                  activeforeground="#CECBC8",
                  activebackground="#28221E",
                  state = ACTIVE,
                  compound=BOTTOM)                   # Instantiating The Button
myButton1.pack()                                     # Displaying on The Window




myWindow.mainloop()                                  # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)