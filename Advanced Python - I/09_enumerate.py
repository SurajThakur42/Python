l = [4,5,3,2,5]

# index = -1
# for i in l:
#     index += 1
#     print(f"This {i} is present on {index} index")

#This can be done in more easy way by enumerate

for index,item in enumerate(l):
    print(f"This {item} is present on {index} index")
