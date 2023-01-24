#26. Escreva um programa que leia 3 valores e escreva a soma dos 2 maiores.

print('-------- Soma dos 2 maiores --------\n')

numero1 = (int(input('Digite um número: ')))
numero2 = (int(input('Digite um número: ')))
numero3 = (int(input('Digite um número: ')))

if numero1 > numero3 and numero2 > numero3:
    print('\nA soma dos dois maiores números é: ', numero1 + numero2)

if numero1 > numero2 and numero3 > numero2:
    print('\nA soma dos dois maiores números é: ', numero1 + numero3)

if numero2 > numero1 and numero3 > numero1:
    print('\nA soma dos dois maiores números é: ', numero2 + numero3)