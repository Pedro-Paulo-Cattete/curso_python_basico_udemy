

frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi crado por Guido van Rossum.'

# print(frase.count('Python')) #Contador de string

i = 0 # Váriavel que será usada pra Índice: Posição do caracter na string
qtd_apareceu_mais_vezes = 0 # Base 0 para comparação de contagens
letra_que_apareceu_mais_vezes = '' #Será preenchido com a fórmula

while i < len(frase): # Enquanto índice for menor que o tamanho da frase:
    letra_atual = frase[i] # Remete a letra que está na posição atual do índice na frase
    
    if letra_atual == ' ': # Se for um espaço e não um caracter,
        i += 1 # Vai pular esse índice
        continue
    
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual) # A contagem de vezes que aparece a letra_atual em frase

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual: #Se a contagem base for menor que a quantidade da letra_atual na frase
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual #Quantidade base se torna a letra atual, para podermos salvar como nova base
        letra_que_apareceu_mais_vezes = letra_atual #Preenche a variável com a letra_atual que foi usada pra checar quantidade na checagem anterior

    i += 1 # +1 no caso de string vai pular para o próximo carecter da string

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_que_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)