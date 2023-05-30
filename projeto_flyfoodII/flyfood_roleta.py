'''
==================================================================================
    UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO
    DEPARTAMENTO DE ESTATÍSTICA E INFORMÁTICA - BSI
    PROJETO INTERDISCIPLINAR PARA SISTEMAS DE INFORMAÇÃO - 2022.1
    PROFESSOR: RODRIGO G. F. SOARES
    ALUNO: ALBERSON ALISON DE ARAÚJO    
    PROJETO: FLYFOOD II
==================================================================================
'''
import math
import random
from random import randint
from typing import List
import time


# -------- LEITURA DO ARQUIVO --------
def ler_arquivo(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    node_coord_section = False
    coordenadas = []
    for line in lines:
        if line.startswith("NODE_COORD_SECTION"):
            node_coord_section = True
            continue
        if node_coord_section:
            if line.startswith("EOF"):
                break
            _, x, y = line.strip().split()
            coordenadas.append((float(x), float(y)))
    return coordenadas


# -------- GERAÇÃO DA POPULAÇÃO --------
def gerar_populacao_inicial(lista, n_permut):
    if (n_permut > math.factorial(len(lista))):
        n_permut = math.factorial(len(lista))
    permutacoes = [None] * n_permut
    count = 0
    while (count < n_permut):
        permut_generacto = random.sample(lista, len(lista))
        if not permut_generacto in permutacoes:
            permutacoes[count] = permut_generacto
            count += 1
    return permutacoes


# -------- FITNESS --------
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # raio da Terra em km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * \
        math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def calcular_distancia_total(coords):
    distancias = []
    for i in range(len(coords)-1):
        lat1, lon1 = coords[i]
        lat2, lon2 = coords[i+1]
        distanciaij = haversine(lat1, lon1, lat2, lon2)
        distancias.append(distanciaij)
    return sum(distancias)


def calcular_fitness(individual):
    distancia_total = calcular_distancia_total(individual)
    fitness = 1 / distancia_total
    return fitness


def medir_aptdao_grupal(population):
    fitness_list = []
    for individual in population:
        fitness = calcular_fitness(individual)
        fitness_list.append(fitness)
    return fitness_list


# -------- SELEÇÃO POR ROLETA --------
def selecionar_por_roleta(populacao, fitness):
    soma_roleta = sum(fitness)
    n_sorteado = random.random() * soma_roleta
    soma_atual = 0
    for i, fit in enumerate(fitness):
        soma_atual += fit
        if soma_atual >= n_sorteado:
            return populacao[i]


# -------- SELEÇÃO DOS PAIS --------
def selecionar_pais(populacao, fitness):
    pais = [None] * len(populacao)
    for count in range(0, len(pais)):
        pais[count] = selecionar_por_roleta(populacao, fitness)
    return pais


# -------- CRUZAMENTO DOS PAIS --------
def cruzar(pais, taxa_cruzamento):
    lista_filhos: List[str] = [None] * len(pais)
    for i in range(0, len(pais)-1, 2):
        if random.random() <= taxa_cruzamento:
            filho1 = cruzar_pais(pais[i], pais[i + 1])
            filho2 = cruzar_pais(pais[i+1], pais[i])
            lista_filhos[i] = filho1
            lista_filhos[i + 1] = filho2
        else:
            lista_filhos[i], lista_filhos[i + 1] = pais[i], pais[i+1]
    return lista_filhos


def cruzar_pais(pai1, pai2):
    filho = [None] * len(pai1)
    ponto_cruzamento1 = randint(1, len(pai1) - 1)
    ponto_cruzamento2 = randint(1, len(pai1) - 1)
    if ponto_cruzamento1 > ponto_cruzamento2:
        aux = ponto_cruzamento1
        ponto_cruzamento1 = ponto_cruzamento2
        ponto_cruzamento2 = aux
    mapping = {}
    for i in range(ponto_cruzamento1, ponto_cruzamento2+1):
        filho[i] = pai1[i]
        mapping[pai1[i]] = pai2[i]
        mapping[pai2[i]] = pai1[i]
    for i in range(len(filho)):
        if i < ponto_cruzamento1 or i > ponto_cruzamento2:
            if pai2[i] not in set(filho):
                filho[i] = pai2[i]
            else:
                if pai2[i] not in mapping:
                    for j in range(len(pai2)):
                        if pai2[j] not in mapping.values():
                            mapping[pai2[i]] = pai2[j]
                            mapping[pai2[j]] = pai2[i]
                            break
                filho[i] = mapping[pai2[i]]
    return filho


# -------- MUTAÇÃO DE BIT --------
def mutacao(filhos, taxa_mutacao):
    for _ in range(0, len(filhos)):
        a = random.random()
        if a <= taxa_mutacao:
            cromo1, cromo2 = randint(0, len(filhos)-1), randint(0, len(filhos)-1)
            aux = filhos[cromo1]
            filhos[cromo1] = filhos[cromo2]
            filhos[cromo2] = aux
    return filhos


# -------- EVOLUÇÃO --------
def evolucao(taxa_cruzamento, taxa_mutacao, pontos_de_entrega, n_cromossomos, n_geracoes):
    populacao = gerar_populacao_inicial(pontos_de_entrega, n_cromossomos)
    fitness = medir_aptdao_grupal(populacao)
    for geracao in range(n_geracoes):
        pais = selecionar_pais(populacao, fitness)
        filhos = cruzar(pais, taxa_cruzamento)
        populacao = mutacao(filhos, taxa_mutacao)
        fitness = medir_aptdao_grupal(populacao)

        indice_menor_custo = fitness.index(min(fitness))
        melhor_rota = populacao[indice_menor_custo]
        km_total = calcular_distancia_total(melhor_rota)

        print(f"-- Geracao: {geracao+1}")
        print(f"-- Melhor rota atual: {melhor_rota}")
        print(f"-- Menor custo atual atual: {km_total:.3f} km\n")
    return melhor_rota, km_total


# -------- MAIN --------
def Main():
    print('==================================================================================')
    print('--------------------------------  = FLYFOOD II =  --------------------------------')
    taxa_cruzamento = 0.9
    taxa_mutacao = 0.4
    pontos_de_entrega = ler_arquivo("BSI/PISI2/projeto_flyfoodII/assets/natal.tsp")
    n_cromossomos = 10
    n_geracoes = 100
    melhor_rota, km_total = evolucao(taxa_cruzamento, taxa_mutacao, pontos_de_entrega, n_cromossomos, n_geracoes)
    fim = time.time()
    print('==================================================================================')
    print('--------------------------------  --RESULTADOS--  --------------------------------')
    print(f"-- Melhor solucao encontrada: {melhor_rota}")
    print(f"-- Menor custo encontrado: {km_total:.3f} km")
    print(f"-- Tempo de execucao: {(fim - inicio):.4f}")
    print('==================================================================================')


if __name__ == "__main__":
    inicio = time.time()
    Main()