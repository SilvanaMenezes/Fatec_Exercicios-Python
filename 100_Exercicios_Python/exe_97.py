# # 97. Escrever um algoritmo e implementá-lo em linguagem C que leia uma matriz
# de valores inteiros 5 por 5 e a exiba. A seguir, leia dois números x e y e em seguida
# troque a xésima linha pela y-ésima linha, a x-ésima coluna com a y-ésima coluna, a diagonal principal
# com a secundária e, por fim mostre a matriz assim modificada

print('-------- Trocando valores de uma Matriz 5x5 --------\n')

matriz = [[0 for coluna in range(5)] for linha in range(5)]
linhaX = [[0 for coluna in range(5)] for linha in range(1)]

diagonalPrincipal = [[0 for coluna in range(5)] for linha in range(5)]
diagonalSecundaria = [[0 for coluna in range(5)] for linha in range(5)]

#Preenchendo os valores da Matriz
for linha in range(5):
  for coluna in range(5):
    matriz[linha][coluna] = int(input(f'Digite o valor da C[{coluna}] , L[{linha}]: ')) 

#Pedindo qual linha quer trocar
trocaX = int(input(f'\n\nDigite o número da linha que deseja trocar: '))
trocaY = int(input(f'Você deseja trocar a L [{trocaX}] para qual linha: '))

indice = 0
print('\nMatriz Inserida Antes das trocas')

for indice in range(0,5):
    print(f'{matriz[indice]}')

#Trocando a linha X pela linha Y
for coluna in range(5):
  for linha in range(5):
    if linha == trocaX:
      linhaX[linha][coluna] = matriz[trocaX][coluna]
      matriz[linha][coluna] = matriz[trocaY][coluna]
    elif linha == trocaY:
      matriz[linha][coluna] = linhaX[trocaX][coluna]

#Armazenando os números da Diagnonal Principal
linha = 0
coluna = 0
while coluna < 5:
  while linha < 5:
    diagonalPrincipal[linha][coluna] = matriz[linha][coluna]
    linha += 1
    coluna += 1

linha = 0
coluna = 4
while coluna >= 0 and linha < 5:
    diagonalSecundaria[linha][coluna] = matriz[linha][coluna]
    linha += 1
    coluna -= 1

#Trocando os valores das Diagnonais
LinhaDiagonalPrincipal = 0
ColunaDiagonalPrincipal = 0

LinhaDiagonalSecundaria = 0
ColunaDiagonalSecundaria = 4

for coluna in range(5):
  for linha in range(5):
    if (matriz[linha][coluna] == diagonalPrincipal[LinhaDiagonalPrincipal][ColunaDiagonalPrincipal]):
      matriz[LinhaDiagonalPrincipal][ColunaDiagonalPrincipal] = diagonalSecundaria[LinhaDiagonalSecundaria][ColunaDiagonalSecundaria]
      matriz[LinhaDiagonalSecundaria][ColunaDiagonalSecundaria] = diagonalPrincipal[LinhaDiagonalPrincipal][ColunaDiagonalPrincipal]

  LinhaDiagonalPrincipal += 1
  ColunaDiagonalPrincipal += 1
  LinhaDiagonalSecundaria += 1
  ColunaDiagonalSecundaria -= 1

print(f'\n- Você escolheu trocar a linha L[{trocaX}] pela L[{trocaY}];\n- A diagonal Principal foi trocada pela Diagonal Secundária.\n\nConfira Abaixo sua nova Matriz:')


for indice in range(0,5):
    print(f'{matriz[indice]}')