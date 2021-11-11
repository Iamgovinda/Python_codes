#in oops there's basically the two types of the variables one is instance variable and the other is class or static variable.
class car:
    #we can declare the static variable here so that it could be same for all the objects.
    wheels=4
    def __init__(self) -> None:
        self.mil=10
        self.com='bmw'  #these are the instance variables which are different for different variables. but common variables are static.

c1=car()
c2=car()

c1.mil=8
car.wheels=5 #this will be affected for both the objects c1 and c2.
print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)