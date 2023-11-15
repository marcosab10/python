palavra_secreta = 'Python é legal'
tamanho  = len(palavra_secreta)
palavra_display = '*' * tamanho
contador = 0

while contador < tamanho :
    entrada = input('Informe 1 digito que nâo seja numero: ');

    if len(entrada) != 1 or entrada.isdigit() == True:
        print('Entrada inválida.')
        continue

    if entrada in palavra_secreta:
        while True:
            try:
                indice = palavra_secreta.index(entrada)
                palavra_secreta = palavra_secreta[:indice] + '1' + palavra_secreta[indice + 1 :tamanho ]
                palavra_display = palavra_display[:indice] + entrada + palavra_display[indice +1:tamanho]
                contador += 1
            except:
                break
    
   
    print(palavra_display)

print('Parabéns você venceu!')


