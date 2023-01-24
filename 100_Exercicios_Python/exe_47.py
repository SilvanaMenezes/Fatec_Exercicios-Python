# 47. Escreva um programa que calcule o resto da divisão de A por B (número inteiros e
# positivos), ou seja, A % B, através de subtrações sucessivas. Esses dois valores são
# passados pelo usuário através do teclado

print ("Resolva o exercicio: *47*")

print ("\n-------------------------\n")

#-------------------------------------------------#
#Declaração de variáveis e atribuição dos valores

A = int(input("Informe o valor de (A): ")) #(A) -> Dividendo
B = int(input("Informe o valor de (B): ")) #(B) -> Divisor

#--------------------------------------------------#
#Exibindo os valores na tela

Dividendo = A

while (Dividendo >= B): 
    Dividendo = Dividendo - B
  
print("\nO resto da divisão de A por B é =", Dividendo)