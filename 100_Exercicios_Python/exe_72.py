# 72. Escreva um programa que leia um vetor de 10 posições ordenados de inteiros e um
# inteiro. O programa deve informar a primeira posição onde este inteiro ocorre no vetor ou
# -1 caso o valor não ocorra no vetor (Busca Binária).

print('-------- Busca Binária --------\n')

vetor = [1,2,3,4,5,6,7,8,9,10]

print(vetor)
itemDeBusca = int(input('Digite o valor que deseja encontrar: '))

comeco = 0 
fim = len(vetor) - 1

indice = 0

#Dividir a lista no meio
while indice < len (vetor):
    if comeco <= fim:
        meio = (comeco + fim) // 2
        if vetor[meio] == itemDeBusca:
            print(f'\nO item que você busca está no {meio}º indice')
            break
    
    if itemDeBusca < vetor[meio]:
        comeco = comeco
        fim = meio -1
    
    if itemDeBusca > vetor[meio]:
        comeco = meio + 1
        fim = fim

        indice += 1

if vetor[meio] != itemDeBusca:
    print(f'\n-1 : O valor que busca não existe na lista')

    
        
            