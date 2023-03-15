"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas: # Esse for é para desmembrar a primeira lista
    print(f'A sala é {sala}') # Esse print está aqui só pra mostrar a lista completa dos valores da lista que vão ser listados
    for aluno in sala: # Esse for é para desmembrar a segunda lista
        print(aluno) # Assim eu vou listar cada aluno de cada sala.