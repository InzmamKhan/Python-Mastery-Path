from tkinter import colorchooser
 # The Storing Variable will Act as a Tuple for Color's RGB and HexDec value

mycolor = colorchooser.askcolor()
print(mycolor)
print(mycolor[0], " is the RGB Value")
print(mycolor[1], " is the HexDec Value")