"""
Iteráveis conhecidos até agora:
While: Pra quando você não sabe quantas repetições serão feitas, temos que estabelecer o índice.
For: Quando sabemos quandos repeticões serão feitas, já busca o índice.
Range: Distância e/ou Etapas
Ex.:    range(start, stop, step)
        range(Início do range, Parada do range, De quantos em quantos ele "pula" funcina como o += ou -=)

Range:
For + Range
range -> range(start, stop, step)
"""

print('Quando se põe apenas um valor em "range", ele entende como stop\
 começando do índice inicial, para range(10) temos:')
numeros = range(10)

for numero in numeros:
    print(numero)

print('Quando se põe dois valores em "range", ele entende como start e stop\
 começando do índice onde foi definido o start, para range(5, 10) temos:')
numeros = range(5,10)

for numero in numeros:
    print(numero)

print('Quando se põe três valores em "range", ele entende como start, stop e step\
 começando do índice onde foi definido o start e pulando de acordo com step até\
 chegar no valor de stop, para range(5, 10, 2) temos:')
numeros = range(5,10, 2)

for numero in numeros:
    print(numero)