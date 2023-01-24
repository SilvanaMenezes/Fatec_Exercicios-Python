#61.Faça um programa em C que crie e inicialize um array de 20 posições de inteiros com 0 para cada elemento.
#  Imprima o vetor em seguida, indicando a posição e o valor na posição (um por linha). 
vetor =[]
for c in range(0, 21): 
    n = int(input(f'Digite o valor na [{c}] posição: '))
    vetor.append(n)
print()    
print('=='*5, 'Mostrando valores e posição','=='*5)
print()
for i, v in enumerate(vetor):   
    print(f'Na posição [ {i} ] encontrei os valores -> {v} ') 
print()
print('=='*7, 'fim das posições', '=='*7)    