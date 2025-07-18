import random

computerno= random.choice(["snake","water","gun"])
yourchoiceno  = input("Enter your choice between snake,water and gun :")
computer = computerno.lower()
yourchoice = yourchoiceno.lower()

print (f"You choose {yourchoice} and  Computer choose {computer}")
if (computer == yourchoice):
    print("This is a draw")

else:

    if(computer == "snake" and yourchoice == "water"):
        print ("Computer Win!")

    elif(computer == "snake" and yourchoice == "gun"):
        print ("You Win!")

    elif(computer == "water" and yourchoice == "snake"):
        print ("You Win!")

    elif(computer == "water" and yourchoice == "gun"):
        print ("Computer Win!")

    elif(computer == "gun" and yourchoice == "snake"):
        print ("Computer Win!")

    elif(computer == "gun" and yourchoice == "water"):
        print ("You Win!")


    else :
        print ("Sorry,Something went wrong.")

print ("Thanks for playing")
print (" If you want to play more than click on run option")


    

