#77. Escreva um programa em C, que leia uma string, gere uma nova string com o texto invertido e imprima esta nova string.
print('--'*10, 'Invertendo as Palavras','--'*10)
frase = str(input('\nDigite uma palavra: ')).upper().strip()
palavra = frase.split()
juntar = ''.join(palavra)
inverso = ''

for letra in range(len(juntar)-1, -1, -1): 
    inverso += juntar[letra]
print(f'\nA palavra "{juntar}" ao contrario fica: {inverso}\n')