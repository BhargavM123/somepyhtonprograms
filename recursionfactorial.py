def factrec(a):
    if(a == 0):
        return 1
    else:
        return a * factrec(a-1)

n = int(input("enter number for factorial : "))

r = factrec(n)
print(r)