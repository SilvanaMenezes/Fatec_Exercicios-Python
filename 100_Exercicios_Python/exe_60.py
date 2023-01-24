#60 A famosa conjectura de Gold Bach diz que todo inteiro par maior que 2 é soma de dois números primos.
# Testes foram feitos, mas ainda não se achou um contra-exemplo. Escreva um programa mostrando que a afirmação é verdadeira para todo número par entre 500 e 1000. O programa deve imprimir o número par e os dois primos que somados dão o número par.

primos1 = []
primos2 = []

print('\n','='*10, 'todos os números primos de 01 à 500', '='*10, '\n')
for x in range(1, 500):
    cont = 0
    for y in range(1,x+1):
       if x % y == 0:
        cont += 1
    if cont <= 2:
        primos1.append(x)
print(primos1, end=',''\n')

print('\n','='*10, 'todos os números primos de 500 à 1000', '='*10, '\n')           
for x in range(500,1000):
    cont = 0
    for y in range(1,x+1):
       if x % y == 0:
        cont += 1
    if cont <= 2:
        primos2.append(x)
print(primos2, end=',''\n')

print('\n','='*10, 'somando as posições', '='*10, '\n')
i = 0
res = 0

primos1[i] = int(input('Digite um número primo da lista de 01 à 500: '))
primos2[i] = int(input('Digite um número primo da lista de 500 à 1000: '))

res = primos1[i] + primos2[i]
print(f'A soma entre os números primos informados {primos1[i]} e {primos2[i]} é o número par {res}.')

#tentei isso aqui, mas ainda tem brechas
'''if primos1[i] == 2:
    primos1[i] = int(input('Você digitou 2, tente outro número: '))
    if primos1[i] != 2:       
        primos2[i] = int(input('Digite um número primo de 500 à 1000: '))
    res = primos1[i] + primos2[i]

    print(f' A soma entre os números primos informados {primos1[i]} e {primos2[i]} é o número par {res}.')
print()'''
















    
        
        
          
    
    
    
        


