import requests
from bs4 import BeautifulSoup

url = 'https://www.exemplo.com/tabela'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar a tabela
tabela = soup.find('table')

# Iterar sobre as linhas da tabela
for linha in tabela.find_all('tr'):
    colunas = linha.find_all('td')
    dados = [coluna.text.strip() for coluna in colunas]
    print(dados)
