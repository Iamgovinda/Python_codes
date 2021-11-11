#python oop is the object oriented programming, means we create class and based on that class another object or instances are created.
class computer:

    def __init__(self,ram,cpu):
        self.ram=ram
        self.cpu=cpu
        print("computer called")
    
    def printinfo(self):
        print("Ram is {} amd cpu is {}.".format(self.ram,self.cpu))

comp1=computer(8,"Rygen")
comp2=computer(16,"intel")

comp1.printinfo()
comp2.printinfo()

print(id(comp2))