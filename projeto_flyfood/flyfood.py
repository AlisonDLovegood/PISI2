'''
==================================================================================
    UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO
    DEPARTAMENTO DE ESTATÍSTICA E INFORMÁTICA - BSI
    PROJETO INTERDISCIPLINAR PARA SISTEMAS DE INFORMAÇÃO - 2022.1

    PROFESSOR: RODRIGO G. F. SOARES
    ALUNO: ALBERSON ALISON DE ARAÚJO    
    PROJETO: FLYFOOD
==================================================================================
'''

import time
inicio = time.process_time_ns()


def permutacao(coordenadas):
    if len(coordenadas) <= 1:
        return [coordenadas]
    coordenadas_aux = []
    for i, atual in enumerate(coordenadas):
        elementos_restantes = coordenadas[:i] + coordenadas[i+1:]
        for p in permutacao(elementos_restantes):
            coordenadas_aux.append([atual] + p)
    return coordenadas_aux


coordenadas = {}
with open('BSI/PISI2/projeto_flyfood/assets/matriz.txt', 'r') as arquivo:
    linhas = arquivo.readlines()[1:]
    for i, linha in enumerate(linhas):
        for j, elemento in enumerate(linha.strip().split()):
            if elemento != '0':
                coordenadas[elemento] = (i, j)

coordenadas_sem_R = {key: coordenadas[key]
                     for key in coordenadas if key != 'R'}
lst_permutacao = permutacao(list(coordenadas_sem_R))

custo_minimo, melhor_percurso = -1, ''
for i in lst_permutacao:
    custo = 0
    i.insert(0, 'R')
    i.append('R')
    for j in range(len(i) - 1):
        x1, y1 = coordenadas[i[j]]
        x2, y2 = coordenadas[i[j+1]]
        custo += abs(x1 - x2) + abs(y1 - y2)
    if custo < custo_minimo or custo_minimo < 0:
        custo_minimo = custo
        melhor_percurso = '-'.join(i)

fim = time.process_time_ns()
tempo = (fim - inicio)

print('==================================================================================')
print('---------------------------------  =FLYFOOD=  ------------------------------------')
print(
    f'Menor trajeto: {melhor_percurso}\nMenor custo(em dronômetros): {custo_minimo}\nTempo de execução: {tempo}')
print('==================================================================================')
