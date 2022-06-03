from array import *

a = array('i',[])

n = int(input("enter no of elements"))

for i in range(n):
    m = int(input("enter integers"))
    a.append(m)

b = a[0]
for i in a:
    if( i >= b):
        b = i


print(b)