# 52. A série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos são
# fornecidos pelo usuário; a partir daí, os termos são gerados com a soma ou subtração dos
# dois termos anteriores, ou seja:
#    
#     1. Ai = Ai-1 + Ai-2, para i ímpar
#     2. Ai = Ai-1 - Ai-2, para i par
#
#  Criar um algoritmo em PORTUGOL que imprima os N primeiros termos da série de
# FETUCCINE, sabendo-se que para existir esta série serão necessários pelo menos três
# termos

print('-------- Série de Fetuccine --------\n')

limite = int(input('Digite ate que indice deseja a série de Fetuccine: '))
numeroAnterior = int(input('\nDigite o 1º número: '))
numeroAtual = int(input('Digite o 2º número: '))

indice = 1
for indice in range(limite + 1):
     if indice % 2 == 0:
         numeroProximo = numeroAtual - numeroAnterior
         print(numeroAtual, end=', ')
         numeroAnterior = numeroAtual
         numeroAtual = numeroProximo
         

     else:
        numeroProximo = numeroAtual + numeroAnterior
        numeroAnterior = numeroAtual
        numeroAtual = numeroProximo
        print(numeroAtual, end=', ')
    
        
