#37. Uma Cia de pulverização utiliza avião para pulverizar lavouras. Os custos de
#pulverização dependem do tipo de praga e da área a ser contratada conforme a tabela:
#Tipo 1 – ervas daninhas R$ 50,00 por acre;
#Tipo 2 – gafanhotos R$ 100,00 por acre;
#Tipo 3 – broca R$ 150,00 por acre;
#Tipo 4 – todos acima R$ 250,00 por acre.
#Se a área a ser pulverizada for superior a 1000 acres, o fazendeiro tem um desconto de
#5%. Em adição, qualquer fazendeiro cujo custo for maior do que R$ 750,00 tem um
#desconto de 10% sobre o valor que ultrapassar os R$ 750,00. Caso ambos os descontos se
#aplicam o da área é calculado antes. Fazer um algoritmo que leia: o tipo de pulverização
#(1 a 4) e área a ser pulverizada; e imprima o valor a ser pago.

print ('-------- Custos de pulverização --------\n')

area_pul = float(input('Quantos acres você deseja pulverizar?\n'))
qualTipo = input('Digite qual tipo de pulverização deseja:\n\nTipo 1 - Ervas Daninhas\nTipo 2 - Gafanhotos\nTipo 3 - Broca\nTipo 4 - Todos acima\n\nDigite 1,2,3 ou 4: ')

desconto5 = 5 / 100
desconto10 = 10 / 100

#Definindo o valor de cada
if qualTipo == '1':
    qualTipo = 50
    preco = area_pul * 50

elif qualTipo == '2':
    qualTipo = 100
    preco = area_pul * 100

elif qualTipo == '3':
    qualTipo = 150
    preco = area_pul * 150

elif qualTipo == '4':
    qualTipo = 250
    preco = area_pul * 250
else:
    print('\nOpção incorreta, por favor digite uma opção válida.')

#Valor com os descontos
if area_pul > 1000:
    desconto1 =  ( preco * desconto5 )
    print('\nO valor da Pulverização é de R$ ' , preco)
    print('O valor do desconto aplicado é de R$ ' , desconto1)
    print('O valor final da pulverização é de R$ ' , preco - desconto1)

if preco > 750:
    desconto2 = ( (preco - 750) * desconto10 )
    print('\nO valor da Pulverização é de R$ ' , preco)
    print('O valor do desconto aplicado é de R$ ' , desconto2)
    print('O valor final da pulverização é de R$ ' , preco - desconto2)




