# 86. Escreva um número que leia um número em Romano e imprima o equivalente em
# decimal (base 10)

print('-------- Conversor de Número Romano para Decimal --------\n')

romano = input('Digite o número Romano: ')

#Removendo os espaços caso o usuario dê(strip), convertando para letras maiusculas(upper) e declarando variaveis e vetores
romano = romano.strip()
romano = romano.upper()

indice = 0
posicao = 0
numeroDecimal = 0
subtracao = 0

limite = len(romano)

vetorRomano = ['I', 'V', 'X', 'L','C','D','M']
vetorNumero = [1, 5, 10, 50, 100, 500, 1000]
numero = []

#Convertendo cada letra para número e colocando no vetor de número
for indice in range(limite):
    for posicao in range(7):
        if romano[indice] == vetorRomano[posicao]:
            numero.append(vetorNumero[posicao])

#Tamanho do meu range
numero.append(0)
limite = len(numero)


#Transformando em número
for indice in range(limite-1):
    if numero[indice] == numero[indice + 1]:
        numeroDecimal = numeroDecimal + numero[indice]
    
    if numero[indice] > numero[indice + 1]:
        numeroDecimal = numeroDecimal + numero[indice]
    
    if numero[indice] < numero[indice + 1]:
        subtracao = numero[indice + 1] - numero[indice]
        numeroDecimal = (numeroDecimal + subtracao) - numero[indice + 1]
            
print(f'\nSeu número Romano em Decimal é: {numeroDecimal}')