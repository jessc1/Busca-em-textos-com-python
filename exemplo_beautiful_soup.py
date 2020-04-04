from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
pagina = http.request("GET", "http://www.iaexpert.com.br")
pagina = http.request('GET', 'https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o')
pagina.status

sopa = BeautifulSoup(pagina.data, "lxml")
sopa
sopa.title
sopa.title.string
links = sopa.find_all('a')
len(links)
for link in links:
    print(link.get('href'))
    print(link.contents)

