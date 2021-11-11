

class rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth

	def area(self):
		return self.length*self.breadth


rec1=rectangle(int(input("Enter the length: ")),int(input("Enter the breadth: ")))
print("Area of rectangle is: ",rec1.area())

