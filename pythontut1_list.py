"""
What is list??

________________________________________________________________________________
A list is a collection of items in a particular order. You can make a list that
includes the letters of the alphabet, the digits from 0–9, or the names of
all the people in your family.
_______________________________
"""

bicycles=['Honda','Hero','pulser','suzuki','discover']
#this is the list of the bicycles

print("this is the list of the biycles: {}".format(bicycles))

#this above line of the code is used to print the elements of the list using the format function.

"""Now how the Access the elements in the list this 
is done directly using slicing of the list"""

print("The first element of the list is ",bicycles[0],".")#prints the first element

print("The last element of the list is ",bicycles[-1],".")#prints last elements.

#printing the element in the proper order using the title function.

print("This word is written properly: {}".format(bicycles[2].title()))

#key point: the list positions starts from 0 not from 1.

#Python has a special syntax for accessing the last element in a list.
#  By asking for the item at index -1, Python always returns the last item in the list:
print("The last element of the list is ",bicycles[-1],".")#prints last elements.


