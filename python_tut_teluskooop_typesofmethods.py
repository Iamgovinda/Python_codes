#in oops the methods are the those functions which acts the behaviour of that particular object.
#There is 3 kinds of methods these are: Instance method, Class Methods, Static Methods.

#lets create the object of student

class student:

    school='Telusko'
    def __init__(self,m1,m2,m3) -> None:
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def average(self):   #This is the instance method and in instance method we have two kind of it they are: accessor and mutator.
        return (self.m1+self.m2+self.m3)/3

    #accessors only help to fetch the value they are getters.
    def getm1(self):
        return self.m1  

    #mutators help to modify the valuses they are setters

    def setm1(self,value):
        self.m1=value

    #and these are the instance variables.

    #now lets create the class method in class method there is one default argument which is 'cls' in place of 'self' in an instance methods.
    @classmethod
    def info(cls):
        return cls.school

    #instance method concerned with the instance variables and class methods are concerned with the class variables but static method has nothing to do with both these variables
    #it takes nothing as the arguments

    @staticmethod
    def stat():
        print("This is the static method.")


s1=student(12,32,34)

print("Before using setter, mark1:  ",s1.getm1(), "Average: ",s1.average()) #using getter here

s1.setm1(30) #setting mark1 = 30

print("After using setter, mark1:  ",s1.getm1(), "Average: ",s1.average())


#lets print the class method by calling it
print(student.info())

#lets print the static method by calling it.
student.stat()