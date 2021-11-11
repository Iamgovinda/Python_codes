"""If a object of a class has another object to be explained for eg, if a student object have laptop class object we can
use the inner class to write the code beautifully.
"""
class student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    
    def show(self):
        print(self.name,self.rollno)

    class laptop:
        def __init__(self):
            self.name="HP"
            self.ram="8 GB"
            self.cpu="intel"
        
        def show(self):
            print(self.name,self.ram,self.cpu)


std1=student("Ram",1)
std2=student("Sita",0)
std1.show(),std1.lap.show()
print("\n")
std2.show(),std2.lap.show()




