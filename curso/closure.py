def multiplica(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicar = multiplica(2)
triplicar = multiplica(3)
quadruplicar = multiplica(4)


print(duplicar(3))
print(triplicar(3))
print(quadruplicar(3))