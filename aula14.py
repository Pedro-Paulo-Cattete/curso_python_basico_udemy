# Método é uma função dentro de uma função
#Método Format

a = 'A'
b = 'B'
c = 1.1
formato = 'a={} b={} c={}'.format(a, b, c)
formato2 = 'a={0} b={1} c={2:.2f}'.format(a, b, c)

print(formato)
print(formato2)

#Parâmetro Nomeado:

a = 'A'
b = 'B'
c = 1.1
formaton = 'a={nome1} b={nome2} c={nome3}'.format(nome1=a, nome2=b, nome3=c)
formaton2 = 'a={nome1} b={nome2} c={nome3:.2f}'.format(nome1=a, nome2=b, nome3=c)

print(formaton)
print(formaton2)