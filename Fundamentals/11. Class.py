# Creating class
class MainGang():
    name = "Anonymous"
    Rno = 00
    branch = "N/A"


    # Creating Constructor
    def __init__(self, name, Rno, branch):
        self.name = name
        self.Rno = Rno
        self.branch = branch
        print("Succesfully Added 1 Person to The Classroom.")
        print("")



    # Creating Functions
    def intro(self):
        print("Name : ", self.name)
        print("Roll Number : ", self.Rno)
        print("Branch : ", self.branch)
        print("")


    # Creating Methods ( They Don't require any Parameter )
    @staticmethod
    def shortintro():
        print("Does it Really Matters ??")
        print("")




# Creating Objects
s1 = MainGang("User1", 15, "Btech")
s2 = MainGang("User2", 25, "Service")
s3 = MainGang("User3", 45, "Bussines")




# Calling Methods / Functions
s1.intro()
s1.shortintro()

s2.intro()
s2.shortintro()

s3.intro()
s3.shortintro()




#Inheritance
class OtherGang(MainGang):
    def __init__(self) -> None:
        pass

s4 = OtherGang()

# Using Properties of Parent class in this Class
s4.intro()
s4.shortintro()