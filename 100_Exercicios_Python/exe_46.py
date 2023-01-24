# 46. Escreva um programa que calcule o quociente da divisão de A por B (número inteiros e
# positivos), ou seja, A / B, através de subtrações sucessivas. Esses dois valores são
# passados pelo usuário através do teclado.

print ("Resolva o exercicio: *46*")

print ("\n-------------------------\n")

#-------------------------------------------------#
#Declaração de variáveis e atribuição dos valores

A = int(input("Informe o valor de (A): ")) #(A) -> Dividendo
B = int(input("Informe o valor de (B): ")) #(B) -> Divisor

#--------------------------------------------------#
#Exibindo os valores na tela

Dividendo = A
Quo = 0

while (Dividendo >= B): 
    Quo = Quo + 1
    Dividendo = Dividendo - B
  
print("\nO quociente da divisão de A por B é =", Quo)