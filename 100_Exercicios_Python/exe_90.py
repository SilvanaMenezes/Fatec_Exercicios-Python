# 90. Escreva um programa em C, que dado uma string, crie uma nova string contendo na
# ordem em que aparecem no string dado, as vogais no começo e as consoantes no final.

print ('-------- Nova String com Vogais seguidas de Consoantes --------\n')

vetorVogais = []
vetorConsoantes = []
indice = 0

string = input('Digite uma palavra: ')

#Eliminando os spaces caso o usuario dê(strip) e convertendo as letras para minusculas(lower)
string = string.strip()
string = string.lower()

limite = len(string)

#Percorrendo as posições da palavra e colocando cada letra no vetor correspondente
for indice in range(limite):
    if (string[indice] == 'a') or (string[indice] == 'e') or (string[indice] == 'i') or (string[indice] == 'o') or (string[indice] == 'u'):
        vetorVogais.append(string[indice])
    else:
        vetorConsoantes.append(string[indice])

#Convertendo os Vetores de Vogais e Consoantes para String e mostrando a nova String
vogais = ''.join(vetorVogais)
consoantes = ''.join(vetorConsoantes)

#Deixando a primeira letra Maiuscula 
vogais = vogais.title() 

print('Sua nova String é: ' + vogais + '' + consoantes)