from controllers.autor_controller import AutorController

def listar_autores():
    autores = AutorController.listar_autores()
    for autor in autores:
        print(f"ID: {autor['IdAutor']}, Nome: {autor['nome']}")
        
    if not autores:
        print("Não há autores cadastrados.")
        return

def criar_autor():
    while True:
        try:
            id_autor = int(input("Digite o ID do autor (número inteiro): "))
            break
        except ValueError:
            print("Por favor, insira um número válido.")

    nome = input("Digite o nome do autor: ")
    autor_id = AutorController.criar_autor(id_autor, nome)
    print(f"Autor adicionado com ID: {id_autor}")

def atualizar_autor():

    autores = AutorController.listar_autores()

    if not autores:
        print("Não há autores cadastrados.")
        return

    # Lista os autores
    print("\nLista de Autores:")
    for i, autor in enumerate(autores, 1):
        print(f"{i}. ID: {autor['IdAutor']}, Nome: {autor['nome']}")


    id_autor = input("Digite o ID do autor que deseja atualizar: ")
    nome = input("Digite o novo nome (ou deixe em branco para manter o atual): ")
    
    if not nome.strip():
        print("O nome não pode estar vazio!")
        return
    
    atualizados = AutorController.atualizar_autor(id_autor, nome)

    if atualizados:
        print(f"Autor com ID {id_autor} atualizado para '{nome}'.")
    else:
        print(f"Nenhum autor encontrado com ID {id_autor}.")

def deletar_autor():
    while True:
        # Listando todos os autores
        autores = AutorController.listar_autores()
        if not autores:
            print("Não há autores para excluir.")
            return  # Se não houver autores, retorna ao menu anterior
        
        # Listando os autores para o usuário escolher
        print("\nLista de Autores:")
        for i, autor in enumerate(autores, 1):
            print(f"{i}. Autor: {autor['nome']}")
        
        try:
            # Seleção do autor a ser deletado
            opcao = int(input("\nEscolha o número do autor que deseja excluir: ")) - 1
            autor = autores[opcao]
            print(f"\nVocê selecionou o autor: {autor['nome']}")
            
            # Confirmando a exclusão
            confirmacao = input("\nDeseja realmente excluir este autor? (Sim/Não): ").strip().lower()
            if confirmacao != 'sim':
                print("Autor não excluído. Retornando ao menu de autores.")
                return  # Caso o usuário desista, volta ao menu de autores

            # Verificando se o autor está sendo referenciado em algum livro
            autor_deletado = AutorController.deletar_autor(autor['_id'])
            if autor_deletado:
                print(f"Autor '{autor['nome']}' excluído com sucesso!")
            else:
                print(f"O autor não pode ser excluído, pois está sendo referenciado em um livro.")
                continue  # Volta ao início caso não consiga excluir o autor

            # Pergunta se deseja excluir mais algum autor
            excluir_mais = input("\nDeseja excluir mais algum autor? (Sim/Não): ").strip().lower()
            if excluir_mais != 'sim':
                print("Voltando ao menu de autores...")
                return  # Caso o usuário não deseje excluir mais, retorna ao menu de autores
        except (ValueError, IndexError):
            print("Opção inválida. Tente novamente.")

