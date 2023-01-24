#59. O número e (número de Euler) pode ser representado e calculado por meio da utilização da série de Taylor para e quando x=1, como a soma da seguinte série infinita: 
#e = 1 +  1/1!  +  1/2!  +  1/3!  + ⋯ +( 1)/n! Escreva um programa, que leia o número de termos da série (n) e imprima como saída, o cálculo do número de eu ler para cada um dos n primeiros elementos da série. 
# for c    in  range   (1, 10, 1)
# for de.. no intervalo(de onde comaça, até onde termina, contagem de 1 á 1 ou 2 a 2...)
from math import factorial

n = int(input('digite um número:  '))
f = factorial(n)
limite = n
e = 0
print()
print(f'E = 1 /{n}!', end='')
print()
for numero in range(1,limite):
    e = 1 + (1/f)
    
print(f'E é igual a = ', e)    