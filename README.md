# 📊 Análise de SEO e Tendências - Mercado Livre

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)

## 📝 Sobre o Projeto

Este projeto consiste em uma pipeline completa de **Engenharia e Análise de Dados** focada em e-commerce. O objetivo principal foi realizar a engenharia reversa dos anúncios mais vendidos ("Pulseiras") no Mercado Livre para identificar padrões de SEO (Search Engine Optimization) que alavancam as vendas.

O projeto é dividido em duas etapas:
1.  **Coleta (Web Scraping):** Automação para extrair títulos de produtos das 5 primeiras páginas de busca.
2.  **Inteligência (NLP & Analytics):** Processamento de linguagem natural para limpar, tokenizar e identificar as palavras-chave de maior conversão.

---

## 💡 Insights de Negócio (Resultados)

A análise dos dados revelou padrões cruciais para vendedores que desejam ranquear na primeira página:

* **Especificidade Técnica:** Anúncios contendo medidas explícitas (**"cm"**) têm prioridade no algoritmo de busca.
* **Gatilhos de Qualidade:** Para joias de prata, o termo **"925"** é mais relevante que a palavra "prata" sozinha.
* **Terminologia de Aço:** O termo **"Inox"** possui melhor performance e leitura que "Inoxidável".
* **Cores e Materiais:** Para itens dourados, a palavra **"Dourado"** é obrigatória. Para itens prateados, o material ("Aço", "Prata") já subentende a cor, tornando a palavra "prateado" redundante.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12+
* **Coleta de Dados:** `Requests`, `BeautifulSoup4`
* **Manipulação de Dados:** `Pandas`
* **Processamento de Texto (NLP):** `NLTK`, `RegEx` (Expressões Regulares)
* **Visualização:** `Matplotlib`, `Seaborn`, `WordCloud`

---
