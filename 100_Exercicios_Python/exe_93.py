#93. Faça um programa em C para ler valores e armazená-los em uma matriz D 5 x 5. A seguir
#o programa deverá calcular a soma dos valores que compõem a diagonal principal e a
#diagonal secundária da matriz

print('-------- Soma da Diagonal principal e Secundária --------\n')

matriz = [[0 for coluna in range(5)] for linha in range (5)]

coluna = 0
linha = 0

#Criação da Matriz
for coluna in range(0,5):
    for linha in range(0,5):
        matriz[coluna][linha] = int(input(f'Digite o valor da C[{coluna}] , L[{linha}]: '))

somaDiagonalPrincipal = 0
somaDiagonalSecundaria = 0

#Soma da Diagonal Principal
while coluna < 5:
    while linha < 5:
        somaDiagonalPrincipal = somaDiagonalPrincipal + matriz[coluna][linha]
        coluna += 1
        linha += 1

#Soma da Diagonal Secundária
linha = 0
coluna = 4
while coluna >= 0 and linha < 5:
    somaDiagonalSecundaria = somaDiagonalSecundaria + matriz[coluna][linha]
    linha += 1
    coluna -= 1

#Mostrar a Matriz pro Usuário
print('\nA matriz inserida é:')
posicao = 0
for posicao in range(0,5):
    print(f'{matriz[posicao]}')      

print(f'\nA soma da Diagonal Principal é igual a: {somaDiagonalPrincipal}')
print(f'A soma da Diagonal Secundária é igual a: {somaDiagonalSecundaria}')