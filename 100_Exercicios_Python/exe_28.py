# 28. Escreva um programa que leia uma letra e mostre se ela é vogal ou consoante.

print ("Resolva o exercicio: *28*")
print ("\n-------------------------\n")

#-------------------------------------------------#
#Declaração de variáveis, atribuição dos valores 

letra = str(input("Digite uma letra: "))

#--------------------------------------------------#
#Exibindo os valores na tela

if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
  print ("\nA letra", "(",letra,")", "é uma vogal")
elif (letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
   print ("\nA letra", "(",letra,")", "é uma vogal")
else:
  print ("\nA letra", "(",letra,")", "é uma consoante")
