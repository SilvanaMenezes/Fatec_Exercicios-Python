#53. Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano, escreva um programa, que imprima o tempo necessário para que a população do país A ultrapasse a população do país B. 
paisA = 5000000
paisB = 7000000
quantidade_anos = 0

while paisB > paisA:
     populacao_PaisA = paisA * 0.03
     populacao_paisB = paisB * 0.02
     paisA = paisA + populacao_PaisA
     paisB = paisB + populacao_paisB 
     quantidade_anos = quantidade_anos + 1
     
print(f'O pais A passará o pais B em {quantidade_anos} Anos')
