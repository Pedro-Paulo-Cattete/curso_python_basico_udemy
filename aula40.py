""" Calculadora com while"""




#.lower torna tudo que for máiusculo pra minúsculo
#.startwith Checa se começa com (), é um boolean

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    else:

        if numeros_validos is True:

            adicao = num_1_float + num_2_float
            subtracao = num_1_float - num_2_float
            divisao = num_1_float / num_2_float
            multiplicacao = num_1_float * num_2_float

            if operador == "+":
                print(adicao)
            elif operador == "-":
                print(subtracao)
            elif operador == "/":
                print(divisao)
            elif operador == "*":
                print(multiplicacao)
            else:
                print("Erro")


            sair = input('Quer sair? [s]sim: ').lower().startswith('s')
    
            if sair is True:
                break