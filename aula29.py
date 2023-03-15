"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 63  # velocidade atual do carro
local_carro = 102  # local em que o carro está na estrada

VELOCIDADERADAR_1 = 60  # velocidade máxima do radar 1
LOCALRADAR_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if velocidade > VELOCIDADERADAR_1:
    print('Velocidade acima do permitido.')
    if (LOCALRADAR_1 + RADAR_RANGE) >= local_carro and (LOCALRADAR_1 - RADAR_RANGE) <= local_carro:
        print('O carro foi multado')
    else:
        print('O carro não foi multado, fora do alcance do radar')

else:
    print('Velocidade OK')