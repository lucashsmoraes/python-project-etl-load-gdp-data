# Laboratório prático: Extrair, transformar e carregar dados do PIB

## Introdução

Neste projeto prático, você colocará em prática as habilidades adquiridas no curso e criará um pipeline ETL completo para acessar dados de um site e 
processá-los para atender aos requisitos.

## Cenário do Projeto:

Uma empresa internacional que está buscando expandir seus negócios em diferentes países ao redor do mundo recrutou você. 

Você foi contratado como Engenheiro de Dados júnior e tem a tarefa de criar um script automatizado que pode extrair a lista de todos os países 
em ordem de seus PIBs em bilhões de USDs (arredondado para 2 casas decimais), conforme registrado pelo Fundo Monetário Internacional (FMI). 

Como o FMI divulga essa avaliação duas vezes por ano, esse código será usado pela organização para extrair as informações conforme elas forem atualizadas.

________________________________________________________________________________________________________________________
Os dados necessários parecem estar disponíveis na URL mencionada abaixo:

``
https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29
``
________________________________________________________________________________________________________________________
As informações necessárias precisam ser disponibilizadas como um `CSV` arquivo `Countries_by_GDP.csv` e também como uma tabela `Countries_by_GDP` 
em um arquivo de banco de dados `World_Economies.db`com atributos Countrye `GDP_USD_billion`.

Seu chefe quer que você demonstre o sucesso deste código executando uma consulta na tabela do banco de dados para exibir apenas as entradas 
com uma economia de mais de 100 bilhões de USD. Além disso, você deve registrar um arquivo com todo o processo de execução chamado `etl_project_log.txt`.

Você deve criar um código Python `etl_project_gdp.py` que execute todas as tarefas necessárias.

## Objetivos
Você precisa concluir as seguintes tarefas para este projeto

1. Escreva uma função de extração de dados para recuperar as informações relevantes da URL necessária.
2. Transforme as informações disponíveis do PIB em `Bilhões de USD` de `Milhões de USD`.
3. Carregue as informações transformadas no arquivo `CSV` necessário e como um arquivo de banco de dados. 
4. Execute a consulta necessária no banco de dados.
5. Registre o progresso do código com registros de data e hora apropriados.

## Configuração inicial
Antes de começar a construir o código, você precisa instalar as bibliotecas necessárias para ele.

As bibliotecas necessárias para o código são as seguintes:

1. `requests`- A biblioteca usada para acessar as informações da URL.

2. `bs4`- A biblioteca que contém a BeautifulSoupfunção usada para webscraping.

3. `pandas`- A biblioteca usada para processar os dados extraídos, armazená-los nos formatos necessários e se comunicar com os bancos de dados.

4. `sqlite3`- A biblioteca necessária para criar uma conexão com o servidor de banco de dados.

5. `numpy`- A biblioteca necessária para a operação de arredondamento matemático conforme exigido nos objetivos.

6. `datetime`- A biblioteca que contém a função datetimeusada para extrair o registro de data e hora para fins de registro.

