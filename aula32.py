"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#Avaliador de Par ou Ímpar


entrada_ex1 = input("Inserir um número inteiro: ")

if entrada_ex1.isdigit():
    transformar_em_inteiro = int(entrada_ex1)
    par_ou_impar = transformar_em_inteiro % 2 == 0

    if par_ou_impar is True:
        print(f"O número {entrada_ex1} é um número Par.")
    else:
        print(f"O número {entrada_ex1} é um número Ímpar")           
else:
    print("Você não digitou um número.")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#Saudação Horas


entrada_ex2 = input("Que horas são no momento?(0-23) ")

if entrada_ex2.isdigit():
    trans_hora_para_número = int(entrada_ex2)
    bom_dia = trans_hora_para_número <= 11
    boa_tarde = trans_hora_para_número >= 12 and trans_hora_para_número <= 17
    boa_noite = trans_hora_para_número >= 18 and trans_hora_para_número <= 23

    if bom_dia:
        print("Bom dia!")
    elif boa_tarde:
        print("Boa tarde!")
    elif boa_noite:
        print("Boa noite!")
    else:
        print("Você não digitou uma hora válida.")
else:
    print("Você não digitou uma hora válida.")

#Obs.: O código acima apesar de correto, tem muitas variáveis sem necessidade,
#Deve se usar várias variáveis no ínicio quando elas vão se repetir várias vezes durante o código.

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada_ex3 = input("Qual o seu nome? ")
contagem_nome = len(entrada_ex3)

if contagem_nome >= 1 and contagem_nome <= 4:
    print(f"O nome {entrada_ex3} possui {contagem_nome} caracteres, logo é um nome curto.")
elif contagem_nome >= 5 and contagem_nome <=6:
    print(f"O nome {entrada_ex3} possui {contagem_nome} caracteres, logo é um nome é normal.")
elif contagem_nome >= 7:
    print(f"O nome {entrada_ex3} possui {contagem_nome} caracteres, logo é um nome é longo.")
else:
    print("Não digitou um nome válido.")