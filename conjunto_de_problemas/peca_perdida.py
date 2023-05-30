def sum_list(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma


lista_incompleta = [1, 2, 3, 4]
lista_completa = [1, 2, 3, 4, 5]
print(sum_list(lista_completa) - sum_list(list))
