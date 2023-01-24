# 71. Escreva um programa que leia um vetor de 10 posições de inteiros e um inteiro. O programa deve informar a primeira posição onde este inteiro ocorre no vetor ou -1 caso o valor não ocorra no vetor (Busca Sequencial).

numero = int(input('Digite um número: '))

lista = []
for contador in range(0,3):
    lista.append(int(input(f'Digite o valor da posição {contador}: ')))

for i in range(len(lista)):  
  if lista[i] == numero:
      print(f'O número informado se encontra na posição {[i]} da lista.')
  else:
     print(-1)
      