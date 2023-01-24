# 15. Num dia de sol, você deseja medir a altura de um prédio, porém, a trena não é
# suficientemente longa. Assumindo que seja possível medir sua sombra e a do prédio no
# chão, e que você lembre da sua altura, faça um programa para ler os dados necessários e
# calcular a altura do prédio

print ("Resolva o exercicio: *15*")

print ("\n-------------------------\n")

#-------------------------------------------------#
#Declaração de variáveis e atribuição dos valores

Spredio = float (input("Informe o tamanho da sombra do prédio: "))
Susuario = float (input("Informe o tamanho da sombra do usuário: "))
Ausuario = float (input("Informe altura do usuário: "))

#--------------------------------------------------#
#Exibindo os valores na tela
sombraP = (Spredio / Susuario)
alturaP = (sombraP * Ausuario)

print(f"\nAltura do prédio é =  {alturaP:.1f} metros")