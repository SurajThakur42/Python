Maths = int(input("Enter your marks in maths :"))
Physics = int(input("Enter your marks in Physics : "))
Chemistry = int(input("Enter your marks Chemistry : "))

total_percent = (100)*((Maths + Physics + Chemistry)/300)

if (total_percent>=40 and Maths > 33 and Physics > 33 and Chemistry > 33):
    print ("you have passed", total_percent )

else :
    print ("Try next year", total_percent) 
    if(total_percent > 40):
         print ("You score ore than 40 percent but You are not score 33 in one subject.So you are not pass") 

  
