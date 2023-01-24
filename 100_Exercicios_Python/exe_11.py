#11. Faça um algoritmo para calcular a nota semestral de um aluno. A nota semestral é obtida pela média aritmética entre a nota de 2 bimestres. Cada nota de bimestre é composta por 2 notas de provas. 

print('--'*5, 'calculo para nota semestral do aluno', '--'*5)
print()
primeira_prova = float(input('Insira a nota da primeira prova --> '))
segunda_prova = float(input('insira a nota da segunda prova --> '))
bimestre = primeira_prova + segunda_prova  
media_bimestre =  bimestre / 2
print(f'Nota Sestral será --> {media_bimestre}')