# 13. Um circuito elétrico é composto de duas resistências R1 e R2 em paralelo, e ambas em
# sequência de uma resistência R3. Faça um algoritmo para calcular a resistência
# equivalente desse circuito.

print ("Resolva o exercicio: *13*")
print ("\n-------------------------\n")

#-------------------------------------------------#
#Declaração de variáveis e atribuição dos valores#

R1 = float(input("Digite o primeiro valor do R1: ")) 
R2 = float(input("Digite o segundo valor do R2: "))
R3 = float(input("Digite o terceiro valor do R3: "))

Req = (1/R1) + (1/R2) + (1/R3) 
ReqT = 1 / Req
#--------------------------------------------------#
#Exibindo os valores na tela

print (f"\nO (Req) do circuito paralelo vai ser:\n{Req:.5f}")
print (f"\nO (ReqT) do circuito paralelo vai ser:\n {ReqT:.2f}" " Ohms")
