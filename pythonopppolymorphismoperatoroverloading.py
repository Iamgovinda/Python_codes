
a=2
b=3

print(a+b)  #when we write this something is being called behind the seen.....
#here in the int class there's the method of __add__ which takes two parametre.

"""
when we write some operator inside two literals,behind the seen, something is being called which is
called a operator magic method.
for +->__add__()
for '-'->__sub__()
for * ->__mul__()
for / ->__divide__()

"""

print(int.__add__(a,b))