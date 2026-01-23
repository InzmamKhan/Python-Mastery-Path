# Tuples are ORDERED, IMMUTABLE, conlcuded within (), and ALLOWS DUPLICATES



# Syntax for Assigning by Self
MyTuple = ("Hello",
           25,
           10.5,
           True,
           10.5 )




# To Print Complete list
print(MyTuple)          # To Print Complete list
print(type(MyTuple))    # To print Data Type




# To find Index of a Given Value
val = int(input("Enter The Value to Find Index of : "))
index = MyTuple.index(val)
print(index)




# To count the Number of Occurence of a Given Value
va = float(input("Enter a Number to Find the Number of Occurence of : "))
count = MyTuple.count(va)
print(count)