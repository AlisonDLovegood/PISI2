r = int(input())  # REPOUSO
f = int(input())  # ATUAL
c = int(input())  # CAPACIDADE

if (f > (3*r)) or (c < 95):
    print("diminuir")
elif (f < (2*f)) and (c > 97):
    print("aumentar")
else:
    print("manter")
