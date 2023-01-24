#27.Escreva um programa que leia 3 números e calcule a média ponderada entre eles.
#Considere que o maior número recebe peso 5 e os outros dois recebem peso 2,5.

print('-------- Média Ponderada --------\n')

numero1 = (float(input('Digite um número: ')))
numero2 = (float(input('Digite um número: ')))
numero3 = (float(input('Digite um número: ')))


if ( numero1 > numero2 ) and  (numero1 > numero3):
    media = (5 * numero1 + 2.5 * numero2 + 2.5 * numero3) / (5 + 2.5 + 2.5)
    print('\nA média ponderada é igual a: ', media)

if (numero2 > numero1) and (numero2 > numero3):
    media = (5 * numero2 + 2.5 * numero1 + 2.5 * numero3) / (5 + 2.5 + 2.5)
    print('\nA média ponderada é igual a: ', media)

if (numero3 > numero1)  and (numero3 > numero2):
    media = (5 * numero3 + 2.5 * numero1 + 2.5 * numero2) / (5 + 2.5 + 2.5)
    print('\nA média ponderada é igual a: ', media)