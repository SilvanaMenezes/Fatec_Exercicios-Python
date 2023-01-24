# 66. Faça um programa em Python que copie o conteúdo de um vetor de 10 posições de inteiro em um segundo vetor e imprima este último.

lista = []
for contador in range(0,10):
  lista.append(int(input(f'Digite o valor para a posição{contador+1}: ')))

print('lista digitada = ',lista)

listaCopiada = lista[:]
print('cópia da lista =',listaCopiada)