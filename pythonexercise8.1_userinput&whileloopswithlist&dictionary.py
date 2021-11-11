"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
"""

sandwiches=['blacksw','whitesw','yellowsw','diamondsw','chocolatesw']
finished_sandwiches=[]
while sandwiches:
    removed_sandwich=sandwiches.pop()
    print("\n This sandwhich: "+removed_sandwich+" is made.")
    finished_sandwiches.append(removed_sandwich)

print("\n\n________________________________")

for sandwich in finished_sandwiches:
    print("\n"+sandwich+" is made.")

# if 'pastrami' in sandwiches:
#     print("yes")
# else:
#     for i in range(3):
#         sandwiches.append('pastrami')

print(sandwiches)
print(finished_sandwiches)