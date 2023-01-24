# 95. Escrever um algoritmo e implementá-lo em linguagem C que linearize uma matriz de 6
# por 6, colocando os valores contidos nela em um vetor de 36 elementos e mostrar o
# conteúdo do vetor.

#Declarando a matriz
matriz = [[0] * (6) for _ in range(6)]

# Adicionando valores na matriz
coluna = 0
for coluna in range(6) :
    for linha in range(6) :
        matriz[coluna][linha] = int(input(f'Digite o valor de C[{coluna}] , L[{linha}]: '))
vetor = [0] * (36)
indice = 0
coluna = 0
linha = 0
for coluna in range(6) :
    for linha in range(6) :
        vetor[indice] = (matriz[coluna][linha])
        indice += 1

#Mostrando os valores em matriz   
print('\nOs numeros da Matriz mostrados em Vetor')

coluna = 0
while (coluna < indice) :
    print(vetor[coluna])
    coluna += 1