# Objetivo do código: Identificar valores entre si


# Váriaveis:

primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

# Código:

if primeiro_valor == segundo_valor:
    print(f'{primeiro_valor} é igual a {segundo_valor}')

elif primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}')

elif primeiro_valor < segundo_valor:
    print(f'{primeiro_valor} é menor que {segundo_valor}')

else:
    print('Você não digitou valores compátiveis entre si')
    
print('Concluido')