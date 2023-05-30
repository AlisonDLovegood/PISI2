a = int(input())
b = int(input())
c = int(input())
v = sorted([a, b, c], reverse=True)
print(v)
if v[0] > v[1] > v[2]:
    print("1")
elif v[0] > (v[1] + v[2]):
    print("1")
elif (v[0] != v[1] and v[1] == v[2]) or (v[0] == v[1] and v[1] != v[2]):
    print("2")
else:
    print("3")
