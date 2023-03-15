for i in range(10): # vai pegar item por item dentro de 'range'
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3): 
        print(i, j) # Mesmo dentro de um for, o outro for sempre irá executar
else:
    print('For completo com sucesso!')