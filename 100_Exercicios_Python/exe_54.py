# 54. Construa um programa que receba um número e verifique se ele é um número triangular.
# (Um número é triangular quando é resultado do produto de três números consecutivos.
# Exemplo: 24 = 2 x 3 x 4)

print ("Resolva o exercicio: *54*")
print ("\n-------------------------\n")

#-------------------------------------------------#
#Declaração de variáveis, atribuição dos valores 

numero = int(input("Digite um número: "))

#--------------------------------------------------#
#Exibindo os valores na tela

i = 1
t = 0

while t < numero:
	t = i*(i+1)*(i+2)
	i += 1

if t == numero:
	print ("\n%d é triangular" %numero)
else: 
	print ("\n%d não é triangular" %numero)

