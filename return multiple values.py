def multireturn (a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b

    return add,sub,div,mul
    # return print(add, sub, div, mul)


a = int(input("enter a : "))
b = int(input("enter b : "))

multireturn(a, b)

add,sub,div,mul = multireturn(a,b)

print(add,sub,div,mul)


