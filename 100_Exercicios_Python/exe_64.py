#64. Faça um programa em C que leia um array de 20 inteiros e imprima o menor e o maior valor dentre os elementos do array

print('-------- Array de 20 elementos --------\n')

vetor = []
posicao = 0

for posicao in range (20):
   vetor.append(int(input(f'Digite o número da posição {posicao}ª : ')))

#Maior e Menor dentro do Array

maior = vetor[0]
menor = vetor[0]

for posicao in range(20):
    if maior < vetor[posicao]:
        maior = vetor[posicao]
    
    if menor > vetor [posicao]:
        menor = vetor [posicao]

print(f'\nO maior valor do vetor é {maior}\nE o menor valor é {menor}.')
