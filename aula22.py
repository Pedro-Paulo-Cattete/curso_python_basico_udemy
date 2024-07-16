# Operador Lógico "or" (ou)
# or = Se qualquer um dos valores for verdadeiro = true

entrada = input("[E]ntrar ou [S]air ")
senha_digitada = input ("Senha: ")
senha_permitida = "12345"

if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")

#Avaliação de Curto Circuito