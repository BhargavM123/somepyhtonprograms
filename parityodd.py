# bit = int(input("Enter the parity bit:\n"))
# b = str(bit)
a = input("Enter the parity bit: ")
bit1 = list(a)
count = 0
count2 = 0
for i in range(0, len(bit1)):
    if bit1[i] == "1":
        count = count + 1

if count % 2 == 0:
    bit1.append("1")
else:
    bit1.append("0")
bits = ""
bits = bits.join(bit1)
sendbit = int(bits)
print("The transmitted parity bit is", sendbit)

print("\n--------At Receiver's Side------\n")
# rbit = int(input("Enter the received parity bit:\n"))
#
# rbit = str(rbit)
b = input("Enter the received parity bit: ")
bit2 = list(b)
for i in range(0, len(bit2)):
    if bit2[i] == "1":
        count2 = count2 + 1

if count2 % 2 == 0:
    print("There is error in the received bit")
else:
    print("There is no error in the received bit")