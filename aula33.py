"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Tipos imutáveis que já vimos: str, int, float, bool
"""
"""
tipo_string = 'Pedro Paulo'
tipo_int = '10'
tipo_float = '10,5'
tipo_bool = "True or False"
"""

#Exemplo de String sendo Imutável:
string = "pedro paulo"
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)

#Exemplo de Método de String:

#Primeira letra em máisculo:
print(string.capitalize())
#Preenche com 0 até chegar a X caracteres entre parenteses: 
print(string.zfill(100))