print("\n", 37 * "-", "SENDER SIDE", "-" * 37)


def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

# x = xor('1100','1001')
# print(x)
def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[0: pick]

    while pick < len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick] #means in divident pick i.e 4th element in first iteration
        else:
            tmp = xor('0' * pick, tmp) + divident[pick]
        pick += 1
    print(tmp)

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)
    print(tmp)
    checkword = tmp
    return checkword


def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    print("CRC/Remainder obtained after encoding: ", remainder)
    print("Data to be transmitted at the sender side: ", codeword)


data = input("Enter the Data Bits: ")
key = input("Enter the Divisor Bits: ")
encodeData(data, key)

print("n", 36 * "-", "RECEIVER SIDE", "-" * 36)


def decodeData(data, key):
    # l_key = len(key)
    # appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(data, key)
    # codeword = data + remainder
    print("CRC/Remainder obtained after decoding: ", remainder)
    temp = "0" * (len(key) - 1)
    if remainder == temp:
        print("If CRC/Remainder are '0'.given data received is Correct.")
    else:
        print("If CRC/Remainder are not '0'.given data received is Wrong.Please try retransmission.")


data1 = input("Enter the Data Bits:")
key = input("Enter the Divisor Bits:")
decodeData(data1, key)
print("\n", 40 * "-", "DONE", "-" * 40, "\n")
