# 8. Dado que a fórmula para conversão de Fahrenheit para Celsius é C = 5/9 (F – 32), leia um valor de temperatura em Fahrenheit e exibi-o em Celsius;

f = float(input('Informe a temperatura em ºF: '))
c = (f - 32) * 5 / 9
print('A temperatura de {}ºF corresponde a {:.2f}ºC.'.format(f,c))