num=int(input("Enter a number: "))

flag=False


if num>1:

    for i in range(2,num):
        if num%i==0:
            flag=True
            break

    if(flag):
        print("{} is not prime number!".format(num))
    else:
        print("{} is prime number".format(num))

else:
    print("Enter the number above 1")

