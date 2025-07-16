a = int (input("Enter number you want to check that it is prime or not : "))

for i in range(2,a):
    if (a%i) == 0:
        print ("This number is not a prime number.")
        break

else :
    print ("This number is a prime number.")



  
