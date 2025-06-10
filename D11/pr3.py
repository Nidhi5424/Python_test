class MyClass:

    def __init__(self, name):
        self.name = name
        print(self.name, "object created")
        

    def __del__(self):
        print(self.name, "object deleted")
   
   
s1 = MyClass("A")
s2 = MyClass("B")
s3 = MyClass("C")
