#70. Escreva um programa que carregue um array com tamanho variável. O tamanho máximo
#do array é de 100 posições (carga de array com sentinela).

print('-------- Array com tamanho variável --------\n')

vetor = []
indice = 0
limiteVetor = 100

while True:
    respostaUsuario = input('Deseja definir o tamanho do Vetor agora? S/N\n')
    if respostaUsuario in 'sSnN':
        break
    else:
        print('Digite uma opção válida.\n')

#Valor do Array Definido no inicio
if respostaUsuario.upper() == 'S':
    while True:
        vetorTamanho = int(input('\nInsira o tamanho do seu vetor: '))
        
        if vetorTamanho > limiteVetor:
            print('Por favor digite um valor menor ou igual a 100\n')
        
        else:
            for indice in range(vetorTamanho):
                vetor.append(int(input(f'Insira um valor para posição {indice}ª do vetor: ')))
            break

#Valor do Array não definido no inicio
if respostaUsuario.upper() == 'N':    
    print('\nO valor máximo a ser guardado é de até 100 posições')
    vetor.append(int(input('\nDigite o valor a ser guardado: ')))
    
    while True:
        continuar = str(input('Deseja continuar? S/N\n'))
        continuar = continuar.strip()
        continuar = continuar.upper()
        
        if continuar == 'S':
            vetor.append(int(input('\nDigite o valor a ser guardado: ')))

        elif continuar == 'N':
            print('\nValores guardados com sucesso.')
            break
        else:
            print('\nOpção inválida\nDigite S para Sim ou N para não\n')

        if limiteVetor == len(vetor):
            print('\nVocê ultrapassou o limite de 100 posições.')
            break


#Aplicando a Busca com carga de Sentinela
itemDeBusca = int(input('Digite o número que deseja encontrar: '))
print(f'\nOs valores guardados são: {vetor}')

#Adicionando a Sentinela
vetor.append(int(itemDeBusca))

indice = 0
while vetor[indice] != itemDeBusca:
    indice += 1

if indice == len(vetor) - 1:
    print('\nEncontramos a carga de Sentinela')

print(f'O valor {itemDeBusca} se encontra na {indice}ª posição do vetor.')