''' Calculadora com while '''
while True:

    print('--- CALCULADORA COM WHILE ---')

    a = int(input(''))
    operador = input('')
    b = int(input(''))



    if operador == '+':
        print(f'o resultado é: {a + b}')
    if operador == '-':
        print(f'o resultado é: {a - b}')
    if operador == '*':
        print(f'o resultado é: {a * b}')
    if operador == '/':
        print(f'o resultado é: {a / b}')
    
    sair = input('Aperte [s] para sair ').lower().startswith('s')
    
    if sair is True:
        print('Você saiu.')
        break
    else:
        continue