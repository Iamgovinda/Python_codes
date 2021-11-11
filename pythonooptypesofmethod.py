"""There are three kinds of methods:
1.class method:def methodname(cls keyword) for class method and use the decorator @classmethod also works with class variable 
2.instance method:accessor and mutators>>>>def methodname(self keyword): for instance method. works with instance method.
3.static method: The kind of method which has nothing to do with class and instance varibales that is called static method.
it is declared using the special decorator here as well: i.e,@staticmethod
"""

class student:

    college="sparkcollege"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def accessor(self):
        return self.m1,self.m2,self.m3
    
    def mutator(self):
        self.m1=20
        self.m2=30
        self.m3=40

    def average(self):                  #working with self means instance method also working with the instance varibales
        return (self.m1+self.m2+self.m3)/3

    #there are two types of instance methods these are: mutator and accessor
    @classmethod
    def collegename(cls):  #This method is working with classvarible with cls keyword so, it is class method.
        return ("My college name is ",cls.college)
    
    @staticmethod
    def info():
        print("This is to inform all you guys that i've nothing to do with any kind of varibales.so i'm chill.")

    


std1=student(12,32,123)
std2=student(122,3,23)

print("all the marks are: ",std1.m1,std1.m2,std1.m3, " also the average is ",std1.average())
print("all the marks are: ",std2.m1,std2.m2,std2.m3, " also the average is ",std2.average())

print(student.collegename())

