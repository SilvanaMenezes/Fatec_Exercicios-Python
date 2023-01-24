# 35. Escreva um programa que leia um número inteiro de 1 a 7 e informe o dia da semana correspondente, sendo domingo o dia de número 1. Se o número não corresponder a um dia da semana, mostre uma mensagem de erro.	

num = int(input('Informe um número de 1 a 7: '))

if num == 1:
  print('domingo')

if num == 2:
  print('segunda')

if num == 3:
  print('terça')

if num == 4:
  print('quarta')

if num == 5:
  print('quinta')

if num == 6:
  print('sexta')

if num == 7:
  print('sabado')

if num > 7:
  print('o número digitado não é válido.')

