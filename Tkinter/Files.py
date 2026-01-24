from tkinter import filedialog

# To Open File

filepath = filedialog.askopenfilename(initialdir = "SOME PATH",
                                        title ="OPEN THE FILE XYZ",
                                        filetypes= (  ("TextFIles", "*.txt"), ("all Files", "*.*")  )


# To Save File
file = filedialog.asksavefileas(initaldir = "SOME PATH",
                                defaultextention = ".txt",
                                filetypes= (  ("TextFIles", "*.txt"), ("all Files", "*.*")  )
filetext = str(entry.get(1.0, END))
file.write(filetext)
file.close()