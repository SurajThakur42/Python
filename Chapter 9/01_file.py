f = open("file.txt")  # f = open("file.txt","r") r is default in open function.
                      # for write in a file use ("filename","w")
data = f.read()
print (data)
f.close()

