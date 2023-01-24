#89. Escreva um programa em C, que gere uma string composta pelo último nome, seguido de
#virgula e as iniciais dos demais nomes (em ordem), seguida de ponto. Por exemplo, se a
#string entrada for “Gabriel Garcia Marquez”, a string gerada deve ser “Marquez, G. G.”.

nome = input('Digite seu Nome e Sobrenome: ').title().strip()

nomeSeparado = nome.split()
tamanho = len(nomeSeparado)
iniciais = []

for indice in range (tamanho):
    iniciais.append(nomeSeparado[indice])
    
    if nomeSeparado[indice] in ['Da','De','Do','Dos','Das']:
        iniciais.remove(nomeSeparado[indice])

#Mostrando o Ultimo Sobrenome
print(iniciais[len(iniciais)-1],', ', end='')

#Mostrando cada Inicial do nome e sobrenomes restantes em ordem
for indice in range (0,len(iniciais)-1):
    print(f'{iniciais[indice][0]}', end='. ')