#91. Elabore um programa em C que leia valores inteiros para preencher uma matriz A 5 x 5.
#  Você deverá criar adicionalmente dois vetores de 5 elementos: somaLinhas e somaColunas.
#  Em cada posição do vetor somaLinhas deverá ser armazenada a soma da linha correspondente na matriz A. 
# Da mesma forma, em cada posição do vetor somaColunas deverá ser armazenada a soma da coluna correspondente na matriz A.

matrizA = [[0 for coluna in range(5)] for linha in range (5)]
somaLinha = []
somaColuna = []
for linha in range(5):
    for coluna in range (5):
        matrizA[coluna][linha] =(int(input(f'Digite um número para coluna {coluna}  e linha {linha}: ')))

#soma linha
for coluna in range(5):
    soma = 0
    for linha in range(5):
        soma += matrizA[linha][coluna]

    linha = soma   
    somaLinha.append(linha)
        
#soma coluna
for linha in range(5):
    soma = 0
    for coluna in range(5):
        soma += matrizA[linha][coluna]

    coluna = soma    
    somaColuna.append(coluna)


print(matrizA)
print(f'\nSoma das Linha: {somaLinha}')
print(f'\nSoma das Colunas {somaColuna}')