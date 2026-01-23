# Text File   :  .txt     .docx      .log
# Binary File :  .mp4     .mov       .png      .jpeg


# r : Read   ( Default )
# w : write
# x : Create and Open for Writing
# a : Appending
# b : Binary Mode
# t : Text Mode
# + : Open a Disk File for Reading & Writing




# To Open The File in a Variable
a = open("C:\\Users\\khani\\OneDrive\\Desktop\\Practice Code\\PYTHON\\File Handeling\\Sample_File_for_FileIO.txt", "r") 

# To Read The Data
data = a.read()
print(type(data))
print(data)

# To Close The File  ( MUST CLOSE AFTER WORK )
a.close()




# To Read The Data Line Wise
b = open("C:\\Users\\khani\\OneDrive\\Desktop\\Practice Code\\PYTHON\\File Handeling\\Source File - FileIO.txt", "r") 
line1 = b.readline()
print(f"This is Line 1 : {line1}")
b.close()




# To Write Data
c = open("C:\\Users\\khani\\OneDrive\\Desktop\\Practice Code\\PYTHON\\File Handeling\\Source File - FileIO.txt", "w") 
newData = input("Enter What You Desire to Write : ")
c.write(newData)
c.close()




# To Write Data
d = open("C:\\Users\\khani\\OneDrive\\Desktop\\Practice Code\\PYTHON\\File Handeling\\Source File - FileIO.txt", "a") 
appendData = input("Enter What You Desire to Append : ")
d.write(appendData)
d.close()