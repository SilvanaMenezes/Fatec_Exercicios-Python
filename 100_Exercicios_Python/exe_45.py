# 45. Escreva um programa que leia 5 números, e imprima a média entre eles.

num = [0,0,0,0,0,0]
soma = 0
i = 1
while i < 6:
  num[i] = int(input('Digite o número %d: '% i))
  soma += num[i]
  i += 1

media = soma / 5  

print(f'A média dos números informados é: {media}')




