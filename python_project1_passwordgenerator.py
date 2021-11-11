import string
import random

plen=int(input("Enter the password length you want to generate: "))

s1=string.ascii_letters
#print(s1)

s2=string.digits
s3=string.punctuation

print(s1)
print(s2)
print(s3)

str=[]

l1=str.extend(list(s1))
str.extend(list(s2))
str.extend(list(s3))

random.shuffle(str)
print("Your generated password is: ")
print("".join(str[0:plen]))


