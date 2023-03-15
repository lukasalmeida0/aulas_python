"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Informe um número: ')



if numero.isdigit(): # função para verificar se a strinbg digitada é um numero.
    numero_int = int(numero)

    if numero_int % 2 == 0:

        print(f'O número {numero_int} é PAR!')
            
    else:
        print(f'O numero é {numero_int} IMPAR!')
else:
    print('Informe um numero inteiro, por favor.')

...
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input('Informe as horas: ')

try:
    horas = int(horas)
    if horas >= 0 and horas <= 11:
        print('Bom dia!')

    elif horas >= 12 and horas <= 17:
        print('Boa tarde!')

    elif horas >= 18 and horas <= 23:
        print('Boa noite!')

    else:
        print('Não conheço essa hora')

except:
    print('Digite um número válido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
cont = int(len(nome))

if cont <= 4:
    print('Seu nome é curto')

elif cont >= 5 and cont <= 6:
    print('Seu nome é normal')

else:
    print('Seu nome é muito grande!')

