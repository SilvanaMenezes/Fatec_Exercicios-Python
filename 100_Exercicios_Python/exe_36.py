# 36. Em uma certificação são feitos 5 exames (I, II, III, IV e V). 
# Escreva um programa que leia as notas destes exames e imprima a classificação do aluno, sabendo que a média é 70. 
# Classificação:
#  A – passou em todos os exames;
#  B – passou em I, II e IV, mas não em III ou V;
#  C – passou em I e II, III ou IV, mas não em V.
#  Reprovado – outras situações	

notaI = int(input('Digite a nota do exame I: '))
notaII = int(input('Digite a nota do exame II: '))
notaIII = int(input('Digite a nota do exame III: '))
notaIV = int(input('Digite a nota do exame IV: '))
notaV = int(input('Digite a nota do exame V: '))

media = (notaI + notaII + notaIII + notaIV + notaV) / 5

if media > 70:
  print(media,'Classificação: A – passou em todos os exames;')
elif media == 70:
  print(media,'Classificação: B – passou em I, II e IV, mas não em III ou V;')
elif media > 30 and media < 70:
  print(media,'Classificação: C – passou em I e II, III ou IV, mas não em V.')
elif media < 30 or media == 0: 
  print(media,'Classificação: Reprovado – outras situações')