
#write a class of calculator capable of finding square,cube and the squareroot.

from math import *
class calculator:

    def __init__(self,num):
        self.number=num

    def square(self):
        return self.number*self.number

    def cube(self):
        return self.number**3

    def squareroot(self):
        return sqrt(self.number)
    
calc1=calculator(9)

print(calc1.cube())
print(calc1.square())
print(calc1.squareroot())