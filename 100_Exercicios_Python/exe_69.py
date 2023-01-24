#69. Escreva um programa que leia um vetor de 15 posições de inteiros. Em seguida, 
# o programa deve ler um valor inteiro e imprimir o -- número de vezes que este valor ocorre no vetor--  
vetor = []
repeticao = 0
for c in range (1, 15):
    vetor.append(int(input(f'Digite um numero para a posição [ {c}ª ]: ')))
vetor.sort()
print()
print('=='*20)
for c in range (0, len(vetor)-1):
    if vetor[c] == vetor[c + 1]:
        repeticao += 1
        if c == len(vetor) -2:
            print('os valores', vetor[c], 'se repetiu', repeticao+1)
    else:
        print('os valores [',vetor[c],'] se repetiu', repeticao+1)
        repeticao = 0
