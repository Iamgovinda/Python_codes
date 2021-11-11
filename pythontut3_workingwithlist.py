#working with the list,.
#firstly lets looping with the list.

#lets make a list of frns.
frns=["Rabindra","Sushil","Netes","Aswin","Alish"]

#printing all the memeber of the friend list.

for frn in frns:
    print(f"Hello dear {frn.title()} how are you?")

print("\nThank you")


#lets make the list of the numerical list with the help of range() function.

numbers=list(range(1,6))
print("\nnumbers: ",numbers)

#lets make the list of the even numbers

evennumbers=list(range(2,11,2))

print("\n\nEvennumbers: ",evennumbers)


#lets make the list of the square numbers using the loop and range function..

sqaure=[]
for i in range(0,6):
    sqaure.insert(i,i**2)
    #or square.append(i**2)

print("\n\nSquare number: ",sqaure)    

#simple statistics with the help of list functions.

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print("\n\nList of Numbers: ",digits)
print("\n\nMin number: ",min(digits))

print("\n\nMax number: ",max(digits))

print("\n\nSum of elements: ",sum(digits))


#this is the list comprehensions:
#lets make the list of the cube number using the list comprehension

cubes=[value**3 for value in range(1,11)]
print("\n\nCube number using LC: ",cubes)