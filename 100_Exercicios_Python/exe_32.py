#32. Escreva um programa que leia um caracter e diga se ele é uma vogal, consoante,
#número ou um símbolo (qualquer outro caracter, que não uma letra ou número).


print('--'*10, 'Identificando caracteres', '--'*10)


caracter = input('\n Digite o caracter desejado: ').upper()

if (caracter == 'A' or caracter == 'E' or caracter == 'I' or caracter == 'O' or caracter == 'U'):
    print(f'\n O caracter {caracter} é uma Vogal: ')

elif caracter == 'Q' or caracter == 'W' or caracter == 'R' or caracter == 'T' or caracter == 'Y' or caracter == 'P' or caracter == 'S' or caracter == 'D' or caracter == 'F'  or caracter == 'G'  or caracter == 'H'  or caracter == 'J'  or caracter == 'K'  or caracter == 'L'  or caracter == 'Ç'  or caracter == 'Z'  or caracter == 'X'  or caracter == 'C'  or caracter == 'V'  or caracter == 'B'  or caracter == 'N'  or caracter == 'M':
    print(f'\n O caracter "{caracter}" é um Consoante')    

#Identifiacndo numero e simbolos 

elif (caracter == '"' or caracter == '""' or caracter == '!' or caracter =='@' or caracter == '#' or caracter == '$' or caracter == '%' or caracter =='¨' or caracter =='&' or caracter == '*' or caracter =='(' or caracter ==')' or caracter == '_' or caracter == '-' or caracter == '=' or caracter == '+' or caracter == '`' or caracter == '[' or caracter == ']' or caracter == '{' or caracter == '}' or caracter == 'ª' or caracter == 'º' or caracter == '~' or caracter == '^' or caracter == '°' or caracter == '/' or caracter == '|' or caracter == '?' or caracter == ';' or caracter == ':' or caracter == '>' or caracter == '.' or caracter == ',' or caracter == '<' or caracter == '§'): 
    print(f'O caracter "{caracter}" é um Símbolo')     

else:
    print(f'O caracter "{caracter}" é um Número')    

    
    