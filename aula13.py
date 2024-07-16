#Exercício:
#Calculo de IMC

#Váriaveis:
nome = "Pedro"
altura = 1.83
peso = 103.5
imc = peso / (altura * altura) # IMC = peso / (altura x altura).

#Texto Solicitado:
"""
"Nome" tem "Altura" de altura,
pesa "Peso" quilos e seu MC é
"IMC"
"""

#Resultado:
print(nome, "tem", altura, "de altura")
print("pesa", peso, "quilos e seu MC é")
print(imc)

#FString - Formatação de Strings - Usar váriavel dentro de variável
#No caso do .2f da linha 1 trata de quantas casas decimais deseja 

linha_1 = f'{nome} tem {altura:2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)