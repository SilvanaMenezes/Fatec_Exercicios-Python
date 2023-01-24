# 55. Dizemos que dois números são amigos se cada um deles é igual a soma dos divisores
# próprios do outro. Os divisores próprios de um número positivo N são todos os divisores
# inteiros positivos de N exceto o próprio N. Um exemplo de números amigos são 284 e
# 220, pois os divisores próprios de 220 são 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 e 110.
# Efetuando a soma destes números obtemos o resultado 284 (1 + 2 + 4 + 5 + 10 + 11 + 20
# + 22 + 44 + 55 + 110 = 284). Os divisores próprios de 284 são 1, 2, 4, 71 e 142,
# efetuando a soma destes números obtemos o resultado 220 (1 + 2 + 4 + 71 + 142 = 220).
# Escreva um programa que dado dois inteiros, verifique se eles são amigos. (17296 e
# 18416 são amigos, por exemplo).

print('-------- Os números são amigos? --------\n')

while True:
    num1 = int(input('\nDigite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    divisoresNum1 = 0
    divisoresNum2 = 0
    indice = 1

#Somando os divisores com resto 0 dos dois números
    for indice in range (1,num1):
        if num1 % indice == 0:
         divisoresNum1 = divisoresNum1 + indice

    for indice in range(1,num2):
        if num2 % indice == 0:
            divisoresNum2 = divisoresNum2 + indice

#Verificando se o divisor do número 1 e numero 2 dão os números
    if (divisoresNum1 == num2) and (divisoresNum2 == num1):
        print(f'\nO número {num1} e o {num2} são amigos.')
    else:
        print(f'\nO número {num1} e o {num2} não são amigos.')

#Caso o usuário não queira mais testar se os Números são amigos
    resposta = input('\nDeseja verificar outros números?  S/N \n' )
    if resposta.upper() == 'N':
        break