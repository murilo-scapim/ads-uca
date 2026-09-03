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


def atualizar_produto():
    if estoque:
        descricao = input("Digite a descrição do produto a ser atualizado: ")
        produto_encontrado = buscar_produto(descricao)

        if produto_encontrado:
            nova_descricao = input("Digite a nova descrição: ")
            novo_preco_unitario = float(input("Digite o novo preço do produto: "))
            nova_quantidade = int(input("Digite a nova quantidade: "))

            produto_encontrado["descricao"] = nova_descricao
            produto_encontrado["preco_unitario"] = novo_preco_unitario
            produto_encontrado["quantidade"] = nova_quantidade

            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado!")
    else:
        print("O estoque está vazio!")


def remover_produto():
    if estoque:
        descricao = input("Digite a descrição do produto a ser removido: ")
        produto_encontrado = buscar_produto(descricao)

        if produto_encontrado:
            estoque.remove(produto_encontrado)
            print("Produto removido com sucesso!")
        else:
            print("Produto não encontrado!")
    else:
        print("O estoque está vazio!")


def dar_entrada_estoque():
    if estoque:
        descricao = input("Digite a descrição do produto para dar entrada no estoque: ")
        produto_encontrado = buscar_produto(descricao)

        if produto_encontrado:
            quantidade = int(input("Digite a quantidade a ser adicionada: "))
            produto_encontrado["quantidade"] += quantidade
            print("Entrada de estoque realizada com sucesso!")
        else:
            print("Produto não encontrado!")
    else:
        print("O estoque está vazio. Não é possível dar entrada em um produto")


def calcular_valor_total():
    total = 0

    for produto in estoque:
        total += produto["preco_unitario"] * produto["quantidade"]

    print("\n========== VALOR TOTAL DO ESTOQUE ==========")
    print(f"Valor total em estoque: R$ {total:.2f}")
    

def exibir_menu():
    print("\nEscolha uma opção: ")
    print("1 - Mostrar estoque")
    print("2 - Adcionar Produto")
    print("3 - Atualizar Produto")
    print("4 - Remover Produto")
    print("5 - Dar entrada de estoque")
    print("6 - Calcular Valor Total")
    print("0 - Sair")
