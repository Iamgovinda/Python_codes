"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
"""

#solution:

invitees=["Deepesh","Bikash","Bishal"]

for member in invitees:
    print(f"Hello, {member} you are invited for dinner in our house, Thank you.")


"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
•	 Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still
in your list.
"""

invitees=["Deepesh","Bikash","Bishal"]
print("\n Just now it is reported that {} cannot make attend to the dinner so another person is invited.".format(invitees.pop(2)))

invitees.append('Suntu')

print("After changing the list of the invitees {}".format(invitees))

"""
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list.
"""

invitees=["Deepesh","Bikash","Bishal"]
print("\n\nIt is reported that more table is available so more people would be invited.")

invitees.insert(0,"Pinku")
invitees.insert(2,'moti')
invitees.append("swosti")

print("\n\n\nAfter all modification list is: ",invitees)

for member in invitees:
    print(f"This is the final invitation to you {member} for dinner.\n")



# Sorting a list element 
#this method is used to sort the element of the list as per alphabetical order.

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nBefore sorting the list: ",cars)

cars.sort()

print("After sorting the list: ",cars)


number=[2,8,6,9,3,1,0]

print("\n Before sorting the number: ",number)

number.sort()

print("\n After sorting the number: ",number)


#we can use sorted function to sort the elment of the list temporarily.

#
#printing the list in the reverse order.

name=['suntu','pinku','reeya','ram','nitu']
print("Namelist: ",name)

name.reverse()
print("\nReversed list: ",name)

#finding the length of the list.
cars = ['bmw', 'audi', 'toyota', 'subaru']

length=len(cars)

print("Length of the list cars is {}".format(length))
