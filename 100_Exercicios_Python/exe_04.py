#4. Dado os três lados de um triângulo determinar o perímetro do mesmo.

print('-------- Perímetro de um Triângulo --------\n')

ladosIguais_tri = input('O triângulo tem os 3 lados iguais? S/N \n')

if ladosIguais_tri.upper() == 'S':
    lado1_tri = (int(input('Digite o valor de um dos lados: ')))
    perimetro_tri = lado1_tri + lado1_tri + lado1_tri
    print ( '\nO valor do Perímetro é igual a: ' , perimetro_tri )
else:
    lado1_tri = (int(input('\nDigite o valor do primeiro lado: ')))
    lado2_tri = (int(input('Digite o valor do segundo lado: ')))
    lado3_tri = (int(input('Digite o valor do terceiro lado: ')))
    perimetro_tri = lado1_tri + lado2_tri + lado3_tri
    print ( '\nO valor do Perímetro é igual a: ' , perimetro_tri )