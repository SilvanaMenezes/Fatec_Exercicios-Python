# 29. Escreva um programa que calcula o desconto previdenciário de um funcionário. Dado um salário, o programa deve retornar o valor do desconto proporcional ao mesmo. O cálculo segue a regra: o desconto é de 11% do valor do salário, entretanto, o valor máximo de desconto é 334,29, o que seja menor;

salario = float(input('Digite o valor do salario: '))

if salario * 0.11 > 334.29:
    desconto = 334.29
else:
    desconto = salario * 0.11
print("O desconto previdenciário do salário informado é:", desconto)

														