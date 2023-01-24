#84. Escreva um programa em C que verifique se uma string normalizada é palíndrome
#  (os mesmos caracteres quando lida da direita para a esquerda ). 
#(.strip - eliminação do espaço entre as palavras; .upper - transforma todas as letra em letras maiúsculas
# "palavras = texto.split - cria uma lista .split - separa as palavras - 'ceu', 'azul' "
# (len(juntar) -1 *ultima letra*, -1 *até a primeira letra*, -1 *volta yma letra*) )

texto = str(input('Digite digite uma frase: ')).strip().upper()
palavras = texto.split()
juntar = ''.join(palavras)
inverter = ''
print('-'*30)
for letra in range(len(juntar) -1, -1, -1):
    inverter += juntar[letra]
if inverter == juntar:
    print('--- Temos um palídromo! ---')
else: 
    print('--- A frase digitada não é um palídromo! ---')    
print('<-- --> '*10)
print(f'Você digitou [{juntar}]\n','Sua frase invertida: ', inverter)
