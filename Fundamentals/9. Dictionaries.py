# Dictionaries are UNORDERED, MUTABLE, conlcuded within {}, and WONT allow DUPLICATES



# Syntax
MyDict = { "Name":"Taha",
           "Age":18,
           "Committed":False,
           "Talent":("Coding", "Baskteball"),
           "Likings":["Sketch", "Movies", "CODM"]    }




# To Print
print(MyDict)               # Whole Dictionary
print(type(MyDict))         # Data Type
print(MyDict["Committed"])  # Any Specific VALUE using KEY




# To Change Value
key = input("Enter The Key to be Updated : ")
val = input("Enter The Updating Value : ")
MyDict[key] = val
print("Printing the Updated Dictionary : ", MyDict)




# To Add Key Value Pairs
newKey = input("Enter The New Key : ")
newVal = input("Enter The It's Value : ")
MyDict[newKey] = newVal
print("Updated Dictionary : " , MyDict)




# Extracting Data
print("Printing all Keys : ")
MyKeys = MyDict.keys()
print(MyKeys)

print("Printing all Value : ")
MyVals = MyDict.values()
print(MyVals)







# Type Converison ( TO LIST )
MyDictToList = list(MyDict.values())
print(MyDictToList)
print(type(MyDictToList))
