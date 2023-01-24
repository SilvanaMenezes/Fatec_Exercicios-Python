#43. Escreva um programa que imprima todos os números pares do intervalo fechado de 1 a 100

print('-------- Números Pares de 1 a 100 --------\n')

for numero in range(1,101):
    if numero % 2 == 0:
        print(numero, end=', ')
        numero += 1