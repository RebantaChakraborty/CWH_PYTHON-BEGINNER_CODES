choice=(input("Enter the operator(+,-,*,/)"))
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if ((choice=='+') and (a==56 and b==9) or (a==9 and b==56)):
    print("77")
elif((choice=='*') and (a==45 and b==3) or (a==3 and b==45)):
    print("555")
elif((choice=='/') and (a==56 and b==6) ):
    print("4")
elif "*"in choice:
    print(a*b)
elif "+" in choice:
    print(a+b)
elif "/" in choice:
    print(a/b)
else:
    print(a-b)
