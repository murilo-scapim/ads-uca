produtos = []

while True:
    print("\n------ Menu ------")
    print("[1] Adicionar produto")
    print("[2] Listar produtos")
    print("[3] Atualizar produto")
    print("[4] Remover produto")
    print("[5] Dar entrada no estoque")
    print("[6] Sair")

    operacao = input("Escolha uma operação: ")

    match operacao:
        case "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))

            produto = {
                "nome": nome,
                "preco": preco,
                "quantidade": quantidade
            }
            produtos.append(produto)
            print("Produto adicionado com sucesso!")

        case "2":
            if len(produtos) == 0:
                print("Nenhum produto cadastrado")
            else:
                print("\n --- Produtos no estoque ---")
                for produto in produtos:
                    print(f"Nome: {produto["nome"]} | Preço: {produto["preco"]:.2f} | Quantidade: {produto["quantidade"]}")