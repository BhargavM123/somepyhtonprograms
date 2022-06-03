from array import *

a = array('u',[])

n = int(input("enter no of elements"))

for i in range(n):
    m = input("enter character : ")
    a.append(m)


if(input("enter character you want to find : ") in a):
    print("character present")
else:
    print("character not present")