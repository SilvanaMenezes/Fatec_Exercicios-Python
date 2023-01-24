#68. Escreva um programa que leia o índice pluviométrico de cada dia do mês de junho e
# informe o dia que mais choveu, o dia que menos choveu e as médias pluviométricas de
#cada uma das duas quinzenas.

print('-------- Índice Pluviométrico do mês de Junho --------\n')

diasJunho = []
indice = 0
posicaoDia = 1

for indice in range(30):
    diasJunho.append(int(input(f'Digite o Índice Pluviométrico do {posicaoDia}º dia: ')))
    posicaoDia += 1

#Definindo qual o Maior Indice e o que Menor Indice

menorIndicePluvio = diasJunho[0]
maiorIndicePluvio = diasJunho [0]

for indice in range(30):   
    if maiorIndicePluvio < diasJunho[indice]:
        maiorIndicePluvio = diasJunho [indice]

    if menorIndicePluvio > diasJunho[indice]:
        menorIndicePluvio = diasJunho [indice]

#Identificando o Dia do Maior e Menor Indice

posicaoDiaMaior = 0
posicaoDiaMenor = 0

for indice in range(30):
    posicaoDiaMaior += 1
    posicaoDiaMenor += 1
    
    if diasJunho[indice] == maiorIndicePluvio:
        print('\nMaior Indice Pluviométrico de Junho 2022')
        print(f'O dia {posicaoDiaMaior}, com Indice de {maiorIndicePluvio} mm.')

    if diasJunho[indice] == menorIndicePluvio:
        print('\nMenor Indice Pluviométrico de Junho 2022')
        print(f'O dia {posicaoDiaMenor}, com Indice de {menorIndicePluvio} mm.')

#Media das quinzenas

somaIndices1quin = 0
somaIndices2quin = 0

for indice in range(30):   
    
    if indice <= 15:
        somaIndices1quin = somaIndices1quin + diasJunho[indice]
        mediaIndices1quin = somaIndices1quin / 15

    if indice > 15:
        somaIndices2quin = somaIndices2quin + diasJunho[indice]
        mediaIndices2quin = somaIndices2quin / 15


print(f'\nA média do Indice Pluviometrico da 1ª Quinzena de Junho é {round(mediaIndices1quin)} mm.')
print(f'A média do Indice Pluviometrico da 2ª Quinzena de Junho é {round(mediaIndices2quin)} mm.')