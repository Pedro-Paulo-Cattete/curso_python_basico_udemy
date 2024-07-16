"""
Variável = Sempre declarar fora do bloco de código
Flag (Bandeira) - Marcar um local
Nome = Não valor
is (é) e is not (não é) = Define o tipo, valor, identidade
id = identidade

Exemplo de id iguais com váriaveis diferentes:
v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

Exemplo de id diferentes:
v1 = 'a'
v2 = 'b'
print(id(v1))
print(id(v2))
"""

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
if passou_no_if is not None:
    print('Passou no if')