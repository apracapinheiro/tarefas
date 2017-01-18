# renomeia os nomes de arquivo com formato de data MM-DD-AAAA em estilo americano para o formato
# DD-MM-AAAA em estilo europeu

import shutil
import os
import re

# cria um regex que corresponda aos arquivos com formato de data em estilo americano
datePattern = re.compile(r"""^(.*?)         # todo o texto antes da data
                         ((0|1)?\d)-         # um ou dois digitos para o mes
                         ((0|1|2|3)?\d)-    # um ou dois digitos para o dia
                         ((19|20)\d\d)      # quatro digitos para o ano
                         (.*?)$             # todo o texto apos a data
                         """, re.VERBOSE)



# Percorre os arquivos do diretorio de trabalho com um loop
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # ignora os arquivos que nao tenham uma data
    if mo == None:
        continue

    # Obtem as diferentes partes do nome do arquivo
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)


    # Compoe o nome do arquivo em estilo europeu
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Obtem os paths absolutos completos dos arquivos
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Renomeia os arquivos
    print('Renomeando "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)