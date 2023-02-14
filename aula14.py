a = 'A'
b = 'BBBB'
c = 1.1
string = 'valor a = {}, valor b = {}, valor c = {:.2F}'
formato = string.format(a, b, c)

print(formato)

#ou podemos fazer desse jeito:

print('{1}, {2}, {0}'.format(c, a, b))


# O comando '.format' faz uma formatação nas strings 
# para obter valores configurados corretamente.

# As chaves '{}' buscam os valores referenciados
# na ordem, ou quando numerados (de 0 para frente) 
# buscam os valores sem seguir uma ordem (indices).

print('{1}, {nome3}, {0}'.format(c, a, nome3 = b)) # tudo que vier depois de um parametro nomeado, precisa ser nomeado também

# argumento e parametro:
# argumento é o valor da variavel, ou seja, o que ela
# representa.
# parametro é a nomeação que vc faz da variavel (nome3 = b)
# onde sempre que vc quiser chamar a variavel, vc precisa chamar
# pelo nome ao invés de chamar pela variavel.
# (parametro nomeado)
