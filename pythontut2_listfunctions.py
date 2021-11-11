"""
Changing, Adding, and Removing Elements
____________________________________________
Most lists you create will be dynamic, meaning you’ll build a list and
then add and remove elements from it as your program runs its course. For
example, you might create a game in which a player has to shoot aliens out
of the sky. You could store the initial set of aliens in a list and then remove
an alien from the list each time one is shot down. Each time a new alien
appears on the screen, you add it to the list. Your list of aliens will decrease
and increase in length throughout the course of the game. 
"""


#Simply lets make the list of the bicycles
bicycles=['Honda','Hero','pulser','suzuki','discover']
#this is the list of the bicycles

temp=bicycles
print("Temporary list: ",temp)

#then lets change  the first element "Honda" with the "Ducati".

bicycles[0]="Ducati"
print("The new list of the bikes after modification: ",bicycles)

#modyfying the values of the listL:

#1. Adding element to the end of the list: that is APPEND function

print("Before appending:\n ",bicycles,"\n")

bicycles.append("Yamaha")

print("After appending yamaha: ",bicycles)

#2. Inserting the element to the list

#we can insert the element in the required index as we want.

#for example.

car=["suzuki","toyota","maruti"]

#lets suppose we want to insert tesla car in index number 1.

car.insert(1,"Tesla")

print("\n\nAfter inserting the element in the carlist: ",car);


# now removing the element from the list:

#A. Using the del statement: this statement is used to delete the element
#from the list from the exact position of the list.
#this statement is useful if you know the index of thee element which you want to delete,

#for example: 

food=["momo","sausage","meat","chaumin"]

del food[1] #this instruction will delete the 2nd element from the foodlist

print("After the deletion of 2nd element: ",food)

#B. Using pop() Method.
#this method is useful when we want to use the element which is just deleted from the list.
#this method will remove the last element of the list and returns the value of removed element.


#for example:
motorcycles = ['honda', 'yamaha', 'suzuki']
print("motorcycles: ",motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print("popped_motorcycle: ",popped_motorcycle)

#popping the elements of the list from the any position of the list.
#we can pass the element's index as an argument to the pop() method to remove element from the any position of the list.

motorcycles = ['honda', 'yamaha', 'suzuki'] 

# lets pop the second element of the list:

secondelement=motorcycles.pop(1)
print(f"\n\n{secondelement} is the second element of the list which is just removed from the list")


#Removing an item by value using remove function.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print("After removing ducati from the list: ",motorcycles)

