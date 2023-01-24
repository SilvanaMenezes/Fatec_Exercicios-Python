# 30. Um posto está vendendo combustíveis com a seguinte tabela de descontos: Álcool Até 25 litros, desconto de 2% por litro Acima de 25 litros, desconto de 4% por litro Gasolina Até 25 litros, desconto de 3% por litro Acima de 25 litros, desconto de 5% por litro.Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,70 e o preço do litro do álcool é R$ 1,90.

A = int(input('Digite a quant/litros de álcool vendidos: '))
G = int(input('Digite a quant/litros de gasolina vendidos: '))

precoA = 1.90
precoG = 2.70

novoPrecoA = precoA * A
novoPrecoG = precoG * G

if A <= 25:
  pagarA = novoPrecoA - (novoPrecoA * 2/100)
  print(f'O cliente pagará R${pagarA} por {A} litros de álcool.')
  
if A >= 25:
    pagarA = novoPrecoA - (novoPrecoA * 4/100)
    print('O cliente pagará R${:.2f} por {} litros de álcool.'.format(pagarA,A))

if G <= 25:
  pagarG = novoPrecoG - (novoPrecoG * 3/100)
  print(f'O cliente pagará R${pagarG} por {G} litros de gasolina.')

if G >= 25:
  pagarG = novoPrecoG - (novoPrecoG * 5/100)
  print(f'O cliente pagará R${pagarG} por {G} litros de gasolina.')
