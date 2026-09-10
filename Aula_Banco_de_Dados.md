# Banco de Dados

Um **banco de dados (Database)** é uma coleção organizada de dados armazenados de forma estruturada, permitindo que essas informações sejam **consultadas, inseridas, alteradas e excluídas** de maneira controlada.

O banco de dados é utilizado para persistir informações de sistemas, aplicações e processos de negócio.

Por exemplo, em um sistema de vendas, um banco de dados pode armazenar:

- Clientes;
- Produtos;
- Pedidos;
- Itens dos pedidos;
- Formas de pagamento;
- Endereços;
- Estoque.

Um banco de dados normalmente é gerenciado por um **SGBD — Sistema Gerenciador de Banco de Dados**, responsável por fornecer mecanismos para armazenamento, consulta, segurança, concorrência, transações e integridade dos dados.

Exemplos de SGBDs:

- PostgreSQL
- MySQL
- Microsoft SQL Server
- Oracle Database
- MongoDB
- Redis

⚠️ **PostgreSQL ≠ pgAdmin.** 

O PostgreSQL é quem **gerencia e executa as operações no banco**; o pgAdmin é uma ferramenta que facilita você **visualizar e administrar** o PostgreSQL, assim como DBeaver e DbKeeper, phpMyAdmin para o MySQL e o MariaDB.

## **Principais tipos de banco de dados**

De maneira geral, podemos dividir os bancos de dados em dois grandes grupos:

1. **Bancos relacionais**
2. **Bancos não relacionais — NoSQL**

A principal diferença está na maneira como os dados são **estruturados, armazenados e relacionados**.

## **Banco de Dados Relacional**

O banco de dados relacional organiza os dados em **tabelas**, compostas por:

- Linhas — registros;
- Colunas — atributos/campos.

As tabelas podem possuir relacionamentos entre si por meio de **chaves**.

### **Exemplo**

Imagine uma tabela **`cliente`**:

| **id_cliente** | **nome** | **email** |
| --- | --- | --- |
| 1 | João Silva | joao@email.com |
| 2 | Maria Souza | maria@email.com |
| 3 | Carlos Lima | carlos@email.com |

Cada linha representa um cliente.

As colunas representam as características do cliente.

Outro exemplo seria uma tabela **`pedido`**:

| **id_pedido** | **data** | **id_cliente** |
| --- | --- | --- |
| 1001 | 2026-09-10 | 1 |
| 1002 | 2026-09-10 | 2 |

O campo **`id_cliente`** permite relacionar o pedido ao respectivo cliente.

### **Exemplos de bancos relacionais**

- PostgreSQL
- MySQL
- Oracle Database
- Microsoft SQL Server
- MariaDB
- SQLite

### **Quando utilizar?**

São especialmente adequados quando:

- Existe uma estrutura de dados bem definida;
- Existem muitos relacionamentos entre os dados;
- É importante garantir integridade;
- Existem transações (conjunto de operações que o banco trata como uma única unidade de trabalho);
- É necessário utilizar consultas SQL complexas;
- A consistência dos dados é fundamental.

## **Banco de Dados Não Relacional — NoSQL**

Os bancos **NoSQL** não dependem necessariamente do modelo tradicional de tabelas relacionadas.

O termo NoSQL é geralmente associado a bancos que adotam modelos de armazenamento diferentes do relacional.

Entre os principais modelos estão:

- Documento;
- Chave-valor;
- Colunar;
- Grafos.

## **Banco orientado a documentos**

Os dados são armazenados geralmente em documentos semelhantes a JSON.

Exemplo:

```json
{
  "id": 1001,
  "cliente": {
    "nome": "João Silva",
    "email": "joao@email.com"
  },
  "produtos": [
    {
      "id": 10,
      "nome": "Notebook",
      "quantidade": 1
    },
    {
      "id": 20,
      "nome": "Mouse",
      "quantidade": 2
    }
  ]
}
```

