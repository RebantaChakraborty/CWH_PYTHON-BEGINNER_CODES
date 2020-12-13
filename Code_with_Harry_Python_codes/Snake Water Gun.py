import  random
complist=["snake","water","gun"]
comp_count=0
user_count=0
print("The game begins!")
n=int(input("How many best of rounds do you want?\n"))


i=0

while(i!=n):
    compchoice = random.choice(complist)
    user_choice = input("Enter your choice(snake,water or gun)\n")
    user_choice = user_choice.lower()
    if(compchoice == "snake" and user_choice == "water"):#computer choice = snake only
        comp_count+=1
        print("comuter's choice:%s,You lose this round"%(compchoice))
    elif(compchoice == "snake" and user_choice == "gun"):
        user_count+=1
        print("comuter's choice:%s,You win this round" % (compchoice))
    elif(compchoice == "water" and user_choice == "gun"):#computer choice=water only
        comp_count=+1
        print("comuter's choice:%s,You lose this round" % (compchoice))
    elif(compchoice == "water" and user_choice == "snake"):
        user_count+=1
        print("comuter's choice:%s,You win this round" % (compchoice))
    elif(compchoice == "gun" and user_choice == "snake"):#computer choice=gun only
        comp_count+=1
        print("comuter's choice:%s,You lose this round" % (compchoice))
    elif(compchoice == "gun" and user_choice == "water"):
        user_count+=1
        print("comuter's choice:%s,You win this round" % (compchoice))
    else:
        print("Round drawn")
    i+=1
if(user_count>comp_count):
    print("You win !Congratulations")
    print(f"Rounds won by computer (out of {n}):",comp_count)
    print(f"Rounds won by you (out of {n}):",user_count)
    print("Rounds drawn:",n-(user_count+comp_count))
elif(user_count<comp_count):
    print("You lost!Better luck next time")
    print(f"Rounds won by computer (out of {n}):", comp_count)
    print(f"Rounds won by you (out of {n}):", user_count)
    print("Rounds drawn:", n - (user_count + comp_count))
else:
    print("It is a draw")
    print(f"Rounds won by computer (out of {n}):", comp_count)
    print(f"Rounds won by you (out of {n}):", user_count)

