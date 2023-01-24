#12. Faça um algoritmo que transforme uma velocidade fornecida em m/s pelo usuário para Km/h. para tal, multiplique o valor em m/s por 3,6.
from cgi import print_directory


print('--'*5, 'Conversor d m/s para Km/s', '--'*5)
print()
m_s = float(input('Divite o valor em m/s --> '))
km_s = m_s * 3,6
print(f'Valor convertido será de {m_s}Km/s')

  
