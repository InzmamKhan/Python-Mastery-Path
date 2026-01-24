from tkinter import *
from tkinter import ttk
import time



# Creating a WINDOW to Apply The MENUBAR
myWindow = Tk()                                          # Instantiating a Window
myWindow.geometry("300x150")                             # To Resize The Window


cur_prog = 0                                             # Some Work to Get Job Done
def work():
   cur_prog += 10
   mybar['value'] = 10
   myWindow.update_idletasks()



# Creating The Progress Bar
mybar = ttk.Progressbar(myWindow, 
                        length=300,
                        mode='determinate')              # Instantiating an Entry
mybar['value'] = 0                 
mybar.pack()                            

# Creating The Button to Get Job Done
mybutton = Button(myWindow,                              
                  text="Go", 
                  command="work")
mybutton.pack()


myWindow.mainloop()                                       # Displaying The Window ( MOST IMPORTANT TO BE AT LAST)