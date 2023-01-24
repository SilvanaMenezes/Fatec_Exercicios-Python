#92. Elabore um programa em C, para ler valores e armazená-los em uma matriz 5 x 5. Após o
#programa deverá responder se a matriz é ou não uma matriz simétrica. Uma matriz
#simétrica possui a mesma composição de valores abaixo e acima da diagonal principal.

print('-------- A Matriz é Simétrica? 5x5 --------\n')

matriz = [[0 for coluna in range(5)] for linha in range (5)]
matrizTransposta = [[0 for coluna in range(5)] for linha in range (5)]

coluna = 0
linha = 0

#Criando primeira Matriz
for coluna in range (0,5):
    for linha in range(0,5):
        matriz[coluna][linha] = int(input(f'Digite o valor da C[{coluna}] , L[{linha}]: '))

#Gerando a Matriz Transposta da Matriz
for coluna in range (0,5):
    for linha in range(0,5):
        matrizTransposta[linha][coluna] = matriz[coluna][linha]

#Verificando se Matriz = Matriz Transposta
posicao = 0
print('\nA Matriz Inserida:\n')

for posicao in range(0,5):
    print(f'{matriz[posicao]}')

if matrizTransposta == matriz:
            print('\nÉ simétrica.')
else:
    print('\nNão é simétrica.')