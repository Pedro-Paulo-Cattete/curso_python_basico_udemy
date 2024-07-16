"""
CONSTANTE = "Variáveis que não vão mudar
muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)

Atalho = Por o cursos em cima da váriavel e apertar F2 muda o nome de todos os relacionados
Símbolo "\" = Quebra linha e avisa para o python que vai continuar o código na linha debaixo
Tornar sempre o código o mais legível possível e mais organizado
"""
velocidade = 61 # velocidade atual do carro
local_carro = 90 # local e que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

#Cod:

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1


if velocidade_carro_passou_radar_1:
    print("Passou da velocidade máxima permitida")
if carro_passou_radar_1:
    print("Passou no radar 1")
if carro_multado_radar_1:
    print("Carro multado em radar 1")