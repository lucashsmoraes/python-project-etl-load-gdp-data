from etl_project_gdp import extract, transform, load_to_csv, load_to_db
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
    df = extract(url, table_attribs)
    df = transform(df)
    load_to_csv(df, csv_path)
    sql_connection = sqlite3.connect('World_Economies.db')
    load_to_db(df, sql_connection, table_name)

