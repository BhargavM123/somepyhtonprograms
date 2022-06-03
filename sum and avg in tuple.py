b = []
n = int(input("enter the number of inputs"))

for i in range(n):
    b.append(int(input("enter number")))
b =tuple(b)
             
s = sum(b)

avg = s/len(b)

print(b)             
print("the sum of numbers is ", s)
print("the avg of numbers is ", avg)             
             
