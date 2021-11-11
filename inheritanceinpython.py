"""
Inheritance in nepali: "उत्तराधिकारी" This means the inherit child of a parent.....
it is the process of accessing or inheriting the class by the child class from parent one.
"""

class A:

    def feature1(self):
        print("Feature1 working.")
    
    def feature2(self):
        print("Feature2 working.")

class B:
    
    def feature3(self):
        print("Feature3 working.")
    
    def feature4(self):
        print("Feature4 working.")

class C(A,B):

    def feature5(self):
        print("Feature5 working")
    
    def feature6(self):
        print("Feature6 working.")


obj=A()
obj.feature1()
obj.feature2()