Observe que todas as informações do pedido podem estar armazenadas em um único documento.

Um exemplo conhecido é o MongoDB.

## **Banco chave-valor**

Utiliza uma estrutura simples:

```
CHAVE       VALOR
------------------------------
usuario:10  "João Silva"
usuario:20  "Maria Souza"
```

É bastante utilizado para:

- Cache;
- Sessões;
- Dados temporários;
- Sistemas de alta velocidade.

O Redis é um exemplo.

## **Banco orientado a grafos**

Representa os dados como **nós e relacionamentos**.

Exemplo:

```
João ── É AMIGO DE ──> Maria
Maria ── É AMIGO DE ──> Carlos
João ── COMPROU ──> Produto A
```

Esse modelo é usado em:

- Redes sociais;
- Sistemas de recomendação;
- Mapas de relacionamentos;
- Sistemas de detecção de fraudes.

## **Relacional × Não Relacional**

| **Característica** | **Relacional** | **Não Relacional** |
| --- | --- | --- |
| **Estrutura** | Tabelas e relações | Documentos, chave-valor, grafos etc. |
| **Schema** | Geralmente rígido e previamente definido | Geralmente flexível |
| **Relacionamentos** | Suportados diretamente | Dependem do modelo e da tecnologia |
| **Linguagem** | SQL | Varia conforme o banco |
| **Consistência** | Forte foco em consistência e integridade dos dados | Pode priorizar disponibilidade e escalabilidade, dependendo da tecnologia |
| **Transações** | Suporte robusto a transações ACID | Suporte varia conforme o SGBD e o modelo |
| **Escalabilidade** | Tradicionalmente vertical, mas também pode ser horizontal | Frequentemente projetados para escalabilidade horizontal |
| **Exemplos** | PostgreSQL, MySQL, MariaDB | MongoDB, Redis, Neo4j |
| **Uso típico** | ERP, sistemas financeiros, vendas | Big Data, cache, conteúdo, aplicações de alta escala |

Não existe um modelo universalmente "melhor". A escolha depende dos requisitos da aplicação.

## **Banco de Dados Relacional: Tabela, Registro e Campo**

### **Tabela**

Representa uma entidade ou conjunto de informações.

```
CLIENTE
```

### **Registro**

É uma linha da tabela.

```
1 | João Silva | joao@email.com
```

### **Campo**

É uma coluna.

```
id_cliente
nome
email
```

Podemos representar:

| **id_cliente** | **nome** | **email** |
| --- | --- | --- |
| 1 | João Silva | joao@email.com |

Nesse exemplo:

- **`cliente`** → tabela;
- **`1 | João Silva | joao@email.com`** → registro;
- **`id_cliente`**, **`nome`** e **`email`** → campos.


## **Tipos de Dados**

Cada coluna deve possuir um **tipo de dado**, determinando quais valores podem ser armazenados.

Os tipos disponíveis variam de acordo com o SGBD.

## **Tipos numéricos**

Exemplos:

```
INTEGER
SMALLINT
BIGINT
DECIMAL
NUMERIC
REAL
DOUBLE PRECISION
```

Exemplo:

```sql
quantidade INTEGER
```

Para valores monetários, normalmente é preferível utilizar tipos de precisão exata, como:

```sql
preco DECIMAL(10,2)
```

Isso permite valores como:

```
1599.90
```


## **Tipos de texto**

Exemplos:

```
CHAR
VARCHAR
TEXT
```

Exemplo:

```sql
nome VARCHAR(100)
```

O **`VARCHAR(100)`** permite armazenar uma string de até 100 caracteres, conforme as regras do SGBD.


## **Data e hora**

Exemplos:

```
DATE
TIME
TIMESTAMP
```

Exemplo:

```sql
data_cadastro TIMESTAMP
```


## **Booleano**

Representa valores verdadeiro/falso.

```sql
ativo BOOLEAN
```

Exemplo:

```
TRUE
FALSE
```


