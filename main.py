from etl_project_gdp import extract, transform, load_to_csv, load_to_db, run_query, log_progress
import sqlite3

'''
1 - URL 
2 - table_attribs: Os atributos ou nomes de colunas para o dataframe armazenado como uma lista.
3 - db_name: 'World_Economies.db'
4 - table_name: 'Countries_by_GDP'
5 - csv_path: 'Countries_by_GDP.csv'
'''
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attribs = ["Country", "GDP_USD_millions"]
db_name = 'World_Economies.db'
table_name = 'Countries_by_GDP'
csv_path = './Countries_by_GDP.csv'

if __name__ == '__main__':
    log_progress('Iniciando processo ETL')
    df = extract(url, table_attribs)

    log_progress('Extração de dados concluída. Iniciando o processo de transformação')
    df = transform(df)

    log_progress('Transformação de dados concluída. Iniciando processo de carregamento')
    load_to_csv(df, csv_path)

    log_progress('Dados salvos em arquivo CSV. Iniciando conecção com banco de dados')
    sql_connection = sqlite3.connect('World_Economies.db')

    log_progress('Conecção SQL Finalizada, Iniciando carregamento dado como tabela no banco de dados')
    load_to_db(df, sql_connection, table_name)

    log_progress('Dados carregados com sucesso. Iniciando consulta na tabela')
    query_statement = f"SELECT * from {table_name} WHERE GDP_USD_billions >= 28780"
    run_query(query_statement, sql_connection)

    log_progress('Processo finalizado com sucesso')
    sql_connection.close()

