a = []
n = int(input("enter no of elements in list"))

for i in range(n):
    print("enter number")
    a.append(int(input()))

x = int(input("enter number to be search"))

for i in a:
    if(i==x):
        print("number present")
        break
else:
    print("number not present")
