# 34. Uma financeira usa o seguinte critério para conceder empréstimos: o valor total do
# empréstimo deve ser até dez vezes o valor da renda mensal do solicitante e o valor da
# prestação deve ser no máximo 30% da renda mensal do solicitante. Escreva um programa
# que leia a renda mensal de um solicitante, o valor total do empréstimo solicitado e o
# número de prestações que o solicitante deseja pagar e informe se o empréstimo pode ou
# não ser concedido.

print ("Resolva o exercicio: *34*")
print ("\n-------------------------\n")

#-------------------------------------------------#
#Declaração de variáveis, atribuição dos valores

valor = float (input("Digite o valor do emprestimo solicitado: R$"))
salario = float (input("Digite o salario mensal: R$"))
anos = int (input("Quantos anos para pagar: "))

#--------------------------------------------------#
#Exibindo os valores na tela

meses = anos * 12
prestacao = valor / meses

if (prestacao > salario * 0.3):
  print ("\nInfelizmente voce não poderá ter o empréstimo")
else:
  print ("\nValor da prestação R$", prestacao, "(Empréstimo OK)")