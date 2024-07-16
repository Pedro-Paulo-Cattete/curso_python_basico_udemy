# Operadores in (Dentro) e not it (Fora)
# Strings são iteráveis
#  0 1 2 3 4
#  P e d r o
# -5-4-3-2-1

#Váriaveis:
nome = 'Pedro'

#Cod:
print(nome[1])
print(nome[-4])
print('')
#Código percente ou não pertence:
print("P" in nome)
print("e" in nome)
print("d" in nome)
print("r" in nome)
print("o" in nome)
print("y" in nome)
print('')
print("P" not in nome)
print("e" not in nome)
print("d" not in nome)
print("r" not in nome)
print("o" not in nome)
print("y" not in nome)
#Cod encontrar valores em váriaveis:
nome_user = input('Digite o seu nome: ')
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome_user:
    print(f'{encontrar} está em {nome_user}')
else:
    print(f'{encontrar} não está em {nome}')