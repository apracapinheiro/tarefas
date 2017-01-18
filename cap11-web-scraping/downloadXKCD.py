# Faz download de todas as tirinhas do site XKCD

import requests
import os
import bs4

url = 'http://xkcd.com'  # url inicial
os.makedirs('xkcd', exist_ok=True)  # armazena as tirinhas em ./xkcd

while not url.endswith('#'):
    # faz download da pagina
    print('Download da pagina %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # encontra a URL da imagem da tirinha
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Nao fo iencontrada imagem de tirinha.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # faz o download da imagem
        print('Download da imagem %s...' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()

        # salva a imagem em ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # obtem a URL do botao prev
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Terminado')