## **Chave Primária — Primary Key (PK)**

A Primary Key (PK) é utilizada para **identificar unicamente** cada registro de uma tabela.

Exemplo:

```sql
CREATE TABLE cliente (
    id_cliente INTEGER PRIMARY KEY,
    nome VARCHAR(100)
);
```

Dados:

| **id_cliente** | **nome** |
| --- | --- |
| 1 | João |
| 2 | Maria |
| 3 | Carlos |

O **`id_cliente`** identifica cada cliente.

Uma PK deve ser:

- Única;
- Não nula;
- Estável;
- Capaz de identificar um registro.


## **Chave Estrangeira — Foreign Key (FK)**

A Foreign Key (FK) é utilizada para estabelecer um **relacionamento entre tabelas**.

Considere:

```
CLIENTE
---------
id_cliente
nome
```

e:

```
PEDIDO
---------
id_pedido
data
id_cliente
```

O campo **`pedido.id_cliente`** pode ser uma FK que referencia **`cliente.id_cliente`**.

Exemplo:

```sql
CREATE TABLE pedido (
    id_pedido INTEGER PRIMARY KEY,
    data_pedido DATE NOT NULL,
    id_cliente INTEGER NOT NULL,

    FOREIGN KEY (id_cliente)
        REFERENCES cliente(id_cliente)
);
```

Assim:

```
CLIENTE
   |
   | 
   | id_cliente
   |
   v
PEDIDO
```

A FK ajuda a garantir a **integridade referencial**.

Por exemplo, o banco pode impedir que seja criado um pedido para um cliente inexistente.

## **Constraints**

**Constraints** são restrições aplicadas aos dados para garantir **regras de integridade**.

As principais são:

- **`PRIMARY KEY`**
- **`FOREIGN KEY`**
- **`NOT NULL`**
- **`UNIQUE`**
- **`CHECK`**
- **`DEFAULT`**


## **NOT NULL**

Determina que uma coluna não pode receber **`NULL`**.

```sql
nome VARCHAR(100) NOT NULL
```

Isso significa que o nome deve obrigatoriamente ser informado.


## **UNIQUE**

Garante que os valores não sejam duplicados.

```sql
email VARCHAR(150) UNIQUE
```

Exemplo:

```
joao@email.com
```

Não poderá aparecer novamente na coluna.


## **CHECK**

Define uma condição que deve ser satisfeita.

```sql
idade INTEGER CHECK (idade >= 18)
```

Ou:

```sql
preco DECIMAL(10,2) CHECK (preco >= 0)
```


## **DEFAULT**

Define um valor padrão.

```sql
ativo BOOLEAN DEFAULT TRUE
```

Se nenhum valor for informado, o banco poderá utilizar:

```
TRUE
```

# **SQL**

**SQL — Structured Query Language** é uma linguagem utilizada principalmente para trabalhar com bancos de dados relacionais.

Com SQL podemos:

- Criar tabelas;
- Inserir dados;
- Consultar dados;
- Atualizar dados;
- Excluir dados;
- Criar relacionamentos;
- Definir restrições;
- Controlar permissões.

Exemplo:

```sql
CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE
);
```

Inserção:

```sql
INSERT INTO cliente (id_cliente, nome, email)
VALUES (1, 'João Silva', 'joao@email.com');
```

Consulta:

```sql
SELECT *
FROM cliente;
```

## **Classificação dos comandos SQL**

A linguagem SQL possui diferentes grupos de comandos, classificados de acordo com sua finalidade.

As principais categorias são:

- **DDL — Data Definition Language**
- **DML — Data Manipulation Language**
- **DQL — Data Query Language**
- **DCL — Data Control Language**
- **TCL — Transaction Control Language**

Essa divisão ajuda a compreender qual é a finalidade de cada comando dentro de um banco de dados.


## **DDL — Data Definition Language**

**DDL (Data Definition Language)** é utilizada para definir e modificar a **estrutura do banco de dados**.

