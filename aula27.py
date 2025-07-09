espaco = ' ' * 5

print(f'{espaco}Calculadora Python{espaco}')
print('\r')
while True:
    primeiro_numero = input('Digite um número: ')
    segundo_numero = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    n_validos = None
    primeiro_numero_int = 0
    segundo_numero_int = 0

    try:
        primeiro_numero_int = int(primeiro_numero)
        segundo_numero_int = int(segundo_numero)
        n_validos = True
    except:
        n_validos = None

    if n_validos is None:
        print('Um ou ambos os números não são válidos.')
        continue

    operador_permitido = '+-/*'

    if operador not in operador_permitido:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Calculando, confira o resultado abaixo: ')

    if operador == '+':
        print(f'{primeiro_numero_int} + {segundo_numero_int} =', primeiro_numero_int + segundo_numero_int)
    elif operador == '-':
        print(f'{primeiro_numero_int} - {segundo_numero_int} =', primeiro_numero_int - segundo_numero_int)
    elif operador == '/':
        print(f'{primeiro_numero_int} / {segundo_numero_int} =', primeiro_numero_int / segundo_numero_int)
    elif operador == '*':
        print(f'{primeiro_numero_int} * {segundo_numero_int} =', primeiro_numero_int * segundo_numero_int)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break