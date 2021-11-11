text=input("Enter the text: ")

if ("Subscribe this for money" in text):
    flag = True

elif ("Buy Now" in text):
    flag = True

elif ("Click and Earn" in text):
    flag= True
else:
    flag= False

if(flag):
    print("This message is a spam")
else:
    print("This is a genuine message.")    

