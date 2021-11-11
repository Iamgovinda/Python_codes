class calculator:
    
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def sum(self):
        return self.num1 + self.num2

    def subtract(self):
        if self.num1>self.num2:
            return self.num1-self.num2
        return self.num2-self.num1
    
    def multiply(self):
        return self.num1*self.num2
    
    def divide(self):
        return self.num1/self.num2
    
calculator = calculator(5,10)

print("Sum:" ,calculator.sum())
print("Subtract:" , calculator.subtract())
print("multiply:" , calculator.multiply())
print("divide:" ,  calculator.divide())


