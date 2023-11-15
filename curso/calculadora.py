
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    numeros_validos = None

    numero_f1 = 0
    numero_f2 = 0
    try:
        numero_f1 = float(numero1)
        numero_f2 = float(numero2)
        numeros_validos = True
    except Exception as error:
        numeros_validos = None
        print(error)

    if numeros_validos is None:
        print('Um ou ambos os números são inválidos.')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '/' and numero_f2 == 0.0:
        print('Não é permitida a divisão por zero.')
        continue

    print('Relizando a sua conta. Confira o resultado abaixo:')

    if operador == '+':
        print(f'{numero_f1} + {numero_f2}=', numero_f1 + numero_f2)
    elif operador == '-':
        print(f'{numero_f1} - {numero_f2}=', numero_f1 - numero_f2)
    elif operador == '/':
        print(f'{numero_f1} / {numero_f2}=', numero_f1 / numero_f2)
    elif operador == '*':
        print(f'{numero_f1} * {numero_f2}=', numero_f1 * numero_f2)
    else:
        print('Nunca deveria chegar aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair:
        break
