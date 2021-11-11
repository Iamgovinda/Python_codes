"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
"""

"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""

user_0={'first_name':'Bishal','second_name':'jamkatel','age':11,'city':'kathmandu'}
user_1={'first_name':'Bikash','second_name':'jamkatel','age':14,'city':'london'}
user_2={'first_name':'Dipesh','second_name':'pudasaini','age':15,'city':'washington_dc'}

people=[user_0,user_1,user_2]

print("\n________________________________________________")
for user in people:
    for first,second in user.items():
        print(str(first) + ":" + str(second))
    print("_______________________________________________")

"""
6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.
"""

print("_________________________________________\n")
print("Question1>>>>>>>>>>>>>>>>>>>>>>>>>")
cat={'kind':'domestic','owner_name':'bikash'}
horse={'kind':'wild','owner_name':'bishal'}

pets=[cat,horse]

for animal in pets:
    for first,second in animal.items():
        print(first+" : "+second)

    print("\n___________________________________")

print("Question2___________________________")
"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.
"""

favorite_places={
    'Bishal':['london','us','aus'],
    'Bikash':['lumbini','mustang']
}

dipu=[]

for i in range(2):
    favplace=input("Dipesh ,Enter your fav place{}:".format(i+1))
    dipu.append(favplace)

favorite_places['dipesh']=dipu

for name,favplaces in favorite_places.items():
    print("favorite places of "+ str(name) + " are " + str(favplaces) )

"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""
favorite_number={
'Dipesh':[1,2,3],
'dipichhya':[2,3,4],
'Bikash':[4,5,6]
}

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored about it.
"""

cities={
    'kathmandu':{
        'country':'Nepal',
        'population':'1.7 milllion',
        'fact':'city of temple'
    },
    'London':{
        'country':'UK',
        'population':'2.7 million',
        'fact':'famous for themes river.'
    },
    'newyork':{
        'country':'USA',
        'population':'3 million',
        'fact':'F.Capital of USA.'
    }


}

print("\n____________________________________")
for city,details in cities.items():
    print("\nThe information about ",city, "is:\n")
    for cit,det in cities[city].items():
        print(str(cit)+":"+str(det))
    print("_______________________________")
    