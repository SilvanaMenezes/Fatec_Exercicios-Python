# 58. O valor aproximado do número π pode ser calculado usando-se a série
# 𝑆 = 1 − 1 3 3 + 1 − 1 5 3 7 3 + 1 … (ver: progressão aritmética)
#Faça um programa que calcule e imprima o valor de π usando os N primeiros termos da
#série (N sendo informado durante a execução do algoritmo).

import math

pi = 0.0
soma = 0
divisor = 1
contador = 1

n = int(input('\nDigite a quantidade de termos: '))
while(contador <= n):
    if contador % 2 == 0:
      soma = soma - 1/pow(divisor,3)
    else:
      soma = soma + 1/pow(divisor,3)
    contador += 1
    divisor += 2

pi = math.pow((soma * 32.0),(1.0 / 3.0))
print(f'\nSegundo a quantidade de termos informada, {n} a série é: {soma} e o número de Pi é: {pi}\n')

    

