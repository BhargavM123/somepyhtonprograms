# bit = int(input("Enter the parity bit:\n"))
# b = str(bit)

c = input("Enter the parity bit:\n")
bit1 = list(c)
print(bit1)

count = 0
count2 = 0
for i in range(0, len(bit1)):
    if bit1[i] == "1":
        count = count + 1

if count % 2 == 0:
    bit1.append("0")
else:
    bit1.append("1")

print(bit1)
#from list into string
bits = ""
bits = bits.join(bit1)
print(type(bits))
# sendbit = int(bits)
print("The transmitted parity bit is", bits)

print("\n--------At Receiver's Side------\n")
# rbit = int(input("Enter the received parity bit:\n"))
#
# rbit = str(rbit)
d = input("Enter the received parity bit:\n")
bit2 = list(d)
for i in range(0, len(bit2)):
    if bit2[i] == "1":
        count2 = count2 + 1

if count2 % 2 == 0:
    print("There is no error in the received bit")
else:
    print("There is error in the received bit")
