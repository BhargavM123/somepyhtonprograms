ip = input('Enter an IPv4 IP Address: ')
l = list(map(str, ip.split('.')))

def check():
    for ele in l:
        if int(ele) < 0 or int(ele) >= 255:
            return 0
        elif ele[0] == '0':
            return 0

if ip.count('.') != 3:
    print("Invalid IPv4 IP Address!!!")
elif ip[0] == '0':
    print("Invalid IPv4 IP Address!!!")
elif check() == 0:
    print("Invalid IPv4 IP Address!!!")
else:
    n = l[0]
    n = int(n)
print('The Class of Entered IPv4 IP Address ', ip, ' is : ', end=' ')
if 0 <= n <= 127:
    print('Class A')
    a = '255.0.0.0'
    l1 = list(map(str, a.split('.')))
    print('The Default Subnet Mask of Entered IPv4 IP Address ', ip, ' is : ', a)
    print('The Default Network Address of Entered IPv4 IP Address ', ip, ' is : ', l[0], '.', l1[1], '.', l1[2],
    '.', l1[3])
    print('The Default Broadcasting Address of Entered IPv4 IP Address ', ip, ' is : ', l[0], '.', l1[0], '.',
    l1[0], '.', l1[0])
    print('Number of Hosts can be : 16,777,214')

elif 128 <= n <= 191:
    print('Class B')
    b = '255.255.0.0'
    l2 = list(map(str, b.split('.')))
    print('The Default Subnet Mask of Entered IPv4 IP Address ', ip, ' is : ', b)
    print('The Default Network Address of Entered IPv4 IP Address ', ip, ' is : ', l[0], '.', l[1], '.', l2[2], '.',
    l2[3])
    print('The Default Broadcasting Address of Entered IPv4 IP Address ', ip, ' is : ', l[0], '.', l[1], '.', l2[0],
    '.', l2[0])
    print('Number of Hosts can be : 65,534')
elif 192 <= n <= 223:
    print('Class C')
    c = '255.255.255.0'
    l3 = list(map(str, c.split('.')))
    print('The Default Subnet Mask of Entered IPv4 IP Address ', ip, ' is : ', c)
    print('The Default Network Address of Entered IPv4 IP Address ', ip, ' is : ', l[0], '.', l[1], '.', l[2], '.',
    l3[3])
    print('The Default Broadcasting Address of Entered IPv4 IP Address ', ip, ' is : ', l[0], '.', l[1], '.', l[2],
    '.', l3[0])
    print('Number of Hosts can be : 254')
elif 224 <= n <= 239:
    print('Class D')
    print("The Class D is not Equipped with Default Subnet Mask.")

elif 240 <= n <= 255:
    print('Class E')
    print("The Class E is not Equipped with Default Subnet Mask.")
else:
    print("Invalid IPv4 IP Address!!!")

