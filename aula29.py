"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

Diferente de if / else, try / except vai pular do try para o except mesmo contendo erro
"""

# Exemplo de ter de tratar informação para não ocorrer erro / ter a resposta correta:

numero_str = input("Digite um número e ele sera dobrado: ")
numero_float = float(numero_str) # Transformar str em float pra dobrar de forma correta

if numero_float == type(float) or type(int):
    print(f'{numero_float * 2:.2f}')
else:
    print('Esse não é um número válido')

#Agora com try e except, onde quando da erro ao invés de quebrar o código pula pra except

numero_str2 = input("Digite outro número e ele sera dobrado: ")

try:
    numero_float2 = float(numero_str2)
    print(f'{numero_float2 * 2:.2f}')
except:
    print('Esse não é um número válido')