Ela trabalha principalmente com objetos como:

- Tabelas;
- Bancos de dados;
- Índices;
- Views;
- Constraints;
- Schemas.

### **Principais comandos DDL**

| **Comando** | **Finalidade** |
| --- | --- |
| **`CREATE`** | Cria objetos |
| **`ALTER`** | Modifica objetos |
| **`DROP`** | Remove objetos |
| **`TRUNCATE`** | Remove todos os registros de uma tabela |

### **CREATE**

Cria um objeto.

```sql
CREATE TABLE cliente (
    id_cliente INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150)
);
```

Nesse exemplo, **`CREATE TABLE`** cria a estrutura da tabela **`cliente`**.

### **ALTER**

Modifica a estrutura de um objeto existente.

Por exemplo, adicionando uma coluna:

```sql
ALTER TABLE cliente
ADD telefone VARCHAR(20);
```

### **DROP**

Remove um objeto.

```sql
DROP TABLE cliente;
```

Nesse caso, a tabela é removida.

**Atenção:** **`DROP TABLE`** não remove apenas os registros. Ele remove a própria estrutura da tabela.

### **TRUNCATE**

Remove todos os registros de uma tabela, mantendo sua estrutura.

```sql
TRUNCATE TABLE cliente;
```

Depois do **`TRUNCATE`**, a tabela continua existindo, mas seus registros são removidos.


## **DML — Data Manipulation Language**

**DML (Data Manipulation Language)** é utilizada para **manipular os dados armazenados nas tabelas**.

Os principais comandos são:

- **`INSERT`**
- **`UPDATE`**
- **`DELETE`**


## **INSERT**

Utilizado para inserir registros.

```sql
INSERT INTO cliente (
    id_cliente,
    nome,
    email
)
VALUES (
    1,
    'João Silva',
    'joao@email.com'
);
```

Após o comando, a tabela poderá conter:

| **id_cliente** | **nome** | **email** |
| --- | --- | --- |
| 1 | João Silva | joao@email.com |

## **UPDATE**

Utilizado para alterar registros existentes.

```sql
UPDATE cliente
SET email = 'joao.silva@email.com'
WHERE id_cliente = 1;
```

O **`WHERE`** é extremamente importante.

Sem ele:

```sql
UPDATE cliente
SET email = 'novo@email.com';
```

a instrução poderá alterar **todos os registros** da tabela.


## **DELETE**

Utilizado para excluir registros.

```sql
DELETE FROM cliente
WHERE id_cliente = 1;
```

Assim como no **`UPDATE`**, deve-se ter cuidado com o **`WHERE`**.

```sql
DELETE FROM cliente;
```

Essa instrução pode excluir todos os registros da tabela.


## **DQL — Data Query Language**

**DQL (Data Query Language)** é utilizada para **consultar dados**.

O principal comando é:

```sql
SELECT
```

Exemplo:

```sql
SELECT *
FROM cliente;
```

O comando retorna os registros da tabela.

Também podemos selecionar apenas algumas colunas:

```sql
SELECT
    nome,
    email
FROM cliente;
```

## **SELECT com WHERE**

O **`WHERE`** permite filtrar os registros.

```sql
SELECT *
FROM cliente
WHERE id_cliente = 1;
```

Podemos utilizar operadores:

```sql
SELECT *
FROM produto
WHERE preco > 100;
```

Ou:

```sql
SELECT *
FROM produto
WHERE estoque > 0;
```

## **SELECT com ORDER BY**

Permite ordenar os resultados.

```sql
SELECT *
FROM produto
ORDER BY preco ASC;
```

**`ASC`** significa ordem crescente.

Para ordem decrescente:

```sql
SELECT *
FROM produto
ORDER BY preco DESC;
```

## **SELECT com JOIN**

Uma das características mais importantes dos bancos relacionais é a possibilidade de consultar informações de várias tabelas.

Por exemplo:

