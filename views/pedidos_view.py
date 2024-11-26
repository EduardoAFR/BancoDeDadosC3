from controllers.pedidos_controller import PedidoController

def listar_pedidos():
    pedidos = PedidoController.listar_pedidos()
    for pedido in pedidos:
        print(f"Id:{pedido['id_pedido']}, Livro: {pedido['livro']}, Quantidade: {pedido['quantidade']}, Data do Pedido: {pedido['data_pedido']}")

    if not pedidos:
        print("Não há pedidos cadastrados.")
        return

def criar_pedido():
    id_pedido = input("Digite o ID do pedido: ")
    livro_id = input("Digite o ID do livro: ")
    quantidade = int(input("Digite a quantidade do livro: "))
    data_pedido = input("Digite a data do pedido (formato YYYY-MM-DD): ")
    
    if not data_pedido:
        resultado = PedidoController.criar_pedido(id_pedido, livro_id, quantidade)
    else:
        resultado = PedidoController.criar_pedido(id_pedido, livro_id, quantidade, data_pedido)
    print(f"Pedido adicionado com ID: {id_pedido}")

    if resultado["sucesso"]:
        print(resultado["mensagem"])
    else:
        print(f"Erro: {resultado['mensagem']}")

def atualizar_pedido():

 # Obtém a lista de pedidos para exibir ao usuário
    pedidos = PedidoController.listar_pedidos()

    if not pedidos:
        print("Não há pedidos cadastrados.")
        return

    # Listando os pedidos para o usuário escolher
    print("\nLista de Pedidos:")
    for i, pedido in enumerate(pedidos, 1):
        print(f"{i}. ID: {pedido['id_pedido']}, Livro: {pedido['livro']}, "
              f"Quantidade: {pedido['quantidade']}, Data do Pedido: {pedido['data_pedido']}")

    # Solicita os dados do usuário
    id_pedido = input("Digite o ID do pedido que deseja atualizar: ")
    livro_id = input("Digite o novo ID do livro (ou deixe em branco para manter o atual): ")
    quantidade = input("Digite a nova quantidade (ou deixe em branco para manter a atual): ")
    data_pedido = input("Digite a nova data do pedido (ou deixe em branco para manter a atual): ")

    # Validação básica para evitar que todos os campos sejam deixados em branco
    if not livro_id.strip() and not quantidade.strip() and not data_pedido.strip():
        print("Nenhum dado para atualizar foi fornecido.")
        return

    # Chamando a controller
    atualizados = PedidoController.atualizar_pedido(id_pedido, livro_id, quantidade, data_pedido)

    # Feedback ao usuário
    if atualizados:
        print(f"Pedido com ID {id_pedido} atualizado com sucesso.")
    else:
        print(f"Nenhum pedido encontrado com o ID {id_pedido}.")


def deletar_pedido():
    while True:
        # Exibindo todos os pedidos
        pedidos = PedidoController.listar_pedidos()
        if not pedidos:
            print("Não há pedidos para excluir.")
            return  # Se não houver pedidos, retorna ao menu anterior

        # Listando os pedidos para o usuário escolher
        print("\nLista de Pedidos:")
        for i, pedido in enumerate(pedidos, 1):
            print(f"{i}. ID: {pedido['id_pedido']}, Livro: {pedido['livro']}, Quantidade: {pedido['quantidade']}, Data: {pedido['data_pedido']}")

        try:
            # Seleção do pedido a ser deletado
            opcao = int(input("\nEscolha o número do pedido que deseja excluir: ")) - 1
            pedido = pedidos[opcao]
            print(f"\nVocê selecionou o pedido:\nID: {pedido['id_pedido']}, Livro: {pedido['livro']}, Quantidade: {pedido['quantidade']}, Data: {pedido['data_pedido']}")

            # Confirmando exclusão
            confirmacao = input("\nDeseja realmente excluir este pedido? (Sim/Não): ").strip().lower()
            if confirmacao != 'sim':
                print("Pedido não excluído. Retornando ao menu.")
                return  # Sai se não houver confirmação

            # Chamar exclusão diretamente na model
            excluido = PedidoController.deletar_pedido(pedido["id_pedido"])
            
            if excluido["sucesso"]:
                print(f"Pedido ID {pedido['id_pedido']} excluído com sucesso!")
            else:
                print(f"Erro ao tentar excluir o pedido: {excluido['mensagem']}")

            # Perguntar se deseja excluir outro pedido
            excluir_mais = input("\nDeseja excluir mais algum pedido? (Sim/Não): ").strip().lower()
            if excluir_mais != 'sim':
                print("Voltando ao menu principal.")
                return
        except (ValueError, IndexError):
            print("Opção inválida. Tente novamente.")
            # Perguntar se deseja excluir outro pedido
            excluir_mais = input("\nDeseja excluir mais algum pedido? (Sim/Não): ").strip().lower()
            if excluir_mais != 'sim':
                print("Voltando ao menu principal.")
                return
        except (ValueError, IndexError):
            print("Opção inválida. Tente novamente.")

