f = open("myfile.txt")
data = f.read()
print(data)
f.close 

# same thing we can write in different way:

with open("myfile.txt") as f:
    data = f.read()
    print (data)

#you don't have to close the file
