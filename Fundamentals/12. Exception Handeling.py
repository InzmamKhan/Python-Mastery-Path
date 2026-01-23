# Try-Exception is a Fundamental Mechanism for Handeling Errors that may occur during your Programs and Might Disrupt The Normal Flow of Program.

# Exception          :   Raised as an Universal Exception
# IndexError         :   Raised when trying to Access an Index Out of  Sequence.
# KeyError           :   Raised when trying to Access a Value in a DICTIONARY that Dosen't Exist.
# AttributeError     :   Raised when trying to Access an Attribute of an Object that Dosen't Exist.
# TypeError          :   Raised when an Opertaion or a Function is Applied to ab Object of an Inapropriate Type.
# FileNotFoundError  :   Raised when trying to trying to Open a File that Dosen't Exist.
# ZeroDivisionError  :   Raised when trying to Divide a Number with 0.
# ValueError         :   Raised when alue provided is Unacceptable.




try :
     num  = int(input("Enter The Numerator : "))
     deno = int(input("Enter The Denominator : ")) 
     result = num / deno
     print(result)




except ZeroDivisionError as myerror1:
     print(myerror1)
     print("You cant divide by Zero")

except ValueError as myerror2:
     print(myerror2)
     print("Cant divide by a Non - Integer")

except Exception as myerror3:
     print(myerror3)
     print("Something Went Wrong")




finally : # Always Happens
     print("This always Happens")