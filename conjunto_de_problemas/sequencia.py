n = int(input())
v = []
for i in range(n):
    v.append(int(input()))
sum = 0
for i in range(len(v)):
    if i == 0:
        sum += 1
    elif (v[i] != v[i-1]):
        sum += 1
    else:
        continue
print(sum)
