# 57. Sendo 𝑆 = 1 +
# 1 + 1/ 5^5 +  1/ 2^2 + 1/3^3 +  1/4^4 + ⋯  1 / N ^N + , um somatório de N (informado pelo
# usuário) termos, escreva um programa para calcular S para um número N

print('-------- Calculando S --------\n')

n = int(input('Digite o número que deseja calcular: '))

limite = n
numero = 0
s = 1/1**1
print('S = 1 +', end='')

for numero in range(limite-1):
    numero += 2
    s = s + 1/(numero**numero)

print('\nS é igual a = ', '%.4f' % s)
    