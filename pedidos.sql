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


INSERT INTO categoria (nome)
VALUES
('Eletrônicos'),
('Informática'),
('Acessórios');

SELECT * FROM categoria;

INSERT INTO cliente(nome, email, telefone)
VALUES
('Aline', 'aline@email.com', '(11)11111-1111'),
('Adecídio', 'adecidio@email.com', '(22)22222-2222'),
('Raylan', 'raylan@email.com', '(33)33333-3333');

SELECT * FROM cliente;

INSERT INTO produto (nome, preco, estoque, id_categoria)
VALUES
('Notebook', 3500.00, 10, 2),
('Mouse sem fio', 120.00, 30, 3),
('Teclado mecânico', 280.00, 15, 3),
('Monitor 24"', 900.00, 8, 2),
('Fone Bluetooth', 250.50, 20, 1);

SELECT * FROM produto;

INSERT INTO pedido (data_pedido, status, id_cliente)
VALUES
('2026-10-08', 'Pendente', 1),
('2026-10-02', 'Pago', 2),
('2026-10-07', 'Enviado', 1);

SELECT * FROM pedido;

INSERT INTO item_pedido (id_pedido, id_produto, quantidade)
VALUES
(1, 2, 1),
(1, 3, 2),
(2, 4, 1),
(2, 5, 1),
(2, 6, 2);

SELECT * FROM item_pedido;

SELECT * FROM cliente;

SELECT id_cliente, nome, email
FROM cliente;

SELECT id_produto, nome, preco
FROM produto
WHERE preco > 500;

SELECT nome, preco
FROM produto
ORDER BY preco DESC;

SELECT * FROM produto;

UPDATE produto
SET preco = 3400.00
WHERE id_produto = 2;

SELECT * FROM pedido;

UPDATE pedido
SET status = 'Pago'
WHERE id_pedido = 1;

UPDATE produto
SET estoque = estoque + 10
WHERE id_produto = 5;

SELECT id_pedido, data_pedido FROM pedido;

SELECT * FROM pedido
WHERE status = 'Pago';

SELECT * FROM cliente
WHERE nome ILIKE '%a%';

SELECT * FROM produto;
SELECT * FROM categoria;

SELECT
	p.id_produto,
	p.nome AS produto,
	p.preco,
	c.nome AS categoria
FROM produto AS p
INNER JOIN categoria AS c
	ON c.id_categoria = p.id_categoria;


SELECT
	p.id_pedido,
	p.data_pedido,
	p.status,
	c.nome AS cliente,
	c.email
FROM pedido AS p
INNER JOIN cliente AS c
	ON c.id_cliente = p.id_cliente;


SELECT
	pe.id_pedido,
	pe.data_pedido,
	c.nome AS cliente,
	p.nome AS produto,
	ip.quantidade,
	p.preco,
	(p.preco * ip.quantidade) AS subtotal
FROM item_pedido AS ip
INNER JOIN pedido AS pe
	ON pe.id_pedido = ip.id_pedido
INNER JOIN cliente AS c
	ON c.id_cliente = pe.id_cliente
INNER JOIN produto AS p
	ON p.id_produto = ip.id_produto;


SELECT
	c.id_cliente,
	c.nome AS cliente,
	pe.id_pedido,
	pe.data_pedido,
	pe.status
FROM cliente AS C
LEFT JOIN pedido AS pe
	ON pe.id_cliente = c.id_cliente
ORDER BY c.nome DESC;

-- Cliente é a tabela da esquerda
-- Pedido é a tabela da direita
