

class Resturant():

    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type

    def describe_resturant(self):
        print(f"The resturant name is {self.resturant_name}")
        print("Welcome to my resturant.")

    def open_resturant(self):
        print("The resturant is open.")

resturant1=Resturant(resturant_name=input("Enter the resturant name1: "),cuisine_type=input("Enter the cuisine type1: "))
resturant2=Resturant(resturant_name=input("Enter the resturant name2: "),cuisine_type=input("\n\nEnter the cuisine type2: "))
resturant3=Resturant(resturant_name=input("Enter the resturant name3: "),cuisine_type=input("\n\nEnter the cuisine type3: "))


print("\n\n\n")
resturant1.describe_resturant()
resturant1.open_resturant()

print("\n\n\n")
resturant2.describe_resturant()
resturant2.open_resturant()

print("\n\n\n")
resturant3.describe_resturant()
resturant3.open_resturant()



