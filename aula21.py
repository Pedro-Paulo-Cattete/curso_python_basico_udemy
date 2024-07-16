# Operadores Lógicos
# and (e) or (ou) not (não)
# Obs.: Existe também o none, que seria um "não valor"
# São considerados valores falsy: 0 0.0 '' False

# Operador Lógico "and" (e)
# and = todos os valores tem de ser verdadeiros

entrada = input("[E]ntrar ou [S]air ")
senha_digitada = input ("Senha: ")
senha_permitida = "12345"

if entrada == 'E' and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")