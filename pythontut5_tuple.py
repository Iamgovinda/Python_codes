"""
Defining a Tuple:
A tuple looks just like a list except you use parentheses instead of square 
brackets which is a immutable collection of the different datas.

"""

#an immutable list is called a tuple.
#lets make a tuple:
dimensions=(200,30)

print(dimensions[0])
print(dimensions[1])


print(id(dimensions))
print(id(dimensions[0]))
print(id(dimensions[1]))


#looping through the Tuple.

favfriends=("Bikki","Bishu","Dipu","RkO")

for friends in favfriends:
    print("\n\n",friends,"\n\n")
    

#Writing over a tuple:
""""Although you can’t modify a tuple, you can assign a new value to a variable
that holds a tuple. So if we wanted to change our dimensions, we could
redefine the entire tuple:"""

number=(200,30,30)

print("\nThis is the original list.\n\n")
for num in number:
    print(num)

number=(23,323,223,23)
print("\nThis is modified tuple\n\n")
for num in number:
    print(num)


