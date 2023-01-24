#01 - Dado o tamanho da base e da altura de um retângulo, calcular a sua área e o seu perímetro

print('-------- Área e Perímetro de um Retângulo --------\n')
#Área
altura_ret = (int(input('Digite a altura do Retângulo: ')))
base_ret = (int(input('Digite a base do Retângulo: ')))
area_ret = base_ret * altura_ret
print('\nA Área do Retângulo é igual a ' , area_ret)

#Perímetro
perimetro_ret = altura_ret * 2 + base_ret * 2
print('O Perímetro desse Retângulo é igual a: ', perimetro_ret)