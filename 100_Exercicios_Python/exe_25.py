#25. Escreva um programa que leia o número equivalente ao mês e imprima a quantidade de dias deste mês

print('-------- Quantidade de Dias do Mês --------\n')

mes = input('Digite o número do mês: ')

if mes == '1':
    print('O Mês escolhido foi Janeiro e, em 2022 ele teve 31 dias')
elif mes == '2':
    print('O Mês escolhido foi Fevereiro e, em 2022 ele teve 28 dias')
elif mes == '3':
    print('O Mês escolhido foi Março e, em 2022 ele teve 31 dias')
elif mes == '4':
    print('O Mês escolhido foi Abril e, em 2022 ele teve 30 dias')
elif mes == '5':
    print('O Mês escolhido foi Maio e, em 2022 ele teve 31 dias')
elif mes == '6':
    print('O Mês escolhido foi Junho e, em 2022 ele teve 30 dias')
elif mes == '7':
    print('O Mês escolhido foi Julho e, em 2022 ele teve 31 dias')
elif mes == '8':
    print('O Mês escolhido foi Agosto e, em 2022 ele teve 31 dias')
elif mes == '9':
    print('O Mês escolhido foi Setembro e, em 2022 ele teve 30 dias')
elif mes == '10':
    print('O Mês escolhido foi Outubro e, em 2022 ele teve 31 dias')
elif mes == '11':
    print('O Mês escolhido foi Novembro e, em 2022 ele teve 30 dias')
elif mes == '12':
    print('O Mês escolhido foi Dezembro e, em 2022 ele teve 31 dias')
else:
    print('Opção de mês invalida')