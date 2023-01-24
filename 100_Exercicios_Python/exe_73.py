# 73. Escreva um programa em C que leia um array de 20 inteiros, calcule e imprima:
# a. A moda dos elementos no array (elemento mais freqüente).
# b. A mediana dos elementos no array (elemento central)
# c. A média

print('-------- Moda, Mediana e Média de um Array --------\n')

import statistics  as sts

moda = 0
mediana = 0
soma = 0
vetor = []
posicao = 1

for posicao in range(1,21):
    vetor.append(int(input(f'Digite um número para a {posicao}ª posição: ')))

#Perguntando ao usuário como ele quer ordenar o vetor
while True:
    resposta = input('\nVocê deseja ordenar o vetor em ordem crescente ou decrescente?\n\n Digite C para Crescente\n Digite D para Decrescente\n\nR: ')

    if resposta.upper() == 'C':
        vetor.sort()
        break
    elif resposta.upper() == 'D':
        vetor.sort(reverse = True)
        break
    else:
        print('\nATENÇÃO: Opção Inválida.')

#Moda, Mediana e Média
print(f'\nO vetor:\n{vetor}\n')

moda = sts.mode(vetor)
print(f'A Moda do vetor é {moda}.')

mediana = sts.median(vetor)
print(f'A Mediana do vetor é {mediana}.')

for posicao in range (20):
    soma = soma + vetor[posicao]

media = soma / 20    
print(f'A Média do vetor é {media: .2f}.')