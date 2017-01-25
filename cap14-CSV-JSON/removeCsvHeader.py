# Remove o cabeçalho de todos os arquivos CSV no diretorio de trabalho atual


import csv
import os


os.makedirs('headerRemoved', exist_ok=True)


# Percorre todos os arquivos no diretorio de trabalho atual em um loop
for csvFileName in os.listdir('.'):
    if not csvFileName.endswith('.csv'):
        continue  # ignora arquivos que não sejam CSV

    print('Removendo o cabecalho de ' + csvFileName + '...')

    # le o arquivo CSV (pula a primeira linha)
    csvRows = []
    csvFileObj = open(csvFileName)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue  # pula a primeira linha

        csvRows.append(row)

    csvFileObj.close()

    # grava o arquivo CSV
    csvFileObj = open(os.path.join('headerRemoved', csvFileName), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)

    for row in csvRows:
        csvWriter.writerow(row)

    csvFileObj.close()