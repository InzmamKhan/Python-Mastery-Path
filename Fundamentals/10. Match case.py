# Match-Case Statement : It is anAlternative to using many 'elif' Statements.

n = int(input("Enter a Number : "))

match(n):
    case 1:
        print("Correct")
    case _:
        print("Wrong")