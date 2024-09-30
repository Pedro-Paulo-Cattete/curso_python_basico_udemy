"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
Método -> ação dentro de um objeto
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

"""
texto = iter ('Luiz') # __iter__()
# "__" são chamados de dunder
"""

iteratador = iter(texto)  # iterator
while True:
     try:
         letra = next(iteratador)
         print(letra)
     except StopIteration:
         break

print("")
# While e For -> Ambos tendo a mesma função mas com tamanhos diferentes

for letra in texto:
    print(letra)