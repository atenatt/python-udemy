"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade_carro = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

VELOCIDADE_RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_RADAR_1 = 100  # local onde o radar 1 está
RADAR_1_RANGE = 1  # A distância onde o radar pega


velocidade_radar_maior_radar_1 = velocidade 

if velocidade_carro > VELOCIDADE_RADAR_1:
    print(f'Seu carro está acima da velocidade permitida para o')

if local_carro >= (LOCAL_RADAR_1 - RADAR_1_RANGE) and \
    local_carro <= (LOCAL_RADAR_1 + RADAR_1_RANGE) and \
        velocidade_carro > VELOCIDADE_RADAR_1:
        print(f'Seu carro foi multado ')