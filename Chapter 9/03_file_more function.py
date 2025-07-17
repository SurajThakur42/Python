f = open("file.txt","r")
data = f.readlines()
print(data,type(data))
f.close()

f = open("file.txt")
data1 = f.readline()
data2 = f.readline()
print(data1,data2)
f.close()

