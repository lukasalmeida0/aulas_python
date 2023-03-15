frase = 'O Python é uma linguagem de programação multiparadigma. '\
    'Python foi criado por Guido Van Rossum'

i = 0
quantidade = 0
letra = ''
while i < len(frase):

    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue

    qnt_letra_apareceu = frase.count(letra_atual) # conta quantas letras atuais estão dentro da frase = qnt_letra_apareceu

    if quantidade < qnt_letra_apareceu:
        quantidade = qnt_letra_apareceu
        letra = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra}" que apareceu {quantidade} vezes')