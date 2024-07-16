"""
Repetições
Função Continue
O continue é como se fosse um continue a operação após resultado solcitado (1).
Enquanto no caso (2) Nesse caso o contador pularia de 9 para 28, 
mas como atribuimos um print a operação ele irá imprimir a informação solicitada nas linhas.
"""
contador = 0


while contador <= 100:
    contador +=1 #Define a operação que será feita quanto ao contador

    if contador == 6: #(1)
        print(f'Não vou mostrar o {contador}.')
        continue 

    if contador >= 10 and contador <= 27: #(2)
        print('Não vou mostrar o', contador)
        continue 

    print(contador)

    if contador == 40:
        break


print('Acabou')