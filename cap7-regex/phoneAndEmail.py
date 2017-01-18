# encontra numeros de telefone e enderecos de email no clipboard

import pyperclip
import re


phoneRegex = re.compile(r'''(
            (\d{3}|\(\d{3}\))?   # codigo de area grupo 1
            (s|-|\.)?            # separador
            (\d{3})              # primeiros 3 digitos grupo 3
            (\s|-|\.)            # separador
            (\d{4})              # ultimos 4 digitos grupo 5
            (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extensao grupo 8
            )''', re.VERBOSE)

# Cria a regex para email
emailRegex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+    # nome do usuario
            @                    # simbolo @
            [a-zA-Z0-9.-]+       # nome do dominio
            (\.[a-zA-Z]{2,4})    # ponto seguido de outros caracteres
            )''', re.VERBOSE)

# Encontra correspondecias no texto do clipboard
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
        matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])


# Copia os resultados para o clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join((matches)))
else:
    print('No phone numbers or emails found')