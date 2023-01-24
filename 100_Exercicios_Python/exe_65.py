# 65. Faça um programa em C que leia um array de 20 inteiros e imprima o menor e o maior
# valor dentre os elementos do array, bem como suas respectivas posições.

print ("Resolva o exercicio: *65*")
print ("\n-------------------------\n")

#-------------------------------------------------#
#Declaração de variáveis e atribuição dos valores#

vetor = []

for indice in range(20):
    vetor.append(int(input(f'Digite um valor para a {indice}ª: '))) 

maior = vetor[0]
menor = vetor[0]
posicaoMaior = 0
posicaoMenor = 0

for indice in range(20):
    if vetor[indice] < menor:
        menor = vetor[indice]
        posicaoMenor = indice
    
    if vetor[indice] > maior:
        maior = vetor[indice]
        posicaoMaior = indice

print(f'\nO maior valor é o {maior} que está na posição {posicaoMaior}.')
print(f'O menor valor é o {menor} que está na posição {posicaoMenor}.')