
import os

palavra_secreta = 'Lionel Messi'.upper()
letras_acertadas = ''
numero_tentativas = 0

print('!!! JOGO DE ADVINHA !!!')
print('Tente advinhar a palavra')
print('\r')
while True:
    letra_digitada = input('Digite uma letra (maiúsculo): ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('!!! PARABÉNS, VOCÊ GANHOU !!!')
        print('A palavra era', palavra_formada)
        print('Tentativas e acertos:', numero_tentativas)
        print('\r')