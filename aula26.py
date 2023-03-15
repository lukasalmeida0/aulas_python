"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
IMP = [COLCHETES]  SERVE PARA PUXAR UM INDICE, DOIS PONTOS : SIGNIFICA 'ATÉ'
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel [4:]) # colchetes serve para pegar um indice
# neste exemplo eu quis ler a variável do indice 4 por diante, já que informei
# o inicio de onde eu quero começar e não informei o final '[4:]'.
print(len(variavel)) # contagem de caracteres função len()
print(variavel[:len(variavel):2]) # O passo faz a contagem de 2 em 2 caracteres
print(variavel[::-1]) # Lendo essa função fica: ler a variavel do inicio ao fim e ao contrario [::-1]
