# Opedrador Lógico "not"
# Usado para inverter expressões (Se não for o valor = True)
# not true = false / not false = true

#Exemplo:
# Váriaveis
senha = input('Senha: ')

#Cod:
if senha == '123456':
    print('Entrou')
elif not senha:
    print('Você não digitou nada.')
else:
    print('Senha incorreta')


#Avaliação de Curto Circuito

# and = print(True and true and false) = false
# or =  print(True and true and false) = true
# not = print(not True) # Igual a False OU # print(not False) # Igual a True