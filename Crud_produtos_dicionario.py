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
        case "3":
            nome = input("Digite o nome do produto: ")

            econtrado = False

            for produto in produtos:
                if produto["nome"].lower() == nome.lower():
                    produto["nome"] = input("Digite o novo nome: ")
                    produto["preco"] = float(input("Digite o novo preço: "))
                    produto["quantidade"] = int(input("Digite a nova quantidade: "))
                    print("Produto atualizado com sucesso!")

                    encontrado = True
                    break

            if econtrado == False:
                print("Produto não encontrado")
        case "4":
            nome = input("Digite o nome do produto: ")

            econtrado = False

            for produto in produtos:
                if produto["nome"].lower() == nome.lower():
                    produtos.remove(produto)
                    print("Produto removido com sucesso!")
                    encontrado = True
                    break

            if encontrado == False:
                print("Produto não encontrado")
        case "5":
            nome = input("Digite o nome do produto: ")

            for produto in produtos:
                if produto["nome"].lower() == nome.lower():
                    entrada = int(input("Digite a quantidade: "))
                    produto["quantidade"] += entrada  # produto["quantidade"] =  produto["quantidade"] + entrada

                    print("Estoque atualizado com sucesso!")
                    encontrado = True
                    break

            if encontrado == False:
                print("Produto não encontrado")
        case "6":
            print("Programa encerrado. Até logo!")
            break
        case _:
            print("Opção inválida!")
