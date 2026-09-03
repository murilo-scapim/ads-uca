from Operacoes_crud import *

while True:
    exibir_menu()

    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            mostrar_estoque()
        case 2:
            adicionar_produto()
        case 3:
            atualizar_produto()
        case 4:
            remover_produto()
        case 5:
            dar_entrada_estoque()
        case 6:
            calcular_valor_total()
        case 0:
            print("Até logo. Saindo do programa!")
            break
        case _:
            print("Opção inválida. Tente novamente!")
        
