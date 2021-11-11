#inheritence is the process of using the methods of existing class.


class A:

    def __init__(self) -> None:
        print("In init A.")

    def feature1(self):
        print("Feature 1 working.")

    def feature2(self):
        print("Feature 2 working.")

#let me create another feature too.

class B(A):   #class B is subclass/childclass which is inheriting all the methods from class A as well.NOw class B can have all the features of method A.

    def __init__(self) -> None:

        #using the special method both the constructor will be called.

        super().__init__()
        print("In init B.")


    def feature3(self):
        print("Feature 3 working.")

    def feature4(self):
        print("Feature 4 working.")


a1=B()  #that means when there is no constructor in B and it is inheriting A then constructor of A will be called also if B has its own constructor then it will call only of B.

print("\n\n\n")
class c1:
    def __init__(self) -> None:
        print("In init c1.")


class c2:
    def __init__(self) -> None:
        print("In init c2.")

class c3(c1,c2): #multiple inheritence here........concept of MRO method resolution order>>go left from right.
    def __init__(self) -> None:
        super().__init__()
        print("In init c3.")


c=c3()
