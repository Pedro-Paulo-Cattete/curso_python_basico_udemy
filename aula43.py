# Exemplo de contagem de letras:
"""
texto = 'Python'

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i], i) # Imprime texto com posição do índice ao lado

    i += 1
"""

"""
# Função do While: Pra quando você não sabe quantas repetições serão feitas:
senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x):')

    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas')
"""

# For = Quando sabemos quandos repeticões serão feitas:
# For = "Para" - então para cada letra dentro do iterável (No caso abaixo string)

texto = "Python" #Sabemos que nesse caso só serão repetidas 6 vezes
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')