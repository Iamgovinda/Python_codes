
#create a sample class lets say A with classattribute then create The sample object obj and set obj.classattribute=0 then check if the value of class attribute inside the class changes ???
#The simple answer is obviously not

class A:
    classattribute=5

obj=A()
obj.classattribute=7

print(obj.classattribute)
print(A.classattribute)


#to change the classattribute you have to follow following
#classname.classattributename=othervalue

A.classattribute=8

print(A.classattribute)