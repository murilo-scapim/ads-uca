CREATE TABLE cliente (
	id_cliente SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	email VARCHAR(150) UNIQUE,
	telefone VARCHAR(20)
);

CREATE TABLE categoria (
	id_categoria SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE produto (
	id_produto SERIAL PRIMARY KEY,
	nome VARCHAR(150) NOT NULL,
	preco DECIMAL(10, 2) NOT NULL CHECK (preco >= 0),
	estoque INTEGER NOT NULL CHECK (estoque >= 0),
	id_categoria INTEGER NOT NULL,
	CONSTRAINT fk_produto_categoria FOREIGN KEY (id_categoria)
		REFERENCES categoria (id_categoria)
);

CREATE TABLE pedido (
	id_pedido SERIAL PRIMARY KEY,
	data_pedido DATE NOT NULL,
	status VARCHAR(30) NOT NULL,
	id_cliente INTEGER NOT NULL,
	CONSTRAINT fk_pedido_cliente FOREIGN KEY (id_cliente)
		REFERENCES cliente (id_cliente)
);

CREATE TABLE item_pedido (
	id_item SERIAL PRIMARY KEY,
	id_pedido INTEGER NOT NULL,
	id_produto INTEGER NOT NULL,
	quantidade INTEGER NOT NULL CHECK (quantidade > 0),
	CONSTRAINT fk_item_pedido FOREIGN KEY (id_pedido)
		REFERENCES pedido (id_pedido),
	CONSTRAINT fk_item_produto FOREIGN KEY (id_produto)
		REFERENCES produto (id_produto)
);
