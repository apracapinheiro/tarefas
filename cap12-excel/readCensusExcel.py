# Cria uma tabela com a populacao e o numero de setores censitarios de cada condado (EUA)

import openpyxl
import pprint

print('Abrindo workbook...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')

countyData = {}

# preenche countyData com a populacao e os setores de cada condado
print('Lendo as linhas...')

for row in range(2, sheet.max_row + 1):
    # cada linha da planilha contem dados de um setor censitario
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # garante que a chave para esse estado exista
    countyData.setdefault(state, {})
    # garante que a chave para esse condado nesse estado exista
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    # cada linha representa um setor censitario, portanto incrementa o valor de um
    countyData[state][county]['pop'] += int(pop)



# abre um novo arquivo texto e grava o conteudo de countyData nesse arquivo
print('Gravando os resultados...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Terminado.')



