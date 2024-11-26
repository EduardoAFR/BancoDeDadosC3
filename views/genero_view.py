from controllers.genero_controller import GeneroController

def listar_generos():
    generos = GeneroController.listar_generos()
    for genero in generos:
        print(f"ID: {genero['IdGenero']}, Nome: {genero['nome']}")

    if not generos:
        print("Não há gêneros cadastrados.")
        return

def criar_genero():
    id_genero = input("Digite o ID do gênero: ")
    nome = input("Digite o nome do gênero: ")
    genero_id = GeneroController.criar_genero(id_genero, nome)
    print(f"Gênero adicionado com ID: {id_genero}")

def atualizar_genero():

    generos = GeneroController.listar_generos()

    if not generos:
        print("Não há gêneros cadastrados.")
        return

    # Lista os gêneros
    print("\nLista de Gêneros:")
    for i, genero in enumerate(generos, 1):
        print(f"{i}. ID: {genero['IdGenero']}, Nome: {genero['nome']}")

        # Coleta de dados do usuário
    id_genero = input("Digite o ID do gênero que deseja atualizar: ")
    nome = input("Digite o novo nome: ")

    # Validação básica
    if not nome.strip():
        print("O nome não pode estar vazio!")
        return

    # Chamada para a controller
    atualizados = GeneroController.atualizar_genero(id_genero, nome)

    # Mensagens ao usuário
    if atualizados:
        print(f"Gênero com ID {id_genero} atualizado para '{nome}'.")
    else:
        print(f"Nenhum gênero encontrado com ID {id_genero}.")

def deletar_genero():
    while True:
        # Listando todos os gêneros
        generos = GeneroController.listar_generos()
        if not generos:
            print("Não há gêneros para excluir.")
            return  # Se não houver gêneros, retorna ao menu anterior
        
        # Listando os gêneros para o usuário escolher
        print("\nLista de Gêneros:")
        for i, genero in enumerate(generos, 1):
            print(f"{i}. Gênero: {genero['nome']}")
        
        try:
            # Seleção do gênero a ser deletado
            opcao = int(input("\nEscolha o número do gênero que deseja excluir: ")) - 1
            genero = generos[opcao]
            print(f"\nVocê selecionou o gênero: {genero['nome']}")
            
            # Confirmando a exclusão
            confirmacao = input("\nDeseja realmente excluir este gênero? (Sim/Não): ").strip().lower()
            if confirmacao != 'sim':
                print("Gênero não excluído. Retornando ao menu de gêneros.")
                return  # Caso o usuário desista, volta ao menu de gêneros

            # Verificando se o gênero está sendo referenciado em algum livro
            genero_deletado = GeneroController.deletar_genero(genero['_id'])
            if genero_deletado:
                print(f"Gênero '{genero['nome']}' excluído com sucesso!")
            else:
                print(f"O gênero não pode ser excluído, pois está sendo referenciado em um livro.")
                continue  # Volta ao início caso não consiga excluir o gênero

            # Pergunta se deseja excluir mais algum gênero
            excluir_mais = input("\nDeseja excluir mais algum gênero? (Sim/Não): ").strip().lower()
            if excluir_mais != 'sim':
                print("Voltando ao menu de gêneros...")
                return  # Caso o usuário não deseje excluir mais, retorna ao menu de gêneros
        except (ValueError, IndexError):
            print("Opção inválida. Tente novamente.")
