def fatorial(x):
    if x == 0:
        return 1
    else:
        return x * fatorial(x-1)


def combinacao(q, r):
    comb = fatorial(q)/(fatorial(r)*fatorial(q-r))
    return comb


q = int(input())
r = int(input())

print(combinacao(q, r))
