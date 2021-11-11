#Using a while loop with lists and dictionaries.
#moving items from one list to another.
"""
Moving Items from One List to Another
Consider a list of newly registered but unverified users of a website. After
we verify these users, how can we move them to a separate list of confirmed
users? One way would be to use a while loop to pull users from the list of
unconfirmed users as we verify them and then add them to a separate list of
confirmed users. Here’s what that code might look like:
"""


#start with users that need to be verified
#and empty the list to hold the confirmed_users
unconfirmed_users=['suntu','pinku','sanu']
confirmed_users=[]

while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\n verified user.")
print("\n__________________________________")
for user in reversed(confirmed_users):
    print("\n",user)

#remove all the 'cat' present in the list pets:
pets=['dog','cat','cat','goat','rabbit','cat','goldfish','cat']

while 'cat' in pets:
    pets.remove('cat')


print(pets)


#Filling a Dictionary with user Input....

responses={}

polling_active=True

while polling_active:
    name=input("\n What is your name: ")
    response=input("Which mountain would you like to climb someday:? ")

    #store the responses in the dictionary:
    responses[name]=response

    #Find out if anyone else is going to take the poll
    repeat=input("Would you like to let another person respond? (yes/no): ")
    if repeat=='no':
        polling_active= False
    else:
        polling_active=True

#find out is complete.show the results.
print("\n____poll___result____")
for name,response in responses.items():
    print(name + "would like to climb " + response +".")

print(responses)