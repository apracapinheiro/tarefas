# abre varios resultados de pesquisa no google

import requests
import sys
import webbrowser
import bs4


print('Googling...')  # exibe um texto enquanto faz download da pagina do google
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# obtem os links dos principais resultadas da pesquisa
soup = bs4.BeautifulSoup(res.text)

# abre uma aba do navegador para cada resultado
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))