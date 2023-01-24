#75. Escreva um programa que ordene um array de inteiros de 15 posições utilizando o
#método da bolha (bubble sort).

print('-------- Array ordenado com Burbble Sort --------\n')

vetor = []
posicao = 0
repeticaoTotal = 0

for posicao in range(15):
    vetor.append(int(input(f'Digite o valor a ser guardado na {posicao}ª posição: ')))

for posicao in range(15-1):
    for posicao in range(15 -1):
        repeticaoTotal += 1
        if vetor[posicao] > vetor[posicao + 1]:
            vetor[posicao] , vetor[posicao + 1] = vetor [posicao + 1] , vetor [posicao]

print(f'\nTivemos que repetir o loop {repeticaoTotal} vezes.\nOs vetores ordenados com o Burbble Sort ficam assim: {vetor}')
