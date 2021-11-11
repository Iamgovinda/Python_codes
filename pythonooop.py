# Online Python compiler (interpreter) to run Python online.
class vol:
    
    def __init__(self,height,width):
        self.h=height
        self.w=width
        
    def calcvol(self):
        return self.h*self.w
        

a=int(input())
b=int(input())

obj=vol(a,b)
print(obj.calcvol())

