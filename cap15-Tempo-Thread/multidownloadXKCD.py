# Faz o download das tirinhas XKCD usando varias threads

import requests
import os
import bs4
import threading


os.makedirs('xkcd', exist_ok=True)  # armazena as tirinhas em ./xkcd


def downloadXkcd(startComic, endComic):
    for urlNumber in (startComic, endComic):
        # faz download da pagina
        print('Download da pagina http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # encontra a URL da imagem da tirinha
        comicElem = soup.select('#comic img')

        if comicElem == []:
            print('Nao foi encontrada imagem de tirinha.')
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

# Cria e inicia os objetos Thread
downloadThreads = []            # uma lista com todos os objetos thread
for i in range(0, 1400, 100):   # executa o loop 14 vezes e cria 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Espera todas as threads terminarem
for downloadThread in downloadThreads:
    downloadThread.join()

print('Terminado')