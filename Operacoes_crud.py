estoque = []

def buscar_produto(descricao):
    for produto in estoque:
        if produto['descricao'] == descricao:
            return produto
    return None

def mostrar_estoque():
    if estoque:
        print("\nEstoque Atual:")
        for produto in estoque:
            print(f"Descrição: {produto['descricao']} | Preço Unitário: R$ {produto['preco']:.2f} | Quantidade: {produto['quantidade']}")
    else:
        print("O estoque está vazio!")

def adicionar_produto():
    descricao = input("Digite a descrição do produto: ")

    if buscar_produto(descricao):
        print("Produto já existe no estoque!")
    else:
        preco_unitario = float(input("Digite o preço unitário do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        produto = {
            "descricao": descricao,
            "preco": preco_unitario,
            "quantidade": quantidade
        }
        estoque.append(produto)
        print("Produto adicionado com sucesso!")


adicionar_produto()

mostrar_estoque()
