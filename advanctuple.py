a = []
l = int(input('enter lower range : '))
u = int(input('enter upper range : '))

for i in range(l, u+1):
    a.append(i)
    a.append(i*i)
    a.append(i*i*i)

a = tuple(a)
print(a)
