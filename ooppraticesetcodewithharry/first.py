#create a class where you can store the information of the programmers working at microsoft.


class programmer:
    company="Microsoft"

    def __init__(self,name,product):
        self.name=name
        self.product=product
    
    def getinfo(self):
        print(f"The name of the programmer is {self.name} and He works at {self.product} of company {self.company} ! ")
    

Netesh=programmer("Netesh","Github")
Karan=programmer("Karan","Teams")

Netesh.getinfo()
Karan.getinfo()
    