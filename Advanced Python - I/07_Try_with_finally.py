# try:
#     a = int(input("Enter the number : "))
#     b= int(input("Enter the number : "))
#     print(a/b)

# except Exception as e:
#     print(e)

# finally:
#     print("I am inside finally")


#we can use print without finally then what is the work of finally 
#the work of finally is that in a fonction when we return the value the print not executed but finally executed

def main():
    try:
        a = int(input("Enter the number : "))
        b= int(input("Enter the number : "))
        print(a/b)

    except Exception as e:
        print(e)

    finally:
        print("I am inside finally")

main()



