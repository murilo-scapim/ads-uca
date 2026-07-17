produtos = []

while True:
    print("\n***** Menu ******")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Deletar produto")
    print("5 - Sair")

    opcao = int(input("Digite uma opção: "))

    match opcao:
        case 1:
            produto = input("Digite o nome do produto: ")
            produtos.append(produto)
            print("Produto adicionado!")
        case 2:
            if not produtos:
                print("Nenhum produto cadastrado!")
            else:
                for indice, produto in enumerate(produtos):
                    print(f"Cod: {indice + 1} Produto: {produto}")
        case 3:
            produto = input("Digite o nome do produto:")

            if produto in produtos:
                novo_produto = input("Digite o novo produto: ")
                indice = produtos.index(produto)
                produtos[indice] = novo_produto
                print(f"Produto {produto} atualizado para {novo_produto} ")
            else:
                print("Produto não encontrado!")
        case 4:
            produto = input("Digite o nome do produto: ")

            if produto in produtos:
                produtos.remove(produto)
                print("Produto removido!")
            else:
                print("Produto não encontrado!")
        case 5:
            print("Programa encerrado!")
            break
        case _:
            print("Opção inválida!")
