def f(n, a, b):
    if n == 1:
        if n > a and n < b:
            g(chamadas, n)
        return 1
    elif n % 2 == 0:
        if n > a and n < b:
            g(chamadas, n)
        return f(n/2, a, b)
    else:
        if n > a and n < b:
            g(chamadas, n)
        return f(3*n+1, a, b)


def g(chamadas, n):
    chamadas.append(n)
    return chamadas


chamadas = []
entradas = []
t = int(input())
for i in range(t):
    entradas.append(list(map(int, input().split())))

for i in range(len(entradas)):
    chamadas = []
    f(entradas[i][1], entradas[i][0], entradas[i][1])
    print(f'Caso {i+1}: {max(chamadas):.0f}')
