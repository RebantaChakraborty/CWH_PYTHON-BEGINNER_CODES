def fibiter(pos):
    if(pos==1):
        return 0
    elif (pos==2):
        return 1
    else:
        return fibiter(pos-1)+fibiter(pos-2)
x=int(input("Enter the position\n"))
print("Result:",fibiter(x))