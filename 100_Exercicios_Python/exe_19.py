# 19. Escreva um programa que calcule a raiz de uma equação do primeiro grau

print ("Resolva o exercicio: *19*")

print ("\n-------------------------\n")

print ("=========================== ===========================")
print ("    Equação do 1º grau             Raiz da equação\n")
print ("    Formula: ax + b = 0            Formula: (-b) / a")
print ("=========================== ===========================")

#-------------------------------------------------#
#Declaração de variáveis e atribuição dos valores

a = int (input("\nDigite o valor de (a): "))
b = int (input("Digite o valor de (b): "))

#--------------------------------------------------#
#Exibindo os valores na tela

if a == 0:
  print ("\nO valor de (a) não pode ser zero!")
else:
  print ("\nA equação do 1º grau é: y -",a, ".x",b)
  raiz = (-b) / a
  print ("\nA (raiz) dessa equação vai ser =", raiz)

     