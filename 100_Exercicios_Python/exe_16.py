# 16. Escreva um programa para gerar o invertido de um número com três algarismos
# (exemplo: o invertido de 498 é 894).

print ("Resolva o exercicio: *16*")
print ("\n-------------------------\n")

#-------------------------------------------------#
#Declaração de variáveis e atribuição dos valores#

valor = 789
unidade = valor % 10
dezena = (valor % 100) // 10
centena = valor // 100
#--------------------------------------------------#
#Exibindo os valores na tela

print ("Valor =", valor)
print (f"\nValor ao contrário = {unidade}{dezena}{centena}")