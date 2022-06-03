a = []
n = int(input("enter no of elements in list"))

for i in range(n):
    print("enter number")
    a.append(int(input()))

for i in a:
    if(i > 0):
        pass
    elif(i == 0):
        pass
    else:
        print("negative no present", i)


