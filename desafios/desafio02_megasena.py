import random


def fatorial(x):
    fact = 1
    for i in range(1, x+1):
        fact = fact * i
    return fact


def sorteio(lst_balls, balls_sorteadas, lst_sorteadas):
    lst_balls = lst_balls.copy()
    sortear = []
    for i in range(balls_sorteadas):
        m = lst_balls.pop(random.randint(0, len(lst_balls)-1))
        sortear.append(m)
    sortear = sorted(sortear)
    if sortear not in lst_sorteadas:
        return lst_sorteadas.append(sortear)
    else:
        return sorteio(balls, bolas_sorteadas, sorteadas)


# inicio do codigo
print('===============================================')
print('================ CASA DE JOGOS ================')
print('DIGITO 1: MEGASENA\nDIGITO 2: QUINA\nDIGITO 3: LOTO-FÁCIL\nDITITO 4: DIGITE AS QUANTIDADES')
n = int(input('waiting... '))
if n == 1:
    total_de_bolas = 60
    bolas_sorteadas = 6
elif n == 2:
    total_de_bolas = 80
    bolas_sorteadas = 5
elif n == 3:
    total_de_bolas = 25
    bolas_sorteadas = 15
elif n == 4:
    total_de_bolas = int(input('Quantidade de bolas no globo: '))
    bolas_sorteadas = int(input('Quantidade de bolas sorteadas:'))

balls, sorteadas = [], []
# popular lista com a quantidade de bolas
for i in range(1, total_de_bolas+1):
    balls.append(i)

# combinação para saber nº maximo de possibilidades feito de forma pura
qtd_combinacoes = int(fatorial(total_de_bolas) / (fatorial(bolas_sorteadas)
                                                  * fatorial(total_de_bolas-bolas_sorteadas)))
# sorteios
for _ in range(qtd_combinacoes):
    sorteio(balls, bolas_sorteadas, sorteadas)
print('\n===============================================')
print('=========== TODAS AS POSSIBILIDADES ===========')
print(sorteadas)
