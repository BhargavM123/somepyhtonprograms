from array import *

a = array('i',[])

n = int(input("enter no of subjects"))
tot = int(input("out of marks")) * n

for i in range(n):
    m = int(input("enter marks"))
    a.append(m)

print(a)
sum = 0
for i in a:
    sum = sum + i

print(sum)
print("percentage = ",(sum/tot)*100)