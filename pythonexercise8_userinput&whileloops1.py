"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""

flag=True

while flag:
    pizza_toppings=input("Enter the pizza topping: To exit enter 'quit': ")
    if pizza_toppings=='quit':
        flag=False
    else:
        print("You will add " + pizza_toppings + " to the pizza!")


"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""

while True:
    age=input("Enter the age: and enter 'quit' to exit: ")
    if str(age)=='quit':
        break
    else:
        if int(age)<3:
            print("You will charge $3.")
        elif int(age)>=3 and int(age)<=12:
            print("You will charge $10.")
        else:
            print("YOu'll charge $15.")

"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
•	 Use a conditional test in the while statement to stop the loop.
•	 Use an active variable to control how long the loop runs.
•	 Use a break statement to exit the loop when the user enters a 'quit' value
"""
