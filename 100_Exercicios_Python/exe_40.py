# 40. Escreva um programa que receba um numero inteiro de 1 a 100 e mostre na tela o numero por extenso

unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']

dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

numero = int(input('Digite um número de 01 à 100: '))

#Separando o número em unidade e dezena
unidadeNum = numero // 1 % 10
dezenaNum = numero // 10 % 10

#Números com unidade e dezena Maiores que 10 e diferente de 0 no final
if (dezenaNum >= 2) and (unidadeNum != 0):
  dezenaExtenso = dezenas[dezenaNum]
  unidadeExtenso = unidades[unidadeNum]
  print(f'O número {numero} por extenso é: {dezenaExtenso} e {unidadeExtenso}.')

#Numeros com dezena maior que dez e unidade igual a 0
if (dezenaNum >=2) and (unidadeNum == 0):
  dezenaExtenso = dezenas[dezenaNum]
  print(f'O número {numero} por extenso é: {dezenaExtenso}.')

#Numeros com dezena igual a 1 ou 0 e unidade igual ou maior que 0
if (dezenaNum == 1 ) or (dezenaNum == 0) and (unidadeNum >= 0):
  numeroExtenso = unidades[numero]
  print(f'O número {numero} por extenso é: {numeroExtenso}.')

if numero == 100:
  print(f'O número {numero} por extenso é: cem')