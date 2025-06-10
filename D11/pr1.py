class Student:


    def __init__(self):
        self.__name = input("Enter Name: ")
        self.__age = int(input("Enter Age: "))
        print()


    def getData(self):
        print(f"Name: {self.__name}, Age: {self.__age}\n")

s1 = Student()
s2 = Student()

s1.getData()
s2.getData()