
class A:
    def __init__(self):
        self.__a = 2
class B(A):
    def __init__(self):
         
        A.__init__(self)
        print("Getting protected member of class A from Subclass B: ")
        print(self.__a)
    
obj2 = A()
obj1 = B()
 
print(obj2.a)