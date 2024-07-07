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
    return df

'''
 Função responsável por converter as informações do PIB do formato Moeda
 para valor flutuante, transformar as informações do PIB de USD (Milhões)
 para USD (Bilhões) arredondando para 2 casas decimais. A função retorna
 o dataframe transformado.
'''
def transform(df):
    return df


'''
Função responsável por salvar o dataframe final como um arquivo `CSV`
no caminho fornecido. A função não retorna nada.
'''
def load_to_csv(df, csv_path):


'''
Função responsável por salvar o dataframe final na tabela do banco de dados
com o nome fornecido. A função não retorna nada
'''
def load_to_db(df, sql_connection, table_name):

'''
Função responsável por fazer consulta na tabela do banco de dados e
imprime a saída no terminal. A função não retorna nada
'''
def run_query(query_statement, sql_connection):

'''
Função responsável por registrar a mensagem logada em um determinado
estágio da execução do código em um arquivo de log. A função não retorna nada
'''
def log_progress(message):
