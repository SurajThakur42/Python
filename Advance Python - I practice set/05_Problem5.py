n = int(input("Enter the number : "))

table = [n*i for i in range(1,11)]
with open("Tables.txt","a") as f:
    f.write(str(table)+"\n")
