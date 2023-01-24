# 33. Escreva um algoritmo que leia 2 valores (x e y), que devem representar as coordenadas
# de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o
# ponto, ou se está sobre um dos eixos cartesianos ou na origem (x=y=0).

print ("Resolva o exercicio: *33*")

print ("\n-------------------------\n")

#-------------------------------------------------#
#Declaração de variáveis e atribuição dos valores#

x = int(input("Digite o primeiro valor de X: "))
y = int(input("Digite o segundo valor de Y: "))

#--------------------------------------------------#
#Exibindo os valores na tela

if (x > 0 and y > 0):
    print("\nPrimeiro Quadrante")
elif (x < 0 and y > 0):
    print ("\nSegundo Quadrante")
elif (x < 0 and y < 0):
    print ("\nTerceiro Quadrante")
elif (x > 0 and y < 0):
    print ("\nQuarto Quadrante")
elif (x == 0 and y > 0 or y < 0):
    print ("\nEstá no eixo Cartesiano")
elif (y == 0 and x > 0 or x < 0):
    print ("\nEstá no eixo Cartesiano")
else:
    print("\nOrigem")