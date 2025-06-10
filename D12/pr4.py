# Base class
class Animal:
    def sound(self):
        print("Animals make different sounds.")

# First child class
class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof! Woof!")

# Second child class
class Cat(Animal):
    def meow(self):
        print("Cat meows: Meow! Meow!")

# Create objects
d = Dog()
c = Cat()

# Call methods
d.sound()   # Inherited from Animal
d.bark()    # Dog's own method

c.sound()   # Inherited from Animal
c.meow()    # Cat's own method
