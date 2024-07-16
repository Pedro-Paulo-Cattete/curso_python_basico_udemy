"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] (i = inicio / f = fim / p = passos, pula contagem)
Obs.: a função len retorna a qtd de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[-4])     # Vai encontrar o caractere na posição -4
print(variavel[4:])     # Vai encontrar os caracteres de 4 pra frente
print(variavel[4:7])    # Vai encontrar os caracteres de 4 até o 7
print(variavel[1:7:1])  # Vai encontrar de 1 a 7 pulando 1 casa
print(variavel[::-1])   # Utilizando o negativo conseguimos inverter a string
print('')
# Função len = Conta Caracteres das Strings
print(len("O"[variavel]))
print((str(len(variavel))) + (f' Caracteres em {variavel}'))
print('')