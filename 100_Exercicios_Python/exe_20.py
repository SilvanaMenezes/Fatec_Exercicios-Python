#Uma loja vende seus produtos no sistema entrada mais duas prestações, sendo a entrada
#maior do que ou igual às duas prestações, as quais devem ser iguais, inteiras e as maiores
#possíveis. Por exemplo, se o valor da mercadoria for R$ 270,00, a entrada e as duas
#prestações são iguais a R$ 90,00; se o valor da mercadoria for R$ 302,75, a entrada é de
#R$ 102,75 e as duas prestações são a iguais a R$ 100,00. Escreva um programa que
#receba o valor da mercadoria e forneça o valor da entrada e das duas prestações, de
#acordo com as regras acima. Observe que uma justificativa para a adoção desta regra é
#que ela facilita a confecção e o consequente pagamento dos boletos das duas prestações.

print('-------- Valor das Parcelas --------\n')

valor_mercadoria = (float(input('Digite o valor da Mercadoria: \n')))
total_parcelas = 3

prestacao1 = int(valor_mercadoria / total_parcelas)
prestacao2 = prestacao1
valor_entrada = valor_mercadoria - (prestacao1 + prestacao2)

print( '\nO valor de entrada é de: ' , round(valor_entrada,2))
print( 'O valor das prestações é de: ' , prestacao2)