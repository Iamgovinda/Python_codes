# Question number1: Counting to Twenty: Use a for loop to print the numbers from 1 to 20,inclusive
print("\n\n_______________________________")
for i in range(1,21):
    print(i,"\n")

print("\n\n_______________________________")
# #Quetion number2: One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

#Answer : I will not do this question because this lines of code can lead hanging our laptop.

# Quetion number3:  Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

#i will only do this till 100 numbers.
print("\n\n_________________________________________________")
numbers=[]
for number in range(1,101):
    numbers.append(number)

print("Min of the numberlist: ",min(numbers))

print("\nMax of the numberlist: ",max(numbers))

print("\nSum of the numberlist: ",sum(numbers))

print("\n\n_________________________________")

#Questionnumber3: Use the third argument of the range() function to make a list
#of the odd numbers from 1 to 20. Use a for loop to print each number.
#>>>>>>Solution

oddnumbers=list(range(1,20,2))

print("\nList of the oddnumber: ",oddnumbers)

#Questionnumber 4: Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
#print the numbers in your list.
print("\n\n_________________________________")

threes=list(range(3,31,3))

for factors in threes:
    print("\n ",factors)