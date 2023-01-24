#3. Dado o tamanho do raio de uma circunferência, calcular a área e o perímetro da mesma

print('-------- Área e Perímetro de uma Circunferência --------')

raio_cir = (float(input('\nDigite o valor do Raio: ')))
pi = 3.14
area_cir = pi * (raio_cir ** 2)
perimetro_cir = 2 * pi * raio_cir

arrendondar = input('\nVocê deseja arrendondar os resultados? S/N \n')

if arrendondar.upper() == 'S':
    print('\nA Área da Circunferência é igual a: ' , int(area_cir))
    print('O Perímetro da Circunferência é igual a: ' , int(perimetro_cir))
else:
    print('\nA Área da Circunferência é igual a: ' , float(area_cir))
    print('A Área da Circunferência é igual a: ' , float(perimetro_cir))

print('\nOBS.: O cálculo foi realizado com o valor de π = 3,14 ')