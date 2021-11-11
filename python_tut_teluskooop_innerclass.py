class student:

    def __init__(self,name,rollno) -> None:
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()


    #Yess we can create a class inside a class........

    class laptop:

        def __init__(self) -> None:
            self.brand='Hp'
            self.ram='8GB'

        #lets create the show method for laptop as well

        def show(self):
            print(self.brand,self.ram)


s1=student('Gobinda',1)
s2=student('Ram',3)


#also you can create the object of inner class inside the outer class or outside the outer class provided you use outer class to call it.

lap1=student.laptop()

# lap1=s1.lap
# lap2=s2.lap


s1.show()
s2.show()