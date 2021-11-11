"""
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
•	 If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
•	 Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
"""

usernames=['admin','dipesh','bikash','bishal','netes']

for users in usernames:
    if users=='admin':
        print(" Hello admin,would you like to see a status report?")
    else:
        print("Hello ",users," you are welcome to our website.")




"""Second Question: 
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
•	 If the list is empty, print the message We need to find some users!
•	 Remove all of the usernames from your list, and make sure the correct
message is printed.
"""

#python returns true is any element is present in the list if not it returns false when we pass it through conditional statement!
print("\n\n\n")
usernames=[]

if usernames:
    print("we dont need anymore users in our system!")
else:
    print("We need to find all the users.")

"""
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
•	 Make a list of five or more usernames called current_users.
•	 Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
•	 Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
•	 Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.
"""

current_users=['admin','dipesh','bikash','netes']

new_users=['suntu','pinku','riya','bikash','netes']


for user in new_users:
    if user in current_users:
        print("He ", user, " is also in the current userlist! Enter new username.")


"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
•	 Store the numbers 1 through 9 in a list.
•	 Loop through the list.
•	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.
"""

print("\n\n\n_____________________________________")
numbers=[]

for number in range(1,10):
    numbers.append(number)

for number in numbers:
    if number==1:
        print(str(number)+"st")
    elif number==2:
        print(str(number)+"nd")
    elif number==3:
        print(str(number)+"rd")
    else:
        print(str(number)+"th")
