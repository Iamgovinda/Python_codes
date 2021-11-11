"""
Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
•	 Use a for loop to print each food the restaurant offers.
•	 Try to modify one of the items, and make sure that Python rejects the
        change.
•	 The restaurant changes its menu, replacing two of the items with different
    foods. Add a block of code that rewrites the tuple, and then use a for
    loop to print each of the items on the revised menu.
"""

Buffet=('Chatpatey','Panipuri','Laughing','Chaup','Pakauda')

for food in Buffet:
    print(food)


#Buffet[0]='Roti'>>>>>>This code is rejected by the python interpreter.

Buffet=('Chatpatey','Panipuri','Laughing','Chap','Pakaud')
print("This tuple is after the little modification: ",Buffet)