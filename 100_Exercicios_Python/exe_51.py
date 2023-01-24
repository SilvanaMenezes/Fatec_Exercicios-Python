# 51. A série de Fibonacci é formada pela sequencia:  1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Escreva um programa que gere a série de FIBONACCI até o N-ésimo termo (com N sendo uma entrada do algoritmo).														

n = int(input('Digite a série de FIBONACCI deseja mostrar: '))

anterior = 0
proximo = 1
soma = 1

for n in range(0,n):
  soma = proximo + anterior
  anterior = proximo
  proximo = soma
  print('{} - '.format(soma), end='')

print('FIM')


