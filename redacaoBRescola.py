import re

import requests
from bs4 import BeautifulSoup

# verificar se a página está disponível
def get_content_page(url):
    content = requests.get(url.strip())
    return False if content.status_code == 404 else content.content

def themes_and_links(url):
    soup = BeautifulSoup(get_content_page(url), 'lxml')
    # select = soup.find('select', attrs={'id': 'selectBoxBR'})
    options = soup.select('select[id=selectBoxBR]> option')
    for option in options[1:]:
        print(option['value'] + '->' + option.text)

def get_description(url):
    soup = BeautifulSoup(get_content_page(url), 'lxml')
    secao_texto = soup.find('div', attrs={'id': 'secao_texto'})
    divs = secao_texto.find_all('div')
    print(divs[11].text)

'''
def get_essays(url):
    soup = BeautifulSoup(get_content_page(url), 'lxml')
    tables = soup.find('table', attrs={'id': 'redacoes_corrigidas'})
    links = tables.find_all('a')
    for link in links:
        print(link.get('href'))
'''
def extract_content_essay(url):
    soup = BeautifulSoup(get_content_page(url), 'lxml')
    try:
        theme = soup.find_all('span', attrs={'itemprop': 'name'})[2].text
        print('TEMA: ', theme)
    except Exception as e:
        try:
            theme = soup.find('span', attrs={'class': 'definicao'})
            theme = theme.find('a').text.strip()
            print(theme)
        except Exception as e:
            print(e)
    title = soup.find('div', attrs={'class': 'br-grid-3 margem-conteudo'})
    title = title.find('h1').text.strip()
    print('TITULO: ', title)
    essay = soup.find('div', attrs={'class': 'conteudo-materia'})
    for content in essay.find_all('p')[1:]:
        print(content.text)

def get_essays(url):
    soup = BeautifulSoup(get_content_page(url), 'lxml')
    print(soup.find(id='redacoes_corrigidas').text)


URL_BASE = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes'
url_theme = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes/tema-abuso-de-autoridade-no-brasil.htm'
url_essay = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes/16257'
# themes_and_links(URL_BASE)
# get_description(url_theme)
# get_essays(url_theme)

extract_content_essay(url_essay)
get_essays(url_essay)
