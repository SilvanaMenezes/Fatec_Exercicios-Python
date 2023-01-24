#63. Escreva um programa que leia dois vetores de números reais de mesma dimensão (10 posições), 
# e imprima o vetor resultante da soma destes vetores. 

vetor = []
soma = 0
for c in range(1, 11):
    vetor.append(float(input(f'Digite um número para a posição  [ {c} ] -> ')))
    
print()
for c in range(1, 11):
    soma = vetor[c] + vetor[c]
#soma
for item in soma:
    print(f'soma dos vetores {item}', end=' ') 

print()    
