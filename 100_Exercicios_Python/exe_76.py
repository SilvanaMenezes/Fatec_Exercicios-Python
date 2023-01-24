#76. Escreva um programa em C, que leia uma string e conte quantas ocorrências de vogais
#existem nesta string.

print('-------- Quantas vogais existem em uma String --------\n')

string = input('Digite a String a ser analisada: ')

contadorDeVogais = 0

for letra in string:
    if letra.lower() in 'aáãâàeéêiíoóuù':
        contadorDeVogais +=1

print(f'\nA palavra {string} tem {contadorDeVogais} vogais.')



