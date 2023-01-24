#78. Escreva um programa em C, que leia uma string e um caracter e conte o número de
#ocorrências do caracter lido na string.

print('-------- Quantas letras tem na String --------\n')

string = input('Digite a String a ser analisada: ')
letra = input('Digite a Letra que deseja procurar: ')

posicao = 0
contador = 0

for posicao in string:
    if posicao == letra.lower():
        contador +=1

print(f'\nA quantidade que a letra "{letra}" se repete na palavra {string} é de: {contador}')