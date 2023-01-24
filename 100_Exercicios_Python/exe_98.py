# 98. Escrever um algoritmo e implementá-lo em linguagem Python que leia duas matrizes (4x3 e 3x2), calcule e imprima a matriz que representa o produto entre as duas matrizes lidas.

#criando as matrizes
matrizA = [[0 for coluna in range(3)]for linha in range(4)]
for linha in range(4):
    for coluna in range(3):
        matrizA[linha][coluna] = int(input(f'digite o valor para L[{linha}],C[{coluna}]:'))
print(f'\nOs valores digitados criou a matrizA={matrizA}\n')

matrizB = [[0 for coluna in range(2)]for linha in range(3)]
for linha in range(3):
    for coluna in range(2):
        matrizB[linha][coluna] = int(input(f'digite o valor para L[{linha}],C[{coluna}]:'))
print(f'\nOs valores digitados criou a matrizB={matrizB}\n')

#multiplicando a matrizB * matrizA
produto = []        
for linha in matrizA[linha]:
    produto.append([])
    for coluna in matrizB[coluna]:
        produto[linha].append(0)
        for i in matrizA[coluna]:
            produto[linha][coluna] += matrizA[linha][i] * matrizB[i][coluna]
print(produto)
    




