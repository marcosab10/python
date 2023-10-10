cpf = '746.824.890-70'
multipicador_1 = 10
multipicador_2 = 11
resultado_1 = 0
resultado_2 = 0
lista = cpf.split('-')
numeros = lista[0]
verificacao = lista[1]

for digito in numeros:
    if(digito != '.' and digito != '-'):
        numero = int(digito)
        resultado_1 += numero * multipicador_1
        resultado_2 += numero * multipicador_2 
        multipicador_1 -= 1
        multipicador_2 -= 1

resultado_2 += multipicador_2 * int(verificacao[0])

resultado_1 = resultado_1 * 10
resultado_2 = resultado_2 * 10
primeiro_digito =  resultado_1 % 11
segundo_digito = resultado_2 % 11
if(primeiro_digito > 9):
    primeiro_digito = 0
if(segundo_digito > 9):
    segundo_digito = 0

print(primeiro_digito == int(verificacao[0]) and segundo_digito ==  int(verificacao[1]))

