# 74 Escreva um programa em Python que armazene um vetor de até 30 inteiros.
# O programa deve fornecer as seguintes operações:

vetor = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
print('\nvetor criado:\n',vetor)

# a. Inserir um elemento no final do vetor
vetor.append(31)
print('\nadicionando elemento:\n',vetor)

# b. Inserir um elemento em uma dada posição
vetor.insert(16,16)
print('\ninserindo elemento aleatório:\n',vetor)

# c. Remover um elemento de uma posição indicada
vetor.remove(0)
print('\nremovendo um elemento:\n',vetor)

# d. Remover todos elementos iguais a um valor indicado
vetor.pop(16)
print('\nremovendo elementos determinados:\n',vetor)

# e. Gerar um novo array sem duplicidades a partir deste array
vetor.copy()






