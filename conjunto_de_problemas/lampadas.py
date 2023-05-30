a = False
b = False
n = int(input())
n1 = list(map(int, input().split()))

for i in range(n):
    if n1[i] == 1:
        a = not (a)
    else:
        a = not (a)
        b = not (b)
if a:
    print('1')
else:
    print('0')
if b:
    print('1')
else:
    print('0')
