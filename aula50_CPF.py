"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
10  9  8  7  6  5  4  3  2  *
 1  2  3  4  5  6  7  8  9
10 18 24 28 30 30 28 24 18
"""

lista_de_multiplicacao = [10, 9, 8, 7, 6, 5, 4, 3, 2]
lista = []
primeiro_item_da_lista = None
resultado = 0
cpf = input('Informe seu CPF: ')

for i in cpf:
    resultado = int(i) * lista_de_multiplicacao[0]
    del lista_de_multiplicacao [0]
    lista.append(resultado)

primeiro_item_da_lista = lista[0]
del lista[0]
for numero in lista:
    numero += primeiro_item_da_lista
    del lista[0]

resultado = (numero * 10) % 11

if resultado > 9:
    resultado = 0
    print(resultado)
else:
    print(resultado)

# # #

dez = cpf + str(resultado)

lista_de_multiplicacao2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
lista2 = []
indice2 = None
resultado2 = 0

for i2 in dez:
    resultado2 = int(i2) * lista_de_multiplicacao2[0]
    del lista_de_multiplicacao2[0]
    lista2.append(resultado2)

primeiro_item_da_lista2 = lista2[1]
del lista2[0]

for numero2 in lista2:
    indice2 = numero2 + primeiro_item_da_lista2
    del lista2[0]

print(indice2)

resultado2 = (indice2 * 10) % 11

if resultado2 > 9:
    resultado2 = 0
    print(resultado2)
else:
    print(resultado2)

cpf_final = cpf + str(resultado) + str(resultado2)
print(cpf_final)


# # # NAO FUNCIONOU, DESISTI