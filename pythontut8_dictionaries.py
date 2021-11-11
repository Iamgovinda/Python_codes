"""
A simple dictionary!
"""

alien1={'color':'green','points':5}


#accessing values in a dictionary
print(alien1['color'])
print(alien1['points'])

#adding the new key value pairs in the dictionary!

print(alien1)
alien1['x_position']=0
alien1['y_position']=25
print(alien1)

print("\n\n")

#starting with an empty dictionary

alien1={}


alien1['color']='green'
alien1['points']=5

print(alien1)

#modifying the values in a dictionary


alien1={'color':'green'}
print("The alien is of color: ",alien1['color'],".")

alien1={'color':'yellow'}
print("The alien is of color: now is ",alien1['color'],".")


#removing the key:value pairs in dictionary!
print("___________________-------------")
alien1={'color':'green','points':5}
print(alien1)

del alien1['points']
print(alien1)


#looping through the list
#looping through the key:value pair.

users={
    'username':'rannepal',
    'firstname':'rabindra',
    'secondname':'nepal'
}

for key,value in users.items():
    print("\n",key,":",value)


favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'php'
}

for name,language in favorite_languages.items():
    print(name,"'s favorite programming language is ",language,'.')

#to access key name in the dictionary using for loop


for name in favorite_languages.keys():
    print("\n",name)


for value in favorite_languages.values():
    print("\n",value)



friends=['jen','sarah']

for name in favorite_languages.keys():
    print("\n",name,'.')

    if name in friends:
        print("Hi ",name,"you are a very talented {} programmer!".format(favorite_languages[name]))


#looping through a dictionary's keys in order!

for name in sorted(favorite_languages.keys()):
   print(name.title()+",thankyou for taking the poll.") 


#Nesting of the dictionary!

# A list of dictionary!

"""
Lets store the information of different alienns
using one list."""

alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

aliens=[alien_0,alien_1,alien_2]

print("\n\nAlien details:")
print("_____________________________________")
for aliendetail in aliens:
    print(aliendetail)


#lets make the details of the 30 aliens:

aliens=[]

for aleinsno in range(30):
    new_alien={'color':'green','points':aleinsno**2,'speed':'slow'}
    aliens.append(new_alien)

print("\n\n\n____________________________________________________")
for i in aliens[:10]:
    print(i)


print("The total number of alien is "+str(len(aliens)))

#A list in a dictionary........
# Store the information about a pizza being ordered.

pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}

print("\n")
#lets summarize the order

print("You order a " + pizza['crust'] + "-crust pizza " + "with the following toppings: ")

for topping in pizza['toppings']:
    print("\n\t"+ topping)

print("\n\n")
favorite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}    

for name,languages in favorite_languages.items():
    print(name.title() + "'s favorite languages are:")
    
    for language in languages:
        print("\t" + language.title())


#A dictionary in a dictionary
"""
You can nest a dictionary inside another dictionary, but your code can get
complicated quickly when you do. For example, if you have several users
for a website, each with a unique username, you can use the usernames as
the keys in a dictionary. You can then store information about each user by
using a dictionary as the value associated with their username. In the following listing, we store three pieces of information about each user: their
first name, last name, and location. We’ll access this information by looping
through the usernames and the dictionary of information associated with
each username:
"""


users={
    'Bishal': {
        'first':'Bishal',
        'second':'jamkatel',
        'location':'london'
    },

    'Bikash': {
        'first':'bikash',
        'second':'jamkatel',
        'location':'galchhi' 
    }
}

print("\n____________________________________________")
for username,details in users.items():
    print("\nUsername: " + username)
    full_name=details['first'] + " " + details['second']
    location = details['location']

    print("\n Fullname: " + full_name.title())
    print("\n Location: " + location.title())
    print("\n________________________________________")\
        