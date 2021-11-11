#introducing the while loops
"""
The for loop takes a collection of items and executes a block of code once
for each item in the collection. In contrast, the while loop runs as long as,
or while, a certain condition is true. 
"""

#printing the number till 5 using for loop

current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1

#another example.......

prompt="\ntell me something and i will repeat it back to you: "
prompt+="\nEnter 'quit' to end the program." 

message=""
while message!='quit':
    message=input(prompt)
    print("\n",message)

#using some flag pointer

active=True
while active:
    message=input("Enter something & Enter 'quit' to exit: ")
    if message=='quit':
        active=False
    else:
        print(message)    


#Using break to exit a loop

while True:
    city=input("Enter a city you have visited, Enter 'quit' to exit: ")
    if city=='quit':
        break
    else:
        print("I'd love to go to "+ city.title()+"!")

#Using continue in a loop
current_number=0
#lets print odd number 1 to 10.

while current_number<10:
    current_number+=1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)