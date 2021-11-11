"""
Functions:
These are the block of the code that are designed to do one specific task,
and it is useful for future use...
it provides reuseability and readibility.
"""

#Lets create the function that simmply greet a user.
def greet_user():
    print("Helloworld")


greet_user()


#lets make the function which greets a person which is passed to the function through a function...
#These means passing an information to the user.

def greet_user(name):
    print("Hello dear "+str(name)+".")


greet_user(input("Enter your name: "))


#Now talk about parametre and arguments

"""parameter or the arguments are those informations or the data that is passed to \
    a function which will be used in the fuction as a variable or something else.
"""

#positional argument
#this works as the order of the parameter in the function.

def pet(pettype,petname):
    print("\n I have " + pettype +".")
    print("\n My "+ pettype + "'s name is "+ petname.title()+".")

pet("dog","jungey")

#passing a list to the function.

friends=['Karan','Netes','Manas','Reeya','Junu']

def frn(frrn):
    print(frrn)
    for frnss in frrn:
        print("Helllo " + frnss + ".")

frn(friends)

#Keyword argument

def add(num1,num2):
    print("num1={} \nnum2={} ".format(num1,num2))
    


print(add(4,3))