#94. Escrever um algoritmo e implementá-lo em linguagem C que leia uma matriz de valores inteiros 6 por 6 e um valor inteiro qualquer, 
# posteriormente multiplicar a matriz pelo valor lido e colocar o resultado na própria matriz.
matriz = [[0 for coluna in range(6)] for linha in range (6)]
mult = [[0 for coluna in range(6)] for linha in range (6)]
for coluna in range (0,6):
    for linha in range(0,6):
        matriz[coluna][linha] = int(input(f'Digite o valor da C[{coluna}] , L[{linha}]: '))
print()
n = int(input('Digite um numero inteiro para multplicar a matriz: '))
print()
for coluna in range (0,6):
    for linha in range(0,6):
        mult[coluna][linha] = n * matriz[coluna][linha]
       
print(matriz)
print(mult)        