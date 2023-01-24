# 100. Verificar se uma matriz dada forma um Quadrado Latino de ordem N, no qual
# em cada linha e em cada coluna aparecem todos os inteiros 1,2,3, ... N, ou seja, cada linha
# ou coluna é permutação dos N primeiros números inteiros

print('-------- Quadrado Latino --------\n')

tamanhoMatriz = int(input('Digite um número para determinar o tamanho para sua matriz: '))

matriz = [[0 for coluna in range (tamanhoMatriz)] for linha in range (tamanhoMatriz)]

#Preenchendo Matriz
for linha in range(0, tamanhoMatriz):
    for coluna in range(0, tamanhoMatriz):
        matriz[linha][coluna] = int(input(f'Digite o valor da C[{coluna}] , L[{linha}]: ')) 

#Mostrando a Matriz
print()
    
for indice in range (tamanhoMatriz):
    print(matriz[indice])

#Verificando se os valores das linhas > 0 tem o valor da linha 0
prosseguir = 1

indice = 0
for linha in range (tamanhoMatriz):
    for indice in range(1,tamanhoMatriz):
        if indice not in matriz[linha]:
            prosseguir = 0
    
if prosseguir == 0:
    print(f'\nNão é um Quadrado Latino, pois os valores da primeira linha não estão nas demais.')

#Verificando se é Quadrado Latino
if prosseguir != 0:
    coluna = 0
    linha = 0
    colunaConferencia = 1
    linhaConferencia = 1
    numeroLinhasRepetidas = 0
    numeroColunasRepetidas = 0

    #Checando linha
    for linha in range (tamanhoMatriz -1):
        if (matriz[linha][coluna] == matriz[linhaConferencia][coluna]):
            numeroLinhasRepetidas += 1
        linhaConferencia += 1

    #Checando Coluna
    for coluna in range (tamanhoMatriz -1):
        if matriz[linha][coluna] == matriz[linha][colunaConferencia]:
            numeroColunasRepetidas += 1
        colunaConferencia += 1
    
    if (numeroLinhasRepetidas == 0) and (numeroColunasRepetidas == 0):
        print(f'\nÉ um Quadrado Latino.')
    else:
        print(f'\nNão é um Quadrado Latino, pois tem repetição de linhas e/ou colunas.')