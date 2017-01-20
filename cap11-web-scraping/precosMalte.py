import requests
import bs4


# headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'}  # MAC
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'} # CHROME
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}  # FIREFOX

num_pagina = 1
url = 'http://loja.weconsultoria.com.br/maltes-s10038/?' + 'pagina=%d' % num_pagina
res = requests.get(url, headers=headers)
status_request = res.raise_for_status()

lista_maltes = []
maltes_preco = {}

while status_request == None:
    pagina = bs4.BeautifulSoup(res.text)
    maltes = pagina.select('div[class="product-name"]')
    precos = pagina.select('b[class="sale"]')
    esgotado = pagina.select('div[class="price"]')
    proximo = pagina.select('span[class="page-next"]')

    if len(precos) > 0:
        for i in range(len(precos)):
            nome_malte = maltes[i].get_text()
            preco_malte = precos[i].get_text()
            # if not esgotado[i].get_text() == 'Esgotado':
            maltes_preco = {nome_malte: preco_malte}
            lista_maltes.append(maltes_preco)

        if len(proximo) > 0:
            num_pagina += 1
            url = 'http://loja.weconsultoria.com.br/maltes-s10038/?' + 'pagina=%d' % num_pagina
            res = requests.get(url, headers=headers)
            status_request = res.raise_for_status()
        else:
            break

for i in range(len(lista_maltes)):
    print(lista_maltes[i])
