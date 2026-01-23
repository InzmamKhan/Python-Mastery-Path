# A Function can be Defined as The Block of Code That Performs A Specific Task.
# Functions provieds Re-usability and Maintainability

n = int(input("Enter a Number "))


# Defining a Function
def reverse(n):
    rev = 0
    while (n > 0):
        rev = (rev * 10) + (n%10)
        n = n/10
    return rev

result_1 = reverse(n)       #This is Known as Calling a Function
print(result_1)







# Lambda Function, These Functions can be Defined as The Small Anonymous Functions that Performs Some Specific Tasks
cube = lambda x: x*x*x
result_2 = cube(n)
print("Printing The Lambda Function (CUBE) of the Entered Number")
print(result_2)






# Recursion can de Defined as The Technique where a Function Calls Itself Again and Agian util The Specific Condition is met.
def fact(n):
    if n==0:
        return 1
    else:
         return fact(n-1) * n

result_3 = fact(n)
print("Printing The Factorial of The Given NUmber using Recursion Technique")
print(result_3)









# *args allows you to Pass Multiple Non-Key Arguments
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4))
print(add(1,2))
print(add(1,2,3,4,5,6,7,8,9))




# **kwargs allows you to Pass Multiple Keyword Arguments
# There are Multiple unpacking operator (*)
# 1. Positional
# 2. Default
# 3. Keyword
# 4. Arbitrary
# This will Always Return as a Dictionary
def about(**kwargs):
    for key, val in kwargs.items():
        print(f"{key} : {val}")

about(Name = "Phoenix",
      Address = "NNP",
      num = "8423XXXXXX")