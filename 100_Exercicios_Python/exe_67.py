# 67. Faça um programa em Python que leia dois vetores de 10 posições de inteiros e copie o maior valor dos dois em cada posição em um terceiro vetor. Em seguida, imprima este terceiro vetor.

listaA = []
listaB = []
listaC = []

print('='*20, 'Incluindo valores da listaA', '='*20, '\n')

for contador in range(0,10):
    listaA.append(int(input(f'Digite o valor da posição {contador+1}: ')))
    

print('='*20, 'Incluindo valores da listaB', '='*20, '\n')

for contador in range(0,10):
    listaB.append(int(input(f'Digite o valor da posição {contador+1}: ')))
    
    if listaA[contador] > listaB[contador]:
        listaC.append(listaA[contador])
        
    else:
        listaC.append(listaB[contador])
            
print(f'Os maiores valores digitados preenchem a listaC = {listaC}.')



