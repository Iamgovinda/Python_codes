

def greetings(users):
    for user in users:
        print("Hello {} how are you?\n".format(user.title()))

usernames=["Bikash","Bishal","Dipesh"]  

greetings(usernames)