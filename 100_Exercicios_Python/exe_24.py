#24. Escreva um programa que leia três números e mostre o maior entre eles.

print( '-------- Maior número --------\n')

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
numero3 = int(input('Digite um número: '))

maior = numero1

if maior < numero2:
    maior = numero2

if maior < numero3:
    maior = numero3

print('O Maior número é o : ' , maior)