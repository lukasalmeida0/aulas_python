""" Calculadora com while """
while True:
    a = input('Digite um número: ')
    b = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(a)
        num_2_float = float(b)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

# # # OPERAÇÃO --------------------------------------
    c = int(a)
    d = int(b)
    sair = input('Quer sair? [s]im: ')
    if sair.lower().startswith('s') is False:

        if operador == '+':
            print(f'o resultado é: {c + d}')
            continue
        if operador == '-':
            print(f'o resultado é: {c - d}')
            continue
        if operador == '*':
            print(f'o resultado é: {c * d}')
            continue
        if operador == '/':
            print(f'o resultado é: {c / d}')
            continue

# # # -----------------------------------------------

    if sair is True:
        print('Você saiu')
        break