#2. Dado o tamanho do lado de um quadrado, calcular a área e o perímetro do mesmo

print('-------- Área e Perímetro de um Quadrado --------\n')
#Área
lado_quad = (int(input('Digite o valor de um dos lados do Quadrado: ')))
area_quad = lado_quad * lado_quad
print( '\nA Área do Quadrado é igual a: ' , area_quad )

#Perimetro
perimetro_quad = lado_quad + lado_quad + lado_quad + lado_quad
print ( 'O Perímetro do Quadrado é igual a: ' , perimetro_quad )