def xor(a,b):
    result = []
    for i in range(1,len(b)):
        if a[i] == b[i]:
            result.append('0')
        else :
            result.append('1')
    return ''.join(result)


def mod2Div(data, divisor):
    pick = len(divisor)
    tmp = data[0: pick]
    while pick < len(data):
        if tmp[0] == '0':
            tmp = xor('0' * pick, tmp) + data[pick]
        else:
            tmp = xor(divisor, tmp) + data[pick]
        pick = pick + 1

    if tmp[0] == '0':
        tmp = xor('0' * pick ,tmp)
    else:
        tmp = xor(divisor,tmp)

    checkwork = tmp
    return checkwork




def encodeData(data,divisor):
   len_l = len(divisor)
   appended_data = data + '0' * (len_l - 1)
   remainder = mod2Div(appended_data,divisor)
   codeword = data + remainder
   print("the crc code is : ", remainder)
   print("the transmitted data is : ", codeword)



data = input("enter the data bits : ")
divisor = input("enter the divisor bits : ")
encodeData(data, divisor)


def decodeData(data, divisor):
    len_l = len(divisor)

    remainder = mod2Div(data, divisor)

    temp = '0' * ( len_l - 1 )
    if temp == remainder:
        print("CRC is correct and data transmitted is OP")
    else:
        print("data transmitted is corrupted")


data1 = input("enter the data bits : ")
divisor1 = input("enter the divisor bits : ")
decodeData(data1, divisor1)
