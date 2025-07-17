import random

computerno= random.choice(["rock","paper","scissors"])
yourchoiceno  = input("Enter your choice between rock,paper and scissors :")
computer = computerno.lower()
yourchoice = yourchoiceno.lower()

print (f"You choose {yourchoice} and  Computer choose {computer}")
if (computer == yourchoice):
    print("This is a draw")

else:

    if(computer == "rock" and yourchoice == "paper"):
        print ("You win Win!")

    elif(computer == "rock" and yourchoice == "scissors"):
        print ("Computer  Win!")

    elif(computer == "paper" and yourchoice == "rock"):
        print ("Computer Win!")

    elif(computer == "paper" and yourchoice == "scissors"):
        print ("You Win!")

    elif(computer == "scissors" and yourchoice == "rock"):
        print ("You Win!")

    elif(computer == "scissors" and yourchoice == "paper"):
        print ("Computer Win!")


    else :
        print ("Sorry,Something went wrong.")
