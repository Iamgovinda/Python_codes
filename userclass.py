class Users():

    def __init__(self,first_name,last_name,age,address):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.address=address

    def describe_user(self):
        print(f"Hello there my name is {self.first_name} {self.last_name}. I am {self.age} years old. \n My address is {self.address}.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, Welcome to our system.")


user1=Users(first_name=input("Enter first name1: "),last_name=input("Enter the second name1: "),age=int(input("Enter your Age1: ")),address=input("Enter your address1: "))
print("\n\n")
user2=Users(first_name=input("Enter first name2: "),last_name=input("Enter the second name2: "),age=int(input("Enter your Age2: ")),address=input("Enter your address2: "))


user1.describe_user()
user1.greet_user

print("\n\n\n")

user2.describe_user()
user2.greet_user