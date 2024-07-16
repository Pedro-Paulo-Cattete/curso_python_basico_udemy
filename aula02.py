# Não usar letras máiusculas pra funções e códigos
# Função sep é para preencher o que vai estar no lugar da virgula, separador
# Função end define algo para se fazer no final da linha
""" 
\r\n (CRLF) ou \n (LF) serve para quebrar a linha e ir para próxima linha, por padrão o python já pula linhas
Pra saber qual dos dois é o seu só olhar ali embaixo no rodapé do VS
""" 
print(12, 34, sep="-", end="#\n")
print(56, 78, sep='-', end='\n#')
print(9, 10, sep='-', end='\n')