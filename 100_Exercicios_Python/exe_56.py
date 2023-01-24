#56.Um número se diz perfeito se é igual à soma de seus divisores próprios. Divisores próprios de um número positivo N são todos os divisores inteiros positivos de N exceto o próprio N. 

N = int(input('Digite um número: '))
print ('Divisores de', N, 'são: ')
for  i in range(1, N + 1):
    if N % i == 0: 
        print(f'{i}', end='  ')

for i in range(1, i <= N):
    s = i + i
print()
print('soma dos divisores é --> ',i)