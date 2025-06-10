
class Grandparent:
    def show_role(self):
        print("I am the Grandparent.")


class Parent(Grandparent):
    def show_role(self):
        print("I am the Parent.")


class Child(Parent):
    def show_role(self):
        print("I am the Child.")


gen = Child()


gen.show_role()          
super(Child, gen).show_role() 
super(Parent, gen).show_role()
