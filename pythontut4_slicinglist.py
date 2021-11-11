"""
Slicing a List
To make a slice, you specify the index of the first and last elements you
want to work with. As with the range() function, Python stops one item
before the second index you specify. To output the first three elements
in a list, you would request indices 0 through 3, which would return elements 0, 1, and 2.
"""

#Example of slice 1:

players=["abd","virat","buttler","maxwell","gayle"]

print("0:3 player: ",players[0:3]) #this will print the players which are in 0,1,2 index of the list.

print(":3 player>> ",players[0:3])

