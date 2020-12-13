def getdate():
    import datetime
    return datetime.datetime.now()

def reader():
    choicename=int(input("Press 1 for Harry\nPress 2 for Rohan\nPress 3 for Hammid\n"))
    if(choicename==1):
        choicede=int(input("Enter 1 to retrieve Harry's diet plan\nEnter 2 to retrieve Harry's Exercise plan\n"))
        if(choicede==1):
            f=open("Harry(diet).txt")
            content=f.read()
            if(content):
             print(content)
            else:
                print("Empty")
            f.close()
        elif(choicede==2):
            f = open("Harry(exercise).txt")
            content = f.read()
            if(content):
             print(content)
            else:
                print("Empty\n")
            f.close()
        else:
            print("Invalid input\n")
    if (choicename == 2):
        choicede = int(input("Enter 1 to retrieve Rohan's diet plan\nEnter 2 to retrieve Rohan's Exercise plan\n"))
        if (choicede == 1):
            f = open("Rohan(diet).txt")
            content=f.read()
            if (content):
                print(content)
            else:
                print("Empty\n")
            f.close()
        elif (choicede == 2):
            f = open("Rohan(exercise).txt")
            content = f.read()
            if (content):
                print(content)
            else:
                print("Empty\n")
            f.close()
        else:
            print("Invalid input\n")
    if (choicename == 3):
        choicede = int(input("Enter 1 to retrieve Hammid's diet plan\nEnter 2 to retrieve Hammid's Exercise plan\n"))
        if (choicede == 1):
            f = open("Hammid(diet).txt")
            content = f.read()
            if (content):
                print(content)
            else:
                print("Empty\n")
            f.close()
        elif (choicede == 2):
            f = open("Hammid(exercise).txt")
            content = f.read()
            if (content):
                print(content)
            else:
                print("Empty\n")
            f.close()
        else:
            print("Invalid input\n")
def  writer():
    choicename=int(input("Enter 1 for Harry\nEnter 2 for Rohan\nEnter 3 for Hammad\n"))
    if(choicename==1):
        choicede=int(input("Press 1 for logging into Harry's Diet\nPress 2 for logging into Harry's Exercise\n"))
        if(choicede==1):
            f=open("Harry(diet).txt","a")
            t=(getdate()).__str__()
            st=input("Enter your diet please:\n")
            f.write("["+t+"]"+" "+st+"\n")
            f.close()
        elif(choicede==2):
            f=open("Harry(exercise).txt","a")
            t = (getdate()).__str__()
            st= input("Enter your diet please:\n")
            f.write("[" + t + "]" + " " + st + "\n")
            f.close()
        else:
            print("Invalid Input\n")
    if (choicename == 2):
        choicede = int(input("Press 1 for logging into Rohan's Diet\nPress 2 for logging into Rohan's Exercise\n"))
        if (choicede == 1):
            f = open("Rohan(diet).txt", "a")
            t = (getdate()).__str__()
            st = input("Enter your diet please:\n")
            f.write("[" + t + "]" + " " + st + "\n")
            f.close()
        elif (choicede == 2):
            f = open("Rohan(exercise).txt", "a")
            t = (getdate()).__str__()
            str = input("Enter your diet please:\n")
            f.write("[" + t + "]" + " " + str + "\n")
            f.close()
        else:
            print("Invalid Input\n")

    if (choicename == 3):
        choicede = int(input("Press 1 for logging into Hammid's Diet\nPress 2 for logging into Hammid's Exercise\n"))
        if (choicede == 1):
            f = open("Hammid(diet).txt", "a")
            t = getdate().__str__()
            str = input("Enter your diet please:\n")
            f.write("[" + t + "]" + " " + str + "\n")
            f.close()
        elif (choicede == 2):
            f = open("Hammid(exercise).txt", "a")
            t = getdate().__str__()
            str = input("Enter your diet please:\n")
            f.write("[" + t + "]" + " " + str + "\n")
            f.close()
        else:
            print("Invalid Input\n")


while(1):
 desire=int(input("Press 1 to retrieve\nPress 2 to log\n"))
 if(desire==1):
     reader()
 elif(desire==2):
    writer()
 else:
    print("Invalid Desire\n")
 x=input("Enter y to continue else press n\n")
 if(x =='n'):
     exit(1)

