a = int(input())
b = int(input())
c = int(input())

if (b-a) < (c-b):
    print("1")
elif (b-a) > (c-b):
    print("0")
else:
    print("-1")
