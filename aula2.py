# \n\r -> CRLF (quebra de linha)
#  \n -> LF (mesma coisa)
print(12, 34, sep='-', end='\nxx') # o \n quebrou a linha e o que veio após foi para a linha de baixo
print(56, 78, sep="-", end='xx\n') #o \n quebrou a linha depois e o que veio antes ficou na linha de cima, quanto o que veio depois quebrou a linha
