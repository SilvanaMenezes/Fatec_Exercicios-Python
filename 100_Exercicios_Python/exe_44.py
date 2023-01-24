# 44. Escreva um programa que imprima todos os números de 1 até 100, inclusive, e a soma de todos eles.

inteiro = 1
soma = 0

while (inteiro <= 100):
  print(inteiro, end = '+')
  soma = soma + inteiro
  inteiro = inteiro + 1

print(f'\nA soma dos inteiros de 1 à 100 é: {soma}')
