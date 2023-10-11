# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

def porcentagem(lista):
    for produto in lista:
        produto["preco"] *= 1.10

    return lista

nova_lista = copy.deepcopy(porcentagem(produtos))

ordenados_nome = copy.deepcopy(sorted(nova_lista,key=lambda item: item["nome"], reverse=True))

ordenados_preco = copy.deepcopy(sorted(nova_lista,key=lambda item: item["preco"]))

print(*nova_lista, sep="\n")
print()
print(*ordenados_nome, sep="\n")
print()
print(*ordenados_preco, sep="\n")
