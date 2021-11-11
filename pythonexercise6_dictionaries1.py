"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
"""

from typing import Counter


glossary={'True':1,'False':2,'looping':'reapting','list':'likeatuplebutmutable'}

for word,meaning in glossary.items():
    print("\n",word,":",meaning,".")


"""
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary.
"""

rivers={'nile':'egypt','koshi':'Nepal','amazon':'brazil','hwangho':'china','ganga':'India'}

for river,Country in rivers.items():
    print("\n The "+river.title()+" river runs through "+Country.title()+".")

"""
6-6. Polling: Use the code in favorite_languages.py (page 104).
•	 Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
•	 Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
"""
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
}

names=['jen','sarah']

for name,language in favorite_languages.items():
    if name in names:
        print("\n ",name,"be responding.")
    else:
        print("\n",name,"please welcome to poll")
