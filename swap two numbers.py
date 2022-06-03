# write a program to swap two variable qithout using temporary variable

a = float(input("enter a number"))
b = float(input("enter b number"))

#a = a ^ b   #only works for int
#b = a ^ b
#a = a ^ b

a = a + b
b = a - b
a = a - b

print("a = ",a)
print("b = ",b)
