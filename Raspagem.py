# Passo 0: Importar Bibliotecas
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import os

# Passo 1: Extrair url do produto que vamos extrair
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'
    }

nome_produto = input('digite o nome do produto: ') # Vamos buscar por 'pulseira'
nome_produto.replace(' ','-')
url_base = f'https://lista.mercadolivre.com.br/{nome_produto}'

# Passo 2: Extração das 5 primeiras páginas
num_pag = 1
titulos = []

while num_pag <= 5:

    print(f'Extração da página {num_pag}')

    indice = 1 + (num_pag - 1) * 48
    url_final = url_base + str(indice) + ' NoIndex_True'
    r = requests.get(url_final,headers=headers)

    if r.status_code == 200:
        print('Requisição Ocorreu com sucesso')
    else:
        print('Ocorreu algum erro')
    site = BeautifulSoup(r.content,'html.parser')
    imagens = site.find_all('img', class_='poly-component__picture')
    # Extrair os títulos
    for img in imagens:
        titulo = img.get('title', '').strip()
        if titulo and titulo != "Colae":  # Filtrar títulos vazios ou genéricos
            titulos.append(titulo)
    
    num_pag += 1
    

# Passo 3: Guardar os titulos em uma tabela e exportar para um csv
Tabela = pd.DataFrame({'Produtos':titulos})

for i, titulo in enumerate(titulos, 1):
    print(f"{i}. {titulo}")

# Exibe o diretório atual (onde o arquivo será salvo)
print("Diretório atual:", os.getcwd())

# Define o nome do arquivo CSV
nome_arquivo = 'Pulseiras_5paginas.csv' # Analogo para colar e pulseira 

# Salva o DataFrame como CSV no diretório do projeto
Tabela.to_csv(nome_arquivo, index=False)

print(f"Arquivo '{nome_arquivo}' criado com sucesso em:\n{os.path.join(os.getcwd(), nome_arquivo)}")