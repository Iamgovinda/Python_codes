#class is the design or the blueprint of any object with the help of this blueprint we can create many and many objects having same attributes and behaviour.
class computer:

    def __init__(self) -> None:
        self.name='Gobinda'
        self.age=20

    def update(self):
        self.age=40

    def compare(self,other):
        if self.age==other.age:
            return True
        else:   
            return False


    


c1=computer()
c2=computer() #basically this is the constructor which calls the __init__method internally and automatically.

print(c1.name)
print(c2.age)


c2.update()

print(c1.name)
print(c2.age)

#so self keyword is the default argument that points to the calling parameter with the actual arguments.

if c2.compare(c1):
    print("They are same.")