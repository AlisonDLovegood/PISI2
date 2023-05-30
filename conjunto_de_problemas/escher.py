n = int(input())
m = [int(i) for i in input().split()]
i, j = 0, -1
escher = m[i] + m[j]
# print(m[i] + m[j], escher)
while i <= n-1:
    if (escher != (m[i]+m[j])):
        print("n")
        break
    i += 1
    j -= 1
else:
    print("s")
