numero_digitado = input('Por favor, digite um número: ')

if numero_digitado.isdigit():
    numero_int = int(numero_digitado)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'
    print(f'O número {numero_int} é {par_impar_texto}')

else:
    print('O valor digitado não é um número')
