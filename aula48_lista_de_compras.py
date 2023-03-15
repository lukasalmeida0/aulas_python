"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar
os valores da sua lista.
Não permita que o programa quebre com erros de indices
inexistentes na lista.
"""
import os

lista = []
verificar_acao = False

while True:

    print('-------------- LISTA DE COMPRAS --------------')
    acao = input('[I]nserir - [A]pagar - [L]istar: ').lower()
    verificar_acao = acao.isalpha()
    if verificar_acao == True:
        
            if acao.startswith('l'):
                os.system('cls')
                if len(lista) == 0:
                    print('LISTA VAZIA')
                else:                
                    for indice in lista:
                        print(indice.title())
                continue
            if acao.startswith('i'):
                item = input('O que deseja inserir na lista? ')
                lista.append(item)
                os.system('cls')
                print('Item adicionado!')
                continue
            if acao.startswith('a'):
                try:
                    apagar = int(input('Qual item da lista deseja apagar? '))
                    apagar -= 1
                    del lista[apagar]
                    os.system('cls')
                    print('Item apagado!')
                    continue
                except:
                    os.system('cls')
                    print('Digite apenas o NÚMERO do item que deseja apagar')
                    continue
            else:
                os.system('cls')
                print('Insira uma opção válida: ')
                continue
    
    else:
        sair = input('Deseja sair? ').lower().startswith('s')
        if sair == True:
             print('Saiu do sistema.')
             break
        else:
            print('Então por favor, digite uma letra.')
            continue