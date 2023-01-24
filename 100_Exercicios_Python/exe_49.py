# 49. Escreva um programa que determine se um dado número N (digitado pelo usuário) é primo ou não.

n = int(input('Digite um número: '))
divisores = 0

for count in range(1,n + 1):
  if n % count == 0:
    divisores += 1   

if divisores == 2:
  print('É primo')
else: 
  print('Não é primo')
