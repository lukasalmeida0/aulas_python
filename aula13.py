nome = 'Lukas Almeida'
altura = 1.80
peso = 90
imc = peso / (altura * altura)  #IMC = peso / (altura x altura)

# f.strings
linha_unica = f'{nome} tem altura de {altura:.2f} pesa {peso} quilos e seu IMC é: {imc:.2f}'

print(linha_unica)