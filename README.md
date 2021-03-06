# Data Engineer

- Data Engineer technical test

## Especificações

- Todas as operações devem ser realizadas utilizando Spark
- A entrega deve ser desenvolvida em Python

## Requisitos

1. Conversão do formato dos arquivos:
   Converter o arquivo CSV presente no diretório data/input/users/load.csv, para um formato colunar de alta performance de leitura de sua escolha.
   Justificar brevemente a escolha do formato

2. Deduplicação dos dados convertidos:
   No conjunto de dados convertidos haverão múltiplas entradas para um mesmo registro, variando apenas os valores de alguns dos campos entre elas.
   Será necessário realizar um processo de deduplicação destes dados, a fim de apenas manter a última entrada de cada registro, usando como referência o id para identificação dos registros duplicados e a data de atualização (update_date) para definição do registro mais recente

3. Conversão do tipo dos dados deduplicados:
   No diretório config haverá um arquivo JSON de configuração (types_mapping.json), contendo os nomes dos campos e os respectivos tipos desejados de output. Utilizando esse arquivo como input, realizar um processo de conversão dos tipos dos campos descritos, no conjunto de dados deduplicados;

### Notas gerais

<details>

- Todas as operações devem ser realizadas utilizando Spark

  - O serviço de execução fica a seu critério, podendo utilizar tanto serviços locais como serviços em cloud
  - Justificar brevemente o serviço escolhido (EMR, Glue, Zeppelin, etc.).

- Cada operação deve ser realizada no dataframe resultante do passo anterior

  - Pode ser persistido e carregado em diferentes conjuntos de arquivos após cada etapa
  - Ou executados em memória e apenas persistido após operação final

- Você tem liberdade p/ seguir a sequência de execução desejada

- Solicitamos a transformação de tipos de dados apenas de alguns campos.
  Os outros ficam a seu critério

- O arquivo ou o conjunto de arquivos finais devem ser compactados e enviados por e-mail

</details>

## Execução do projeto

### Escolha do formato colunar a se usar Parquet or ORC - Escolhido Parquet

Ambos os formatos (ORC, Parquet) são altamente utilizados e conhecidos.

- Para as soluções de DW
  - BigQuery (GCP -> [ORC](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-orc), [Parquet](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet))
  - Redshift (AWS -> [ORC](https://docs.aws.amazon.com/pt_br/redshift/latest/dg/copy-parameters-data-format.html#copy-orc), [Parquet](https://docs.aws.amazon.com/pt_br/redshift/latest/dg/copy-parameters-data-format.html#copy-parquet))

As soluções [Glue](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) para ETL e Apache Flink como mecanismo de streaming de dados [ORC](https://ci.apache.org/projects/flink/flink-docs-release-1.11/dev/table/connectors/formats/orc.html) e [Parquet](https://ci.apache.org/projects/flink/flink-docs-release-1.11/dev/table/connectors/formats/parquet.html), suportam ambos os formatos de arquivo.

Já as soluções [Apache Hive](https://hive.apache.org/) (preferido para [Batch processing](https://www.simplilearn.com/basics-of-hive-and-impala-tutorial)) e [Apache Impala](https://impala.apache.org/) (preferido para [ad hoc queries](https://www.simplilearn.com/basics-of-hive-and-impala-tutorial)) suportam ambos os formatos, porém o [formato recomendado](https://docs.cloudera.com/runtime/7.1.2/using-hiveql/topics/hive-orc-parquet-compare.html) é Orc para o Hive e o Parquet para o Impala.

No nosso caso de referencia que é somente o processamento do arquivo CSV para Colunar utilizando Spark, o mesmo também suporta ambas as opções [ORC](https://spark.apache.org/docs/latest/sql-data-sources-orc.html), [Parquet](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html)

Ambos os formatos seriam boas escolhas visando suporte das plataformas e soluções. Ambos também tem uma boa performance considerando o ["Benchmarking PARQUET vs ORC"](https://medium.com/@dhareshwarganesh/benchmarking-parquet-vs-orc-d52c39849aef) realizado por Dhareshwarganesh.
Porém o formato Parquet tem um melhor suporte ao Spark diretamente conforme apresentado pelo Xinran Waibel no [towardsdatascience](https://towardsdatascience.com/demystify-hadoop-data-formats-avro-orc-and-parquet-e428709cf3bb).

Para uma escolha mais assertiva de um formato do arquivo é necessário tem uma visão mais ampla de como será

### Solução

#### Teste local

Foi criado o diretório [local_execution](local_execution/) com intuito de iniciar no projeto e validar algumas operações antes de rodar na Cloud.

Dentro deste diretório existe um [README.md](local_execution/README.md) explicando com executar o mesmo.

A solução local não está completamente implementada, mas achei valido permanecer com este componente no projeto para consultas de futura melhoria.

#### Escolha da plataform a ser utilizada - AWS Glue

A plataforma que foi escolhida pela sua simplicidade de operação, visto que o problema apresentado é simples.

Também considerei o custo para execução na cloud, para este projeto foi gasto $0,26 para o Glue e para o S3 eu permaneci dentro do free tier.

#### O projeto [aws-glue-csv-parquet](https://github.com/afonsoaugusto/aws-glue-csv-parquet/tree/main)

O projeto [aws-glue-csv-parquet](https://github.com/afonsoaugusto/aws-glue-csv-parquet/tree/main) é a minha solução para este problema. Foi escolhido ser feito em um repositório separado para simplificar o pipeline.

*A estrutura, definição e a descrição da solução deste projeto é feita no submodulo do mesmo.*

##### Adicionando submodulo

`git submodule add git@github.com:afonsoaugusto/aws-glue-csv-parquet.git`

##### Atualizando submodulo

`git submodule update --init --recursive`
