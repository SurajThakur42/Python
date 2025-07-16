a =["Harry","Suraj",True,False]

def remove(a,word):
    for items in a:
        a.remove(word)
        return a
    
print (remove(a,True))
