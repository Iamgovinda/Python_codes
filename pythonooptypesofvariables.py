"""There are 2 kinds of variables:
1. Class variable/static variable:The variable which is commmon to all the methods inside a class but outside the __init__method is called class variable.
2. Instance variable: The variable which is different for different object you create inside the constructor is called instance variable.

"""

class student:

    college="spark college"

    def __init__(self):
        self.name="Riya"
        self.age=19

std1=student()
std2=student()

std1.age=20
std1.name="Netes"

print(std1.name,std1.age,std1.college)
print(std2.name,std2.age,std2.college)






    
