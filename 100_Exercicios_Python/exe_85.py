#85. Escreva um programa que leia uma string representando um número hexadecimal (base 16)
#  e imprima sua representação em decimal (base 10).
# Decimal 79 = 4F (hex) 
# Decimal 10 = A (hex) 
# Decimal 90 = 5A (hex) 

hexa = input('digite um numero em hexadecimal: ').upper()
res = int(hexa, 16) 
print(f"O valor Hexadecimal: {str(hexa)} em Decimal é: " + str(res))