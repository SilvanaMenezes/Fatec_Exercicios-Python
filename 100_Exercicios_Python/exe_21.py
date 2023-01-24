# 21. Escreva um programa que leia um número e exiba se ele é positivo ou negativo.

print ("Resolva o exercicio: *21*")
print ("\n-------------------------\n")

#-------------------------------------------------#
#Declaração de variáveis, atribuição dos valores

n = int(input("Digite um número: "))

#--------------------------------------------------#
#Exibindo os valores na tela

if n > 0:
  print ("\nNúmero Positivo")
elif (n == 0):
  print ("\nNúmero Neutro")
else:
  print("\nNúmero Negativo")
