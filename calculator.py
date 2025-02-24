import math
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second nmber:"))
print("1.ADDITION")
print("2.SUBSTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.MODULO DIVISION")
print("6.POWER")
print("7.FACTORIAL")
print("8.EXIT")
choice=int(input("Enter the choice:"))
if choice==1:
    result=num1+num2
    print("Result:",result)
elif choice==2:
    result=num1-num2
    print("Result:",result)
elif choice==3:
    result=num1*num2
    print("Result:",result)
elif choice==4:
    result=num1/num2
    print("Result:",result)
elif choice==5:
    result=num1%num2
    print("Result:",result)
elif choice==6:
    result==num1**num2
    print("Result:",result)
elif choice==7:
    result=math.factorial(num1)
    print("Result:",result)
else:
    print("Wrong choice")
