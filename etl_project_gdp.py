from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

'''
 Função responsável por extrair informações necessárias do site e savar
 em um dataframe. A função deverá retornar o dataframe para o processamento
 posterior
'''


def extract(url, table_attribs):
    page = req.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')
    rows = tables[2].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            if col[0].find('a') is not None and '—' not in col[1]:
                data_dict = {"Country": col[0].a.contents[0],
                             "GDP_USD_millions": col[1].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)
    return df


'''
 Função responsável por converter as informações do PIB do formato Moeda
 para valor flutuante, transformar as informações do PIB de USD (Milhões)
 para USD (Bilhões) arredondando para 2 casas decimais. A função retorna
 o dataframe transformado.
'''


def transform(df):
    gdp_list = df["GDP_USD_millions"].tolist()                          # transformando a coluna em uma lista
    gdp_list = [float("".join(x.split(','))) for x in gdp_list]         # convertendo o texto da moeda em texto númerico
    gdp_list = [np.round(x / 1000, 2) for x in gdp_list]        # dividindo por 1000 e arredondando
    df["GDP_USD_millions"] = gdp_list                                   # reecriando o dataframe
    df = df.rename(columns={"GDP_USD_millions": "GDP_USD_billions"})    # renomeando a coluna
    return df


'''
Função responsável por salvar o dataframe final como um arquivo `CSV`
no caminho fornecido. A função não retorna nada.
'''
def load_to_csv(df, csv_path):
    df.to_csv(csv_path)


'''
Função responsável por salvar o dataframe final na tabela do banco de dados
com o nome fornecido. A função não retorna nada
'''
# def load_to_db(df, sql_connection, table_name):

'''
Função responsável por fazer consulta na tabela do banco de dados e
imprime a saída no terminal. A função não retorna nada
'''
# def run_query(query_statement, sql_connection):

'''
Função responsável por registrar a mensagem logada em um determinado
estágio da execução do código em um arquivo de log. A função não retorna nada
'''
# def log_progress(message):
