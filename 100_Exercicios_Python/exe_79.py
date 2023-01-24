#79. Escreva um programa em C, que gere a substring de uma string original, dado a posição
#inicial e a final da substring.

print('-------- Defina uma nova String com a posição Inicial e Final --------\n')

string = input('Digite a String: ')
posicaoInicial = int(input('Digite qual posição quer que seja a Inicial: '))
posicaoFinal = int(input('Digite qual posição quer que seja a Final: '))

print(f'A substring criada a partir da String "{string}", é', string[posicaoInicial:] + string[:posicaoFinal])