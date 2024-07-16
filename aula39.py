"""
Iterando strings com while
"""

#       012345678910 -> Índice 
nome = "Pedro Paulo"  #Iteráveis

"""
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])
"""

#Exercício:
#Reproduzir esse resultado usando while:
# nova_string += '*P*e*d*r*o* *P*a*u*l*o*'

indice = 0 #Começa do primeiro caracter
novo_nome = '' #Considera como vazia

while indice < len(nome): #Enquanto indice for menor que a quantidade de letras no nome
    letra = nome[indice] #Letra é igual a indice, onde indice é a posição dentro do nome
    novo_nome += f'*{letra}' 
    """
    Novo nome é uma string vazia que será preenchida com letra que na próxima linha vai 
    sempre ser preenchida com o próximo indice fazendo com que apareça o nome completo
    enquanto (While) ele for menor que o len de nome.
    
    Quanto a função "f" seria justamente para poder considerar que podemos trabalhar com
    novo nome, nesse caso acrescentando o caracter "*" antes de cada {letra}
    """
    indice += 1 #Nesse caso mais um é o próximo caracter, estamos trabalhando com strings
novo_nome += '*' #Apenas para acrescentar o caracter * ao final do novo_nome

print(novo_nome)