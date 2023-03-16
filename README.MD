# BONUS CHALLENGE - ALFA TRANSPORTES

**Crie um programa em Python, que utilize a biblioteca requests para consultar os dados das filiais da Alfa Transportes listadas acima e popular automaticamente a tabela de filiais, buscando os dados na API ReceitaWS. Link para Documentação da API: https://receitaws.com.br/api Link para Documentação da biblioteca Requests: https://docs.python-requests.org/en/latest/**


## Instalando as dependências

Após criação e ativação do ambiente virtual, instalar dependências:

```pip install -r requirements.txt```

## Banco de dados (PostgreSQL)

Para acesso ao banco de dados, alterar informações constantes no arquivo ConnectDb.py, onde:

```host='localhost', database='postgres', user='postgres', password='password123'```

Criação da tabela no banco de dados:

```CREATE TABLE FILIAIS_ALFA (codigo_id SERIAL PRIMARY KEY, cnpj TEXT NOT NULL, nome TEXT NOT NULL, cidade TEXT NOT NULL, estado TEXT NOT NULL, UNIQUE (cnpj));```

## Executando

Executar o arquivo main.py. 

Atentar-se a variável "array_cnpjs" com apenas três items, uma vez que a API possui limite de apenas 3 consultas por minuto.