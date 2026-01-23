# Lists are ORDERED, MUTABLE, conlcuded within [], and allows DUPLICATES



# Syntax for Assigning by Self
MyList = ["Taha",
          18,
          5.10,
          True   ]




# Print 
print(type(MyList)) # To print Data Type
print(MyList)       # To Print Complete List




# Slicing ( Prints or Stores Elements within a Range )
m  = int(input("Give Lower Range for Slicing : "))
n  = int(input("Give Upper Range for Slicing : "))
a=MyList[m:n]
print(a)




# To add another Element
element_1 = input("Enter First Element to be Added : ")
MyList.append(element_1)
print(MyList)

element_2 =  input("Enter Second Element to be Added at Specific Position : ")
position = int(input("Enter the Index : "))
MyList.insert(position, element_2)
print(MyList)




# To Remove Element
rem = input("Enter The Element Whose First Occurence needs to be Removed : ")
MyList.remove(rem)
print("Removing The First Occurence of The Inputted Number : ", MyList)

remo = int(input("Enter The Index Whose Element needs to be Removed : "))
MyList.pop(remo)
print("Removing The Element using Index : ", MyList)




# To Sort
MyList.sort()
print("My List after Getting Sorted in Ascending Order : ", MyList)

MyList.sort(reverse=True)
print("My List after Getting Sorted in Descending Order : ", MyList)
