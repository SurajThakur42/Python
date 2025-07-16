def sum(n):
    if (n == 1):
        return 1
    return sum(n-1) + n
   
n = int(input("ENter the number : "))
print (f"Sum of natural number is :{sum(n)}")
