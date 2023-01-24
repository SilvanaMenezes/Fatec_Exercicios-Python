# 96. Escrever um algoritmo e implementá-lo em linguagem Python que leia duas matrizes de valores inteiros 3 por 4 e crie uma terceira matriz, que seja a soma das duas primeiras, e uma quarta, que seja a diferença entre a primeira e a segunda. Mostrar as matrizes lidas e calculadas

L = 3 
C = 4 
matrixA = [] 
matrixB = [] 
matrixSoma = [] 
matrixSubtração = []

for l in range(L):
  numero = []
  for c in range(C):
    numero.append(int(input("Digite o número da {}°Linha e {}°Coluna na matriz A: ".format(l+1, c+1)))) 
    matrixA.append(numero)
print()
        
for l in range(L): 
  numero = [] 
  for c in range(C): 
    numero.append(int(input("Digite o número da {}°Linha e {}°Coluna da matriz B: ".format(l+1, c+1)))) 
    matrixB.append(numero)        
print() 

print("Matrix A")
for l in range(L):
  for c in range(C):
    print(matrixA[l][c], end=" | ")
print()
        
print()

print("Matrix B") 
for l in range(L): 
  for c in range(C): 
    print(matrixB[l][c], end=" | ") 
print() 
 
print() 

for l in range(L): 
  numero = [] 
  for c in range(C): 
    numero.append(matrixA[l][c] + matrixB[l][c]) 
    matrixSoma.append(numero)
print() 
        
print("Matrix Soma") 
for l in range(L): 
  for c in range(C): 
    print(matrixSoma[l][c], end=" | ") 
print() 

print() 

for l in range(L): 
  numero = [] 
  for c in range(C): 
    numero.append(matrixA[l][c] - matrixB[l][c]) 
    matrixSubtração.append(numero)
print() 
        
print("Matrix Subtração") 
for l in range(L): 
  for c in range(C): 
    print(matrixSubtração[l][c], end=" | ") 
print()													