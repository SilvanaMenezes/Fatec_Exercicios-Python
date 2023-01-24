# 50. Escreva um programa que leia um valor e imprima todas as possíveis combinações em
# que o lançamento de um par de dados tenha como resultado da soma dos valores dos
# dados o número lido. Por exemplo, se a entrada for o número 7, o programa deve
# imprimir as seguintes combinações:
#  1 6
#  2 5
#  3 4
#  4 3
#  5 2
#  6 1


print ("Resolva o exercicio: *50*")
print ("\n-------------------------\n")

#-------------------------------------------------#
#Declaração de variáveis, atribuição dos valores 

numero = int(input("Digite um número: "))

#--------------------------------------------------#
#Exibindo os valores na tela

lado1 = 1
lado2 = 2
lado3 = 3
lado4 = 4
lado5 = 5
lado6 = 6

if (numero == 1 or numero > 12):
    print ("Não existe combinação")

elif (numero == 2):
    print ("\nCombinação")
    print (lado1, "", lado1)
elif (numero == 3):
    print ("\nCombinação")
    print (lado1, "", lado2)
    print (lado2, "", lado1)
elif (numero == 4):
    print ("\nCombinação")
    print (lado1, "", lado3)
    print (lado2, "", lado2)
    print (lado3, "", lado1)
elif (numero == 5):
    print ("\nCombinação")
    print (lado1, "", lado4)
    print (lado2, "", lado3)
    print (lado3, "", lado2)
    print (lado4, "", lado1)
elif (numero == 6):
    print ("\nCombinação")
    print (lado1, "", lado5)
    print (lado5, "", lado1)
    print (lado2, "", lado4)
    print (lado4, "", lado2)
    print (lado5, "", lado1)
    print (lado1, "", lado5)
elif (numero == 7):
    print ("\nCombinação")
    print (lado1, "", lado6)
    print (lado2, "", lado5)
    print (lado3, "", lado4)
    print (lado4, "", lado3)
    print (lado5, "", lado2)
    print (lado6, "", lado1)
elif (numero == 8):
    print ("\nCombinação")
    print (lado4, "", lado4)
    print (lado6, "", lado2)
    print (lado3, "", lado5)
    print (lado2, "", lado6)
    print (lado5, "", lado3)
elif (numero == 9):
    print ("\nCombinação")
    print (lado6, "", lado3)
    print (lado3, "", lado6)
    print (lado4, "", lado5)
    print (lado5, "", lado4)
elif (numero == 10):
    print ("\nCombinação")
    print (lado5, "", lado5)
    print (lado6, "", lado4)
    print (lado4, "", lado6)
elif (numero == 11):
    print ("\nCombinação")
    print (lado5, "", lado6)
    print (lado6, "", lado5)
elif (numero == 12):
    print ("\nCombinação")
    print (lado6, "", lado6)

