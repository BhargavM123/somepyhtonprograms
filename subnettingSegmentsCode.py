ipAdd = input('input the ip address:')
tempArray = ipAdd.split('.')
l = list(map(str, ipAdd.split('.')))
# b = []
str1 = "."
b = []

if ipAdd.count('.') != 3:
    print('invalid ip address')

if len(tempArray) != 4:
    raise NameError('not a valid ip address')

for i in l:
    b.append(i)
print(b)
# for i in tempArray:
#     num = int(i)
#     if num < 0 or num > 255:
#         raise NameError('not a valid ip address')
#     else:
#         print(num)
#         b.append(num)

noOfNetwork = int(input('enter the no of segments you want (must be in the form of 2^n) : '))

networkRange = int(256 / noOfNetwork)
startadd = 0

for i in range(noOfNetwork):
    print('sub net segment no :', i + 1)
    print(f'starting address:{b[0]}.{b[1]}.{b[2]}.{startadd}')
    print(f'broadcast address:{b[0]}.{b[1]}.{b[2]}.{startadd + networkRange - 1}')
    print(f'default mask :{b[0]}.{b[1]}.{b[2]}.{networkRange}')
    print('no of host', networkRange - 2)
    print()
    startadd = startadd + networkRange
