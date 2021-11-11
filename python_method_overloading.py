from multipledispatch import dispatch

class calculate_sum:

    @dispatch(int, int)
    def sum(num1,num2):
        return num1+num2
    
    @dispatch(int,int,int)
    def sum(num1,num2,num3):
        return num1+num2+num3

    @dispatch(str,str,str)
    def sum(str1,str2,str3):
        return str1+str2+str3

test1=calculate_sum()
sum1=test1.sum(2,3)
sum2=test1.sum(1,2,3)
sum3=test1.sum("Hello ","Python ","TheRighWay!")
print(sum1)
print(sum2)
print(sum3)
