number = input('Escolha um número: ')

if number.isdigit():
    n_int = int(number)
    pi = n_int % 2 == 0
    pi_texto = 'Ímpar'

    if pi:
        pi_texto = 'par'
    print(f'O número que você escolheu é {pi_texto}')
    print('Valor multiplicado por ele mesmo:',n_int * n_int)
    print('Sua contagem até ele é: ')

else:
    print('O valor digitado não é númerico')

condicao = 0

while condicao < n_int:
    condicao +=1

    if condicao %2 == 0 and condicao %2 != 0:
        continue
    print(condicao)