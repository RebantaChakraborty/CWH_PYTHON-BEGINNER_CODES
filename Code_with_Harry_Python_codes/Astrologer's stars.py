print("Welcome to astrogloger's stars")
a=bool(int(input("Enter 1 for non inverted star else press 0 for inverted star ")))
n=int(input("Enter the number of rows"))

if(a is True):
    for r in range(n):
        for c in range(r+1):
           print("* ",end='')
        print("")
elif (a is False):
   for r in range(n):
       for c in range(n,r,-1):
         print("* ",end='')
       print()
