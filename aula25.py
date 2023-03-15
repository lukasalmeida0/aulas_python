variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:_>10}') # ese comando serve para preenchimento total de caracteres
# neste exemplo eu estou colocando um total de 10 espaços
# mas com a string 'ABC' no final, tendo 7 espaços no inicio e
# os 3 algarismos no final, totalizando os 10 espaços.

print(f'{1000.87134789234789432:0=+10,.1f}')

print(f'O hexadecimal de 1500 é: {1500: 08x}')

print(f'{variavel!r}')
"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""