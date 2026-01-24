from tkinter import *




# Creating a WINDOW to Apply The MENUBAR
myWindow = Tk()                                                                 # Instantiating a Window
myWindow.geometry("300x150")                                                    # To Resize The Window




# Creating a List Box
mylistBox = Listbox(myWindow,                                                   # Instantiating The List Box
                    font=("Arial", 20, "bold"),
                     fg="tan",
                     bg="black",
                     selectmode=MULTIPLE)
mylistBox.config(height=mylistBox.size())                                       # Adjusting Height According to Options
mylistBox.config(width=mylistBox.size())                                        # Adjusting Width According to Options
mylistBox.pack()                                                                
mylistBox.insert(1, " Pizza ")                                                  # Adding Options
mylistBox.insert(2, " Burger ")                                                 # Adding Options
mylistBox.insert(3, " Ice Cream ")                                                 # Adding Options
mylistBox.insert(4, " Biryani ")                                                # Adding Options
mylistBox.insert(mylistBox.size(), " Roasted ")                                 # Adding Options of Your Choice

mylistBox.delete(3)                                                             # Deleting Options

# mylistbox.get(mylistbox.curselection())                                       To get Current Selection




myWindow.mainloop()                                                             # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)