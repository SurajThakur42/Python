import random
Computer_Guessno = random.randint(1,1000)
Computer_Guess = int(Computer_Guessno)

You_Guess = -1
guesses = 0
while (Computer_Guess != You_Guess):
    guesses += 1
    You_Guess = int(input("Enter the number which you guess between 0 to 1000: "))

    if(Computer_Guess < You_Guess):
        print("Lower number please")

    elif(Computer_Guess > You_Guess):
        print("Higher number please")

    else:
        print(f" Number is {Computer_Guess} and you guess {You_Guess}. \n You guess right number.Congratulations! \n You guess the right number in {guesses} attempt.")

