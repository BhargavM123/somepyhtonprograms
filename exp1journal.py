# Lists
l = []

# Adding Element into list
l.append(5)
l.append(10)
l.append(60)
l.append(20)
print("Adding 5 and 10 in list", l)

# Popping Elements from list
l.pop()
print("Popped one element from list", l)
print()

# Tuple
t = tuple(l)

# Tuples are immutable
print("Tuple", t)
print()

# Dictionary
d = {}

# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)

# Removing key-value pair
del d[10]
print("Dictionary", d)
print()

# Array
a = ["1", "2", "3"]

# Adding Array Elements
a.append("4")

# Removing Array Elements
a.pop(1)

print("Array", a)

