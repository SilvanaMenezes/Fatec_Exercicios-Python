# #31. No Futebol Americano, usa-se o Quarterback Rating como um índice que indica o
# #desempenho do quarterback (quando maior, melhor). Ele é calculado como indicado a
# #seguir: Calcula-se o percentual de passes completados em relação aos passes tentados
# ##pelo quarterback. Deste valor subtrai-se 0,3 e divide-se por 0,2. Este valor não deve ser
# #aior que 2,375 ou menor que 0 (caso seja, ajusta-se o valor para 2,375 ou 0,
# respectivamente).
# Em seguida, calcula-se a razão de jardas passadas pela quantidade de passes tentados.
# Deste valor, subtrai-se 3 e divide-se por 4. Novamente, este valor não deve ser maior que
# 2,375 ou menor que 0 (caso seja, procede-se como no caso anterior).
# Agora, calcula-se a razão de passes para touchdows pelo número de passes tentados.
# Divide-se o valor por 0,05. Mais uma vez, este valor não deve ser maior que 2,375 ou
# menor que 0 (caso seja, procede-se como de costume).
# Então, calcula-se a razão entre passes interceptados e o número de passes tentados. Deste
# valor, subtrai-se 0,095 e divide-se o resultado por 0,04. Como de praxe, este valor não
# deve ser maior que 2,375 ou menor que 0 (caso seja, atua-se como explicado).
# O quarterback rating é calculando somando-se as quatro parcelas anteriores,
# multiplicando a soma por 100 e dividindo-se o produto por 6.
# Escreva um programa, que leia o número de passes tentados, o número de passes
# completos, o número de jardas passadas, o número de passes para touchdown e o número
# de passes interceptados e informe o QB Rating do quarterback.

print('-------- Quarterback Rating --------\n')

passesCompletados = float(input('Digite a quantidade de Passes Completados: '))
passesTentados = float(input('Digite a quantidade de Passes Tentados: '))

#Pontuação de Passes Completados em Relação a Passes tentados
pontuacaoA = 0

percentualPassesCT = (passesCompletados / passesTentados)
pontuacaoA = (percentualPassesCT - 0.3) / 0.2

if pontuacaoA > 2.375:
    pontuacaoA = 2.375

elif pontuacaoA <= 0:
    pontuacaoA = 0  

#Pontuação de Jardas Passadas em razao pela quantidade de Passes Tentados
pontuacaoB = 0

jardas = float(input('Digite a quantidade de Jardas Passadas: '))
razaoJardasP = jardas / passesTentados
pontuacaoB = (razaoJardasP - 0.3) / 4

if pontuacaoB > 2.375:
    pontuacaoB = 2.375

elif pontuacaoB <= 0:
    pontuacaoB = 0 

#Pontuação de Tasses para Touchdown em realação ao numero de Passes Tentados
pontuacaoC = 0 

passesTouchdown = float(input('Digite a quantidade de passes para Tounchdown: '))
razaoPasseTounchdown = passesTouchdown / passesTentados
pontuacaoC = razaoPasseTounchdown / 0.5

if pontuacaoC > 2.375:
    pontuacaoC = 2.375

elif pontuacaoC <= 0:
    pontuacaoC = 0 

#Pontuação Passes interceptados pelo numero de passes tentados
pontuacaoD = 0

passesInterceptados = float(input('Digite a quantidade de passes Interceptados: '))
razaoPassesInterceptados = passesInterceptados / passesTentados
pontuacaoD = (razaoPassesInterceptados - 0.095) / 0.04

if pontuacaoD > 2.375:
    pontuacaoD = 2.375

elif pontuacaoD <= 0:
    pontuacaoD = 0 

#Calculando o Quarterback Ratinge
quarterbackRating = pontuacaoA + pontuacaoB + pontuacaoC + pontuacaoD
quarterbackRating = quarterbackRating * 100
quarterbackRating = quarterbackRating / 6

print('\nO índice é de ' , '%.3f' % quarterbackRating)