```sql
SELECT
    cliente.nome,
    pedido.id_pedido,
    pedido.data_pedido
FROM cliente
INNER JOIN pedido
    ON pedido.id_cliente = cliente.id_cliente;
```

Nesse exemplo, o **`JOIN`** relaciona:

```
CLIENTE
   ↓
PEDIDO
```

permitindo consultar dados das duas tabelas.


## **DCL — Data Control Language**

**DCL (Data Control Language)** é utilizada para controlar **permissões e acessos** aos objetos do banco de dados.

Os principais comandos são:

- **`GRANT`**
- **`REVOKE`**


## **GRANT**

Concede uma permissão.

Exemplo:

```sql
GRANT SELECT
ON cliente
TO usuario_consulta;
```

Nesse exemplo, o usuário **`usuario_consulta`** recebe permissão para consultar a tabela **`cliente`**.

Também podemos conceder múltiplas permissões:

```sql
GRANT SELECT, INSERT, UPDATE
ON cliente
TO usuario_operador;
```


## **REVOKE**

Remove uma permissão anteriormente concedida.

```sql
REVOKE UPDATE
ON cliente
FROM usuario_operador;
```

Nesse caso, o usuário deixa de possuir a permissão de **`UPDATE`** sobre a tabela.

### **Objetivo do DCL**

O DCL está relacionado principalmente à **segurança e controle de acesso**.

Por exemplo, uma empresa pode ter:

```
ADMINISTRADOR
    ↓
Acesso total

ANALISTA
    ↓
SELECT

OPERADOR
    ↓
SELECT + INSERT + UPDATE
```

Dessa forma, cada usuário recebe somente as permissões necessárias para desempenhar sua função.


## **TCL — Transaction Control Language**

**TCL (Transaction Control Language)** é utilizada para controlar **transações** no banco de dados.

Os principais comandos são:

- **`COMMIT`**
- **`ROLLBACK`**
- **`SAVEPOINT`**

Uma transação representa um conjunto de operações que deve ser tratado de maneira controlada.


## **COMMIT**

Confirma as alterações realizadas na transação.

Exemplo:

```sql
BEGIN;

UPDATE conta
SET saldo = saldo - 100
WHERE id_conta = 1;

UPDATE conta
SET saldo = saldo + 100
WHERE id_conta = 2;

COMMIT;
```

Após o **`COMMIT`**, as alterações são confirmadas.


## **ROLLBACK**

Desfaz as alterações ainda não confirmadas da transação.

```sql
BEGIN;

UPDATE conta
SET saldo = saldo - 100
WHERE id_conta = 1;

ROLLBACK;
```

O **`UPDATE`** será desfeito, conforme o comportamento transacional do SGBD e do contexto da operação.

## **Resumo dos comandos SQL**

| **Categoria** | **Significado** | **Objetivo** | **Principais comandos** |
| --- | --- | --- | --- |
| **DDL** | Data Definition Language | Estrutura | **`CREATE`**, **`ALTER`**, **`DROP`**, **`TRUNCATE`** |
| **DML** | Data Manipulation Language | Manipulação de dados | **`INSERT`**, **`UPDATE`**, **`DELETE`** |
| **DQL** | Data Query Language | Consulta | **`SELECT`** |
| **DCL** | Data Control Language | Permissões | **`GRANT`**, **`REVOKE`** |
| **TCL** | Transaction Control Language | Transações | **`COMMIT`**, **`ROLLBACK`**, |


## **Exemplo prático**

Considere a tabela:

### **DDL — criando a tabela**

```sql
CREATE TABLE produto (
    id_produto INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque INTEGER NOT NULL DEFAULT 0
);
```

### **DML — inserindo um produto**

```sql
INSERT INTO produto (
    id_produto,
    nome,
    preco,
    estoque
)
VALUES (
    1,
    'Notebook',
    3500.00,
    10
);
```

### **DQL — consultando**

