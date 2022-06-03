try:

    c = 21/0
    print("a/b = %d"%c)

except Exception:
    print("can't divide by zero")

try:
    a = [1, 2, 3]
    print(a[3])
except LookupError:
    print("Index out of bound error.")
else:
    print("Success")

try:
    class Attributes(object):
        pass

    object = Attributes()
    print(object.attribute)
except:
    print("exception AtrributeError")