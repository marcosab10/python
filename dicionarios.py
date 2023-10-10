itens = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    }, 
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    }, 
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }, 
]
numero_acertos = 0
for item in itens:
    pergunta, opcoes, resposta = item
    print(f'{pergunta}: {item.get(pergunta)}')
    print()
    print(f'{opcoes}:')

    for indice , opcao in enumerate(item.get(opcoes)):
        print(f'{indice}) {opcao}')
        
    selecao = input('Escolha uma opção: ')
    try:
        indice = int(selecao)
        lista_opcoes = item.get(opcoes)
        if lista_opcoes[indice] == item.get(resposta):
            print('Acertou')
            numero_acertos += 1
        else:
            print('Errou')
    except:
        print('Errou')

print(f'Você acertou {numero_acertos}')
print(f'de {len(itens)} perguntas.')
