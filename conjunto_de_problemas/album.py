n = int(input('fig no algum: '))
m = int(input('fig compradas: '))
l = []
for i in range(m):
    x = int(input('num: '))
    if x not in l:
        l.append(x)
print(n-len(l))
