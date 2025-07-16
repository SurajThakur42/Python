def fun():
    a = int(input("Enter First number : "))
    b = int(input("Enter Second number : "))
    c = int(input("Enter Third number : "))

    if(a<b<c):
        print ("Third number is greatest number.")

    if(a>b>c):
        print ("First number  is the greatest number.")

    if (a<b>c):
        print ("Second number is the greatest.")

    
fun()

   
