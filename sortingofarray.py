from array import *

a = array('i',[])

n = int(input("enter no of elements"))

for i in range(n):
    m = int(input("enter integers"))
    a.append(m)

for i in range(n-1):
    if(a[i] > a[i+1]):
        temp = a[i]
        a[i] = a[i+1]
        a[i + 1] = temp

print(a)