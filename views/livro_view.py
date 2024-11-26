from controllers.livro_controller import LivroController

def listar_livros():
    livros = LivroController.listar_livros()
    for livro in livros:
        print(f"ID: {livro['id_livro']}, Título: {livro['titulo']}, Autor: {livro['autor']}, Gênero: {livro['genero']}")

    if not livros:
        print("Não há livros cadastrados.")
        return

def criar_livro():
    id_livro = input("Digite o ID do livro: ")
    titulo = input("Digite o título do livro: ")
    autor_id = input("Digite o ID do autor: ")
    genero_id = input("Digite o ID do gênero: ")
    resultado = LivroController.criar_livro(id_livro, titulo, autor_id, genero_id)


    if resultado["sucesso"]:
        print(resultado["mensagem"])
        print(f"Livro adicionado com ID: {id_livro}")
    else:
        print(f"Erro: {resultado['mensagem']}")
   
def atualizar_livro():

    livros = LivroController.listar_livros()

    if not livros:
        print("Não há livros cadastrados.")
        return

    # Lista os livros
    print("\nLista de Livros:")
    for i, livro in enumerate(livros, 1):
        print(f"{i}. ID: {livro['id_livro']}, Título: {livro['titulo']}, "
              f"Autor: {livro['autor']}, Gênero: {livro['genero']}")

    # Solicita os dados do usuário
    id_livro = input("Digite o ID do livro que deseja atualizar: ")
    titulo = input("Digite o novo título (ou deixe em branco para manter o atual): ")
    autor_id = input("Digite o novo ID do autor (ou deixe em branco para manter o atual): ")
    genero_id = input("Digite o novo ID do gênero (ou deixe em branco para manter o atual): ")

    # Validação básica para evitar que todos os campos sejam deixados em branco
    if not titulo.strip() and not autor_id.strip() and not genero_id.strip():
        print("Nenhum dado para atualizar foi fornecido.")
        return

    # Chamando a controller
    atualizados = LivroController.atualizar_livro(id_livro, titulo, autor_id, genero_id)

    # Feedback ao usuário
    if atualizados:
        print(f"Livro com ID {id_livro} atualizado com sucesso.")
    else:
        print(f"Nenhum livro encontrado com o ID {id_livro}.")


# main.py ou onde o menu de livros está implementado

def deletar_livro():
    while True:
        # Listando todos os livros
        livros = LivroController.listar_livros()
        if not livros:
            print("Não há livros para excluir.")
            return  # Se não houver livros, retorna ao menu anterior
        
        # Listando os livros para o usuário escolher
        print("\nLista de Livros:")
        for i, livro in enumerate(livros, 1):
            print(f"{i}. Título: {livro['titulo']}, Autor: {livro['autor']}, Gênero: {livro['genero']}")
        
        try:
            # Seleção do livro a ser deletado
            opcao = int(input("\nEscolha o número do livro que deseja excluir: ")) - 1
            livro = livros[opcao]
            print(f"\nVocê selecionou o livro:\nTítulo: {livro['titulo']}, Autor: {livro['autor']}, Gênero: {livro['genero']}")
            
            # Confirmando a exclusão
            confirmacao = input("\nDeseja realmente excluir este livro? (Sim/Não): ").strip().lower()
            if confirmacao != 'sim':
                print("Livro não excluído. Retornando ao menu de livros.")
                return  # Caso o usuário desista, volta ao menu de livros

            # Verificando se o livro está sendo referenciado em algum pedido
            excluido = LivroController.deletar_livro(livro['id_livro'])
            
            if excluido["sucesso"]:
                print(f"Pedido ID {livro['id_livro']} excluído com sucesso!")
            else:
                print(f"Erro ao tentar excluir o livro: {excluido['mensagem']}")

            # Pergunta se deseja excluir mais algum livro
            excluir_mais = input("\nDeseja excluir mais algum livro? (Sim/Não): ").strip().lower()
            if excluir_mais != 'sim':
                print("Voltando ao menu de livros...")
                return  # Caso o usuário não deseje excluir mais, retorna ao menu de livros
        except (ValueError, IndexError):
            print("Opção inválida. Tente novamente.")