```sql
SELECT *
FROM produto;
```

### **DML — alterando**

```sql
UPDATE produto
SET preco = 3299.90
WHERE id_produto = 1;
```

### **DML — excluindo**

```sql
DELETE FROM produto
WHERE id_produto = 1;
```

### **DDL — alterando a estrutura**

```sql
ALTER TABLE produto
ADD descricao TEXT;
```

### **DCL — concedendo acesso**

```sql
GRANT SELECT
ON produto
TO usuario;
```

### **TCL — controlando uma transação**

```sql
BEGIN;

UPDATE produto
SET estoque = estoque - 1
WHERE id_produto = 1;

COMMIT;
```

## **Modelo MER**

**MER — Modelo Entidade-Relacionamento** é uma representação conceitual dos dados e de seus relacionamentos.

Ele é utilizado durante a etapa de **modelagem do banco de dados**.

O MER procura responder perguntas como:

- Quais são as entidades?
- Quais são seus atributos?
- Como as entidades se relacionam?
- Qual é a cardinalidade desses relacionamentos?


## **Entidade**

Uma **entidade** representa algo relevante para o domínio do sistema.

Exemplo de um sistema de vendas:

```
CLIENTE
PRODUTO
PEDIDO
VENDEDOR
CATEGORIA
```

Podemos imaginar:

```
CLIENTE
----------------
id_cliente
nome
email
telefone
```


## **Atributos**

Os **atributos** representam características de uma entidade.

Para **`CLIENTE`**:

```
CLIENTE
 ├── id_cliente
 ├── nome
 ├── email
 └── telefone
```

Para **`PRODUTO`**:

```
PRODUTO
 ├── id_produto
 ├── nome
 ├── preco
 └── estoque
```


## **Relacionamentos**

Um relacionamento representa uma associação entre entidades.

Exemplo:

```
CLIENTE realiza PEDIDO
```

Podemos representar:

```
CLIENTE ───── realiza ───── PEDIDO
```

Outro exemplo:

```
PEDIDO ───── possui ───── PRODUTO
```


## **Cardinalidade**

A cardinalidade determina **quantas ocorrências de uma entidade podem estar relacionadas com outra**.

Os principais casos são:

- 1:1 — um para um;
- 1:N — um para muitos;
- N:N — muitos para muitos.


## **Relacionamento 1:N**

Exemplo:

> Um cliente pode realizar vários pedidos.
> 

```
CLIENTE 1 ───────── N PEDIDO
```

Um cliente:

```
João
```

pode possuir:

```
Pedido 1
Pedido 2
Pedido 3
```

Mas cada pedido pertence a um cliente.


## **Relacionamento 1:1**

Exemplo:

```
PESSOA 1 ───────── 1 PASSAPORTE
```

Uma pessoa possui um passaporte e, considerando a regra do domínio, cada passaporte pertence a uma pessoa.


## **Relacionamento N:N**

Exemplo:

> Um pedido pode possuir vários produtos e um produto pode estar presente em vários pedidos.
> 

```
PEDIDO N ───────── N PRODUTO
```

Em um banco relacional, normalmente precisamos criar uma entidade/tabela intermediária.

```
PEDIDO
   |
   N
   |
ITEM_PEDIDO
   |
   N
   |
PRODUTO
```


## **Modelo Lógico**

Depois do modelo conceitual/MER, podemos construir o **modelo lógico**.

O modelo lógico transforma as entidades e relacionamentos em estruturas mais próximas do banco de dados:

- Tabelas;
- Colunas;
- Chaves primárias;
- Chaves estrangeiras;
- Tipos de dados;
- Restrições.

Por exemplo, no MER temos:

```
CLIENTE 1 ───── N PEDIDO
```

No modelo lógico:

```
CLIENTE
---------------------
PK id_cliente
   nome
   email
```

```
PEDIDO
---------------------
PK id_pedido
   data_pedido
FK id_cliente
```

