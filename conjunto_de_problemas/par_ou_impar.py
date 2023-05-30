p = int(input())
d1 = int(input())
d2 = int(input())

if ((p == 0) and (d1+d2 % 2 == 0)) or ((p == 1) and (d1+d2 % 2 != 0)):
    print('0')
else:
    print('1')
