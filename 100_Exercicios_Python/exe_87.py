# 87. Escreva um programa em Python, que verifique se duas strings são iguais, independente da
# caixa das letras. Por exemplo, este programa deve dizer que “Teste” é igual a “TeStE”

str1 = str(input('Digite a primeira string: ')).upper()
str2 = str(input('Digite a segunda string: ')).upper()

if str1 == str2:
    print('iguais')
else:
    print('diferentes')