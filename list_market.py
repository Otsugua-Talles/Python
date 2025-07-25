"""
Lista de compras com listas
o usuário poderá:
inserir, apagar e listas valores da sua lista
Não permita que o programa quebre com
erros de indices inexistentes na lista
"""
import os

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError or IndexError:
            print('Por favor, digite valor númerico.')
        except IndexError:
            print('Este número não está na lista.')
        
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
