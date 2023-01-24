# 23.Escreva um programa que leia um número e imprima se este número é ou não par.

print('-------- Identificador de Números Pares e Impares --------\n')

numero = int(input('Digite um número: '))
resultado = numero % 2

if resultado == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é impar'.format(numero))