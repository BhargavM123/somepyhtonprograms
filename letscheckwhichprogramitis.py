ipAdd = input('input the ip address:')
tempArray = ipAdd.split('.')
addrArray = []
str1 = "."

if len(tempArray) != 4:
    raise NameError('not a valid ip address')

for i in tempArray:
    num = int(i)
    if num < 0 or num > 255:
        raise NameError('not a valid ip address')
        addrArray.append(num)

noOfNetwork = int(input('enter the no of segments you want (must be in the form of 2^n)'))

networkRange = int(256 / noOfNetwork)
startadd = 0
for i in range(noOfNetwork):
    print('sub net segment no :', i + 1)
    print(f'starting address:{addrArray[0]}.{addrArray[1]}.{addrArray[2]}.{startadd}')
    print(f'broadcast address:{addrArray[0]}.{addrArray[1]}.{addrArray[2]}.{startadd + networkRange - 1}')
    print(f'default mask :{addrArray[0]}.{addrArray[1]}.{addrArray[2]}.{networkRange}')
    print('no of host', networkRange - 2)
    print()
    startadd = startadd + networkRange