A FK fica no lado N do relacionamento 1:N.


## **MER × Modelo Lógico**

Uma forma simples de entender:

```
REQUISITOS
    ↓
MODELO CONCEITUAL / MER
    ↓
MODELO LÓGICO
    ↓
MODELO FÍSICO
    ↓
BANCO DE DADOS
```

### **MER**

Preocupa-se principalmente com:

```
Entidades
Atributos
Relacionamentos
Cardinalidades
```

### **Modelo lógico**

Preocupa-se com:

```
Tabelas
Colunas
PK
FK
Tipos de dados
Constraints
```

### **Modelo físico**

Preocupa-se com detalhes específicos da implementação no SGBD:

```
CREATE TABLE
Índices
Particionamento
Tipos específicos do SGBD
Configurações de armazenamento
Performance
```


## **Cenário prático — Sistema de vendas**

### **Requisitos**

Uma empresa deseja desenvolver um sistema para controlar suas vendas.

O sistema precisa armazenar:

- Clientes;
- Produtos;
- Categorias;
- Pedidos;
- Produtos vendidos em cada pedido.

As regras são:

1. Um cliente pode realizar vários pedidos.
2. Cada pedido pertence a um único cliente.
3. Uma categoria pode possuir vários produtos.
4. Cada produto pertence a uma categoria.
5. Um pedido pode possuir vários produtos.
6. Um produto pode aparecer em vários pedidos.
7. Para cada produto vendido no pedido, devemos armazenar a quantidade e o preço praticado na venda.


## **Identificando as entidades**

A partir dos requisitos, podemos identificar:

```
CLIENTE
CATEGORIA
PRODUTO
PEDIDO
ITEM_PEDIDO
```

Por que **`ITEM_PEDIDO`**?

Porque existe um relacionamento N:N entre:

```
PEDIDO ↔ PRODUTO
```

E precisamos armazenar informações específicas desse relacionamento:

```
quantidade
preco_unitario
```

Portanto, criamos uma entidade associativa:

```
ITEM_PEDIDO
```


## **Identificando os atributos**

### **CLIENTE**

```
id_cliente
nome
email
telefone
```

### **CATEGORIA**

```
id_categoria
nome
```

### **PRODUTO**

```
id_produto
nome
preco
estoque
```

### **PEDIDO**

```
id_pedido
data_pedido
status
```

### **ITEM_PEDIDO**

```
id_item
quantidade
preco_unitario
```


## **Identificando os relacionamentos**

Temos:

```
CLIENTE 1 ───── N PEDIDO
```

```
CATEGORIA 1 ───── N PRODUTO
```

E:

```
PEDIDO 1 ───── N ITEM_PEDIDO
```

```
PRODUTO 1 ───── N ITEM_PEDIDO
```

O modelo completo fica conceitualmente:

```
                         ┌──────────────┐
                         │   CATEGORIA  │
                         └──────┬───────┘
                                │ 1
                                │
                                │ N
                         ┌──────▼───────┐
                         │   PRODUTO    │
                         └──────┬───────┘
                                │ 1
                                │
                                │ N
                         ┌──────▼───────┐
                         │ ITEM_PEDIDO  │
                         └──────┬───────┘
                                │ N
                                │
                                │ 1
                         ┌──────▼───────┐
                         │    PEDIDO    │
                         └──────┬───────┘
                                │ N
                                │
                                │ 1
                         ┌──────▼───────┐
                         │   CLIENTE    │
                         └──────────────┘
```


## **Transformando o MER em modelo lógico**

Agora transformamos as entidades em tabelas.

### **CLIENTE**

```
CLIENTE
---------------
PK id_cliente
   nome
   email
   telefone
```

### **CATEGORIA**

```
CATEGORIA
-----------------
PK id_categoria
   nome
```

### **PRODUTO**

```
PRODUTO
------------------
PK id_produto
   nome
   preco
   estoque
FK id_categoria
```

### **PEDIDO**

```
PEDIDO
------------------
PK id_pedido
   data_pedido
   status
FK id_cliente
```

### **ITEM_PEDIDO**

```
ITEM_PEDIDO
-------------------
PK id_item
   quantidade
   preco_unitario
FK id_pedido
FK id_produto
```

## **Visualização do modelo lógico**

```
┌──────────────────────┐
│       CLIENTE        │
├──────────────────────┤
│ PK id_cliente        │
│    nome              │
│    email             │
│    telefone          │
└──────────┬───────────┘
           │
           │ 1:N
           │
┌──────────▼───────────┐
│        PEDIDO        │
├──────────────────────┤
│ PK id_pedido         │
│    data_pedido       │
│    status            │
│ FK id_cliente        │
└──────────┬───────────┘
           │
           │ 1:N
           │
┌──────────▼───────────┐
│     ITEM_PEDIDO      │
├──────────────────────┤
│ PK id_item           │
│    quantidade        │
│    preco_unitario    │
│ FK id_pedido         │
│ FK id_produto        │
└──────────┬───────────┘
           │
           │ N:1
           │
┌──────────▼───────────┐
│       PRODUTO        │
├──────────────────────┤
│ PK id_produto        │
│    nome              │
│    preco             │
│    estoque           │
│ FK id_categoria      │
└──────────┬───────────┘
           │
           │ N:1
           │
┌──────────▼───────────┐
│      CATEGORIA       │
├──────────────────────┤
│ PK id_categoria      │
│    nome              │
└──────────────────────┘
```

## **Implementação em SQL**

```sql
CREATE TABLE cliente (
    id_cliente INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    telefone VARCHAR(20)
);

CREATE TABLE categoria (
    id_categoria INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE produto (
    id_produto INTEGER PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    preco DECIMAL(10,2) NOT NULL CHECK (preco >= 0),
    estoque INTEGER NOT NULL DEFAULT 0 CHECK (estoque >= 0),
    id_categoria INTEGER NOT NULL,

    CONSTRAINT fk_produto_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES categoria(id_categoria)
);

CREATE TABLE pedido (
    id_pedido INTEGER PRIMARY KEY,
    data_pedido DATE NOT NULL,
    status VARCHAR(30) NOT NULL,
    id_cliente INTEGER NOT NULL,

    CONSTRAINT fk_pedido_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES cliente(id_cliente)
);

CREATE TABLE item_pedido (
    id_item INTEGER PRIMARY KEY,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    preco_unitario DECIMAL(10,2) NOT NULL CHECK (preco_unitario >= 0),
    id_pedido INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,

    CONSTRAINT fk_item_pedido
        FOREIGN KEY (id_pedido)
        REFERENCES pedido(id_pedido),

    CONSTRAINT fk_item_produto
        FOREIGN KEY (id_produto)
        REFERENCES produto(id_produto)
);
```

## **Resumo dos principais conceitos**

| **Conceito** | **Definição** |
| --- | --- |
| Banco de dados | Conjunto organizado de dados persistidos |
| SGBD | Software responsável por gerenciar o banco |
| Banco relacional | Organiza dados principalmente em tabelas relacionadas |
| NoSQL | Família de bancos que utiliza modelos não relacionais |
| Tabela | Estrutura que armazena registros |
| Registro | Uma ocorrência/linha de uma tabela |
| Campo | Coluna que representa um atributo |
| PK | Identifica unicamente um registro |
| FK | Referencia uma chave de outra tabela |
| Constraint | Restrição que garante regras de integridade |
| MER | Modelo conceitual das entidades e relacionamentos |
| Modelo lógico | Representação em tabelas, chaves e atributos |
| Cardinalidade | Define a quantidade de ocorrências em um relacionamento |
| 1:1 | Um para um |
| 1:N | Um para muitos |
| N:N | Muitos para muitos |
| SQL | Linguagem utilizada para trabalhar com bancos relacionais |
