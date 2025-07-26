try:
    a = int(input("Enter the number : "))
    b= int(input("Enter the number : "))
    print(a/b)

except Exception as e:
    print(e)

else:
    print("I am inside else")

