import requests
import bs4
import time

# headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'}  # MAC
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'} # CHROME
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}  # FIREFOX


def request_site(url, headers, num_pagina):
    if not num_pagina:
        num_pagina = 1

    res = requests.get(url, headers=headers)
    status_request = res.raise_for_status()
    return res, status_request


def scraping_insumos(requisicao, status, num_pagina, lista_insumos):

    while status == None:
        pagina = bs4.BeautifulSoup(requisicao.text)
        insumo = pagina.select('div[class="product-name"]')
        precos = pagina.select('b[class="sale"]')
        proximo = pagina.select('span[class="page-next"]')

        if len(precos) > 0:
            for i in range(len(precos)):
                nome_insumo = insumo[i].get_text()
                preco_insumo = precos[i].get_text()
                # if not esgotado[i].get_text() == 'Esgotado':
                insumos_preco = {nome_insumo: preco_insumo}
                lista_insumos.append(insumos_preco)

            if len(proximo) > 0:
                num_pagina += 1
                url = 'http://loja.weconsultoria.com.br/fermentos-s10036/?' + 'pagina=%d' % num_pagina
                requisicao, status = request_site(url, headers, num_pagina)
                # res = requests.get(url, headers=headers)
                # status_request = res.raise_for_status()
            else:
                break
        time.sleep(3)

    return lista_insumos

num_pagina = 1
# url = 'http://loja.weconsultoria.com.br/maltes-s10038/?' + 'pagina=%d' % num_pagina  # maltes
# url = 'http://loja.weconsultoria.com.br/lupulos-s10037/?' + 'pagina=%d' % num_pagina   # lupulos
url = 'http://loja.weconsultoria.com.br/fermentos-s10036/?' + 'pagina=%d' % num_pagina   # leveduras

lista_insumos = []

requisicao, status = request_site(url, headers, num_pagina)
lista_precos_insumos = scraping_insumos(requisicao, status, num_pagina, lista_insumos)

for i in range(len(lista_precos_insumos)):
    print(lista_precos_insumos[i])
