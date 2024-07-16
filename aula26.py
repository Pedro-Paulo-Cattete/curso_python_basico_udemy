"""
Formatação Básica de strings
s - string
d - int
f - float
<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>100,.1f
Conversion flags - !r (repr) !s (str) !a (ask)
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:0>10}.')
print(f'{variavel:k<10}.')
print(f'{variavel:-^10}.')
print(f'{1000.4873648123746:.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')