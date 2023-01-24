#62.Faça um programa em C que leia um array de 10 posições e conte quantos números pares são elementos do array.
#  Imprima esta quantidade
vetor = []
contador = 0
for c in range(0, 11):
    n = int(input(f'Digite um número para a posição {c} : '))
    vetor.append(n)
    
print()
print('=='*8, 'Valor das posições', '=='*8)
print()
for i,v in enumerate(vetor):
    print(f'Na posição [ {i} ] encontrei o valor -> {v}')
print()
for i,v in enumerate(vetor):
    if v % 2==0:
        print(f'Valores pares são -> {v} gravado na posição [ {i} ] \n')
        contador = contador + 1

print(f' Total de pares é -> {contador} \n')
print('=='*8, 'Fim posição', '=='*8 )
