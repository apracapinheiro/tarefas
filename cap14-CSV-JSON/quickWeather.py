# Exibe a previsao do tempo para uma localidade obtida na linha de comando

import json
import requests
import sys


# Processa a localidade a partir dos argumentos da linha de comando
# if len(sys.argv) < 2:
#     print('Uso do programa: quickWheater.py localizacao')
#     sys.exit()
#
# location = ' '.join(sys.argv[1:])

# Faz download dos dados JSON a partir da API de OpenWheaterMap.org
url = 'http://api.openweathermap.org/data/2.5/weather?q=San Francisco, CA&start=1485349200&end=1485633600&APPID=86a9750a855f4880e7750644455cb167'
# url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&cnt=3&APPID=86a9750a855f4880e7750644455cb167' % location
print(url)
response = requests.get(url)
response.raise_for_status()

# Carrega dados JSON em uma variavel Python
weatherData = json.loads(response.text)

# Exibe as descricoes da previsao do tempo
w = weatherData['main']
# print('Tempo nesse momento em %s: ' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Amanha: ')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('Depois de amanha: ')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])