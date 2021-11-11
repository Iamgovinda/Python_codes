class computer:

    def __init__(self,cpu,ram): #this is the init method which is called automatically for each objects.
        self.cpu=cpu                 #this is basically the attributes
        self.ram=ram
        
    def config(self):                    #this is basically the behaviour.
        print(f'{self.cpu},{self.ram}')


com1=computer('i5',16)
com2=computer('rygen 3',64)

com1.config()
com2.config()