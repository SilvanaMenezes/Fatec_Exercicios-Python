# 7. Solicitar a idade de uma pessoa em dias e informar na tela a idade em anos, meses e dias;

anos = int(input('Qual sua idade? '))
print (f'A idade informada é {anos}.')

idade_dias = anos *365
print (f'Sua idade em dias é {idade_dias}.')

idade_meses = anos *12
print (f'Sua idade em meses é {idade_meses}.')
