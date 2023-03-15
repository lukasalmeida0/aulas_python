# INTRODUÇÃO AO try / except
# try : tentar executar um código
# except : ocorreu algum erro ao tentar executar

# print(1234)
# print(456)




numero_str = input('Vou dobrar o numero que você digitar: ')
# numero_float = float(numero_str)

# if numero_str.isdigit():
#     print(numero_str.isdigit())
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')

# else:
#     print('Isso não é um numero')

#################################


try:
     print('STR', numero_str)
     numero_float = float(numero_str)
     print('FLOAT', numero_float)
     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um numero')