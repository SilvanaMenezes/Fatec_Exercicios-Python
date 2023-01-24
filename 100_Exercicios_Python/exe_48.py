# 48. Escreva um programa que determine se um dado número N (digitado pelo usuário) é
# primo ou não

print ("Resolva o exercicio: *48*")
print ("\n-------------------------\n")

#-------------------------------------------------#
#Declaração de variáveis, atribuição dos valores 

numero = int(input("Digite um número: "))

#--------------------------------------------------#
#Exibindo os valores na tela

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print("\n""(",numero,")" " não é primo")
            break
    else:
        print("\n""(",numero,")" " é primo")
elif numero == 0:
    print("\n""(",numero,")" " é zero")
elif numero == 1:
    print("\n""(",numero,")" " é um")
else:
    print("\n""(",numero,")" " é negativo")