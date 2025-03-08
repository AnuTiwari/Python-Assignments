class Parent:
    def func1(self):
        print("Function in Parent class.")

class Child(Parent):  # Single Inheritance
    def func2(self):
        print("Function in Child class.")

class GrandChild(Child):  # Multilevel Inheritance
    def func3(self):
        print("Function in GrandChild class.")

class MultipleA:
    def funcA(self):
        print("Function in MultipleA class.")

class MultipleB:
    def funcB(self):
        print("Function in MultipleB class.")

class MultipleC(MultipleA, MultipleB):  # Multiple Inheritance
    def funcC(self):
        print("Function in MultipleC class.")

# Testing
obj1 = GrandChild()
obj1.func1()
obj1.func2()
obj1.func3()

obj2 = MultipleC()
obj2.funcA()
obj2.funcB()
obj2.funcC()
