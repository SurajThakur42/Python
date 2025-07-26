try:
    with(
    open("file 1.txt") as f1,
    open("file 2.txt") as f2,
    open("file 3.txt") as f3,

):
       data1 = f1.read
       data2 = f2.read
       data3 = f3.read

except FileNotFoundError as e:
    print(e)

print("This is not crash yet.")
