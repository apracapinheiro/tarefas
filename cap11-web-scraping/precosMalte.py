import requests
import bs4


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'}

res = requests.get('http://loja.weconsultoria.com.br/maltes-s10038/', headers=headers)
res.raise_for_status()

pagina = bs4.BeautifulSoup(res.txt)

precos = pagina.select('.sale')
maltes = pagina.select('.product-name')

nome_malte = maltes[0].get_text('title', 'sale')