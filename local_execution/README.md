# Validação do algoritimo

## Testes locais antes da automação na CLOUD.

    Antes de automatizar em alguma solução para CLOUD, eu preferi executar localmente todo o processo.
    Assim deixei automatizado

## Requerimentos

- Docker
- Docker-compose

No meu ambiente estou rodando com as seguintes versões

- Docker Version: 19.03.13
- Docker-compose
  - docker-compose version 1.26.2, build eefe0d31
  - docker-py version: 4.2.2
  - CPython version: 3.7.7
  - OpenSSL version: OpenSSL 1.1.0l 10 Sep 2019

## Portas e URL

- Porta do Cluster Spark UI: 8080
- URL do Cluster Spark para acesso dento da network criada pelo docker-compose: spark://spark:7077
- Porta do JupyterNotebook: 8888

## Rodando com docker-compose

Utilizando o comando `docker-compose up` no diretório _local_execution_ você terá acesso ao cluster spark e ao container rodando o jupyter notebook.
A url de acesso e o token estarão disponiveis no log do docker-compose.

## Rodando utilizando o devcontainer do VSCode

Utilizando a opção _devcontainer_ do VSCode o mesmo irá executar o _docker-compose_.
Porém ele não irá executar o Jupyter Notebook devido o dockerfile estar usando a diretiva _CMD_ ao inves do _ENTRYPOINT_.

Os laboratórios locais foram desenvolvidos utilizando os notebooks do jupyter.

Para executar o jupyter notebook no container basta executar o script:

```sh
bash entrypoint-jupyter.sh
```

## VOLUMES do projeto

No arquivo [docker-compose.yml](./docker-compose.yml) foram definidos três volumes de referencia no service python3.

- **/config** para o arquivo _types_mapping.json_ que define o mapeamento de conversão de dados.
- **/data** para os arqivos do desafio ficarem isolados
- **/workspace/project** para ter uma visão do projeto como todo

## Documentações que foram importantes

* [spark.apache.org/docs/api/python/pyspark.sql](https://spark.apache.org/docs/latest/api/python/pyspark.sql.html)


## TODO

Durante a execução local eu não iniciei um hdfs para ser utilizado.
Devido a este fato eu uso o pandas para carregar o csv e apartir dele eu crio o objeto no pyspark.

Para salvar o arquivo eu estava fazendo o metodo de tranformar para um dataframe pandas e dele salvar no S.O.
Porém neste metodo existe uma perda de informação na conversão dos dados para o timestamp.
Como o meu objetivo é a execução em Cloud, vou deixar este *TODO* neste projeto.
