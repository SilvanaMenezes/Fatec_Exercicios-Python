# 99. Escrever um algoritmo e implementá-lo em linguagem C que dada uma matriz N X N, contendo, 
# em cada linha, as idades do homem e da mulher no casamento, criar uma matriz de frequência de idade de casamento, 
# com as contagens para cada combinação de idades. As idades variam de 18 até 30. Os pares de idade devem ser lidos 
# até que se informe um valor inválido para a idade de qualquer dos dois nubentes. Em seguida, o programa deverá informar: 

# (1). Qual a idade mais frequente de casamento dos homens 
# (2). Qual a idade mais frequente de casamento das mulheres 
# (3). Qual a combinação mais frequente de idades de casamento
import statistics  as sts


idadeF = []
idadeM = []
todos = list()
pessoa = dict()
soma_m = 0
soma_f = 0
modaF = 0
modaM = 0
modaGeral = 0
#leitura de dados
#cálculo de moda = mode() ###
while True:
    pessoa.clear()
    pessoa['idade'] = int(input('Idade: '))   
    if pessoa['idade'] < 18 or pessoa['idade'] > 30:
        del pessoa
        break
    while True:
        pessoa['nome'] = str(input('Nome: '))
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        
        if pessoa['sexo'] in 'MF':
                break
        print('ERRO! Digite apenas M ou F. ')
    
    todos.append(pessoa.copy())
    
    
    while True:
        resp = str(input('Continuar registrando? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responta S ou N. ')
    if resp == 'N':
        break    
print('=-='*30)
print(f'{todos}\n')
#qntd mulheres
for p in todos:
    if p['sexo'] in 'Ff':
        idadeF.append(p['idade'])
        modaF = sts.mode(idadeF)
        
        
#qntd homens      
    if p['sexo'] in 'Mm':
        idadeM.append(p['idade'])
        modaM = sts.mode(idadeM)
        
idadeGeral = idadeM + idadeF
modaGeral = sts.mode(idadeGeral)

print(f'Idade mais frequente de casamento dos homens: {modaM}') 
print(f'Idade mais frequente de casamento dos mulheres: {modaF}')    
print(f'Idade mais frequente do casamento: {modaGeral}')
print(todos)
print()
print('encerramento')
