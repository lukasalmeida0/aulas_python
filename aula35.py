'''
Iterando strings com while
'''
nome = 'Lukas Almeida'
indice = 0
novo_nome = '' # string vazia pois vai servir para receber cada nova letra do nome.

while indice < len(nome): # enquanto o indice for menor que o tamanho total do nome
    letra = nome[indice] # a variavel 'letra' vai receber o primeiro indice (ou seja, cada letra do nome)
    novo_nome += f'-{letra}' # A variavel 'novo_nome' vai receber sempre a letra antiga + a letra nova.
    # Além de, como a 'letra' é uma string, pode ser usado a f'{}' mesmo fora de print().
    indice += 1 # Vai aumentar o numero do indice, possibilitando a variavel novo_nome capturar as letras seguintes.

novo_nome += '-' # serve para colocar o - no final

print(novo_nome) # No final vai printar na tela o novo nome com todas as modificações
