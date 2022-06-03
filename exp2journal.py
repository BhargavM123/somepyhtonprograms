def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);

num = int(input("enter a number"))
print("Factorial of", num, "is",
      factorial(num))

print()
num = int(input("enter a number"))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))
