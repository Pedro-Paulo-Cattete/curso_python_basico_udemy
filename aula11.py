# Precedência de Operações - Quais operações são feitas primeiro.
"""
Ordem de quais são feitas primeiro:
1. (n + n)
2. **
3. * / // %
4. + -
"""

conta_1 = 1 + 1 ** 5 + 5 # Resultado 7 (1 a quinta = 1 + 1 + 5)
print(conta_1)

conta_2 = (1 + 1) ** (5 + 5) # Resultado 1024 ((1 + 1) 2 ** 10 ((5 + 5))
print(conta_2)

conta_3 = (1 + int(0.5 + 0.5)) # Resultado 2
print(conta_3)