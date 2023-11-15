# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]
# from itertools import zip_longest

# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print(list(zip(l1, l2)))
# print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))

estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista_menor, lista_maior):
    def leia(lista):
        for i in lista:
            yield i

    if(len(lista_menor) > len(lista_maior)):
        aux = lista_menor
        lista_menor = lista_maior
        lista_maior = aux
    
    generator = leia(lista_maior)

    nova_lista = [(elemento, next(generator) ) for elemento in lista_menor]
    return nova_lista

print(zipper(siglas, estados))


