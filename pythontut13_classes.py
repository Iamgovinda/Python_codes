"""
Object oriented programming is one of the most effective approches to writing a software.'
In OOP you write a classed that represents real-world things and the 
situations, and you create objects based on these classes.
"""

#creating and using a class
"""
You can model almost anything using classes. Let’s start by writing a simple
class, Dog, that represents a dog—not one dog in particular, but any dog.
What do we know about most pet dogs? Well, they all have a name and age.
We also know that most dogs sit and roll over. Those two pieces of information (name and age) and those two behaviors (sit and roll over) will go
in our Dog class because they’re common to most dogs. This class will tell
Python how to make an object representing a dog. After our class is written,
we’ll use it to make individual instances, each of which represents one specific dog.
Creating the Dog Class
Each instance created from the Dog class will store a name and an age, and
we’ll give each dog the ability to sit() and roll_over():
"""

class Dog():
    """this is the dog class"""
    #firstly a a class is the blueprint of a object.
    #it have attributes that are datas which are stored in the variable.
    #it have behaviour that is methods which are similar to the function and are defined within a class.

    def __init__(self,name,age,height) -> None:
        self.name=name
        self.age=age
        self.height=height

    def sitting(self):
        print(self.name + " is sitting.")
    
    def running(self):
        print(self.name + " is running.")





dog1=Dog('kalu',12,5)
dog2=Dog('Setu',5,7)


print(f"Name of dog1 is {dog1.name}")
print(f"Age of dog1 is {dog1.age}")
print(f"height of the dog1 is {dog1.height} feet.")
print("Its behavior:")
dog1.running()

print("\n\n")
print(f"Name of dog2 is {dog2.name}")
print(f"Age of dog2 is {dog2.age}")
print(f"height of the dog2 is {dog2.height} feet.")
print("Its behavior: ")
dog2.sitting()
