requested_items=['mushrooms','tomato','chilly','floor','egg']

for requested_item in requested_items:
    print("Adding ", requested_item, " in the pot!")
print("Finally pizza is ready!")    

#lets suppose we dont have the most required item 'tomato' in the stock
print("\n\n\n\n\n")
for requested_item in requested_items:
    if requested_item=='tomato':
        print("Sorry we are out of the stock for tomato!")
    else:
        print("Adding ",requested_item,"in the pot!")

print("pizza is ready without tomato!")

#checking whether the list is empty or not!

requested_items=[1]

if len(requested_items)==0:
    print("This list is an empty list!")
else:
    print("Length of the list is ",len(requested_items))

#uSING mULTIPLE LIST:
print("\n\n\n")
available_items=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_items=['mushrooms','french fries','extra cheese']

for requested_item in requested_items:
    if requested_item in available_items:
        print("Adding ",requested_item,".")
    else:
        print("Sorry,we dont have",requested_item,".")
