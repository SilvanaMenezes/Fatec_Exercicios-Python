# 83. Escreva um programa em Python, que gere a substring de uma string original, dado a posição inicial e a final da substring.

string = str(input('Digite uma string: ')).strip()

print('Sua string tem {} caracteres.'.format(len(string)))

print('--- Gerando uma substring a partir da string digitada. ---')

posicaoInicial = int(input('posição inicial: '))
posicaoFinal = int(input('posição final: '))

substring = string[posicaoInicial] + string[posicaoFinal]
print(f'A substring criada é: {substring}')

