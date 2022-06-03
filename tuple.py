#create tuple and access the element and convert in list

a = (1,2,3,4,5)
print(type(a))
a = list(a)
a.append(2)
print(a)

print(a[2])

a.insert(3,9)
print(a)

b = [2,34,564,43]
a.extend(b)
print(a)

c = (1,2,3,4,5,6,23)
for i in c:
	print(i)

