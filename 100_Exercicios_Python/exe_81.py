# 81. Escreva um programa em Python que normalize uma string lida, em uma nova string. Normalizar uma string é o processo de remover os espaços excedentes que separam as palavras.

string = str(input('Digite uma string: '))

lista = string.split()
print('A string digitada sem espaços fica assim: {}'.format(''.join(lista)))
