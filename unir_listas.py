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


