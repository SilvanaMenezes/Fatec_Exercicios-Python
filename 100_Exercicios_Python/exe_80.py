#80. Escreva um programa em C que leia duas string e informe se a primeira contém a
#segunda.

print('-------- Comparação entre 2 Strings --------\n')

while True:

    string1 = input('\nDigite a primeira String: ')
    string2 = input('Digite a segunda String apenas: ')

    if string1.lower() == string2.lower():
        print(f'\nA segunda String({string2}), contém na primeira String({string1}).')
    elif string1.lower() != string2.lower():
        print(f'\nA segunda String({string2}), não contém na primeira({string1}).')
    
    continuar = input('\nA comparação foi feita deseja continuar? S/N\n')
    if continuar.lower() == 'n':
        break