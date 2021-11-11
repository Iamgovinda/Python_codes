#A example that defines inheritence : parent house is my house as well also parent phone will be my phone as well..
#lets create the simple class which is class A

#Inheritance concept gives the feature to access the method of another class from one class.


class A:

    def feature1(self):
        print("Feature 1 working.")

    def feature2(self):
        print("Feature 2 working.")

#let me create another feature too.

class B(A):   #class B is subclass/childclass which is inheriting all the methods from class A as well.NOw class B can have all the features of method A.

    def feature3(self):
        print("Feature 3 working.")

    def feature4(self):
        print("Feature 4 working.")

#you can also have the multilevel inheritance//........as well

class C(B):
    
    def feature5(self):
        print("Feature 5 is working.")

class D:

    def feature6(self):
        print("feature 6 is working")


class F(A,D): #class F is inheriting method from the two classes they are A and D simultaneously which is called multiple inheritence.
    def feature7(self):
        print("Feature 7 working.")


a1=A()

a1.feature1()
a1.feature2()

b1=B()

c1=C()
c1.feature1 #/2/3/4/5   that is we can take the method of to class A to class C through class B.that is multilevel inheritance.

#Inheritance is the process of inheriting the methods to one class to another class. While defining class >>class defineclass(inheritingclass):
f1=F()
