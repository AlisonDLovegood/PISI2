try:
    a = []
    b = []
    for i in range(4):
        a.append(int(input()))
    for i in range(4):
        b.append(int(input()))
    if a[2] < b[0] or a[0] > b[2]:
        print("0")
    elif a[3] < b[1] or a[1] > b[3]:
        print("0")
    else:
        print("1")

except ValueError:
    print("Só números inteiros!!!")
