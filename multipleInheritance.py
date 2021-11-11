class A:

    def feature1(self):
        print("Feature 1 working.")

    def feature2(self):
        print("Feature 2 working.")

#let me create another feature too.

class B:   #class B is subclass/childclass which is inheriting all the methods from class A as well.NOw class B can have all the features of method A.

    def feature3(self):
        print("Feature 3 working.")

    def feature4(self):
        print("Feature 4 working.")

class D:
    def feature6():
        print("Feature 6 working.")

class C(A,B,D):
    def feature5():
        print("Feature 5 working.")

c1 = C()
c1.
