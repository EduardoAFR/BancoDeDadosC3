from views import autor_view, genero_view, livro_view, pedidos_view
from relatorios.relatorio import relatorio_todos_autores_com_pedidos, relatorio_pedidos_por_genero
from connection.connection import conectar
from connection.connection import initialize_database

def splash_screen():
    """
    Exibe a tela de boas-vindas (Splash Screen) com o nome da aplicação,
    os componentes do grupo e o total de registros em cada coleção.
    """
    print("#" * 40)
    print("#" * 7 + " SISTEMA DE GERENCIAMENTO " + "#" * 7)
    print("#" * 40)
    print("# TOTAL DE REGISTROS EXISTENTES #")

    # Conecta ao banco de dados
    db = conectar()

    # Conta o número de documentos em cada coleção
    autores_count = db["autores"].count_documents({})
    livros_count = db["livros"].count_documents({})
    generos_count = db["generos"].count_documents({})
    pedidos_count = db["pedidos"].count_documents({})

    # Exibe os totais
    print(f"1 - AUTORES: {autores_count}")
    print(f"2 - LIVROS: {livros_count}")
    print(f"3 - GENEROS: {generos_count}")
    print(f"4 - PEDIDOS: {pedidos_count}")

    # Informações adicionais
    print("\n# CRIADO POR: Eduardo Rodrigues #")
    print("# Emanuel #")
    print("# Devandro #")
    print("\n# DISCIPLINA: BANCO DE DADOS #")
    print("# 2024/2 #")
    print("# PROFESSOR: HOWARD ROATTI #")
    print("#" * 40)


def exibir_menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Autores")
        print("3. Gerenciar Gêneros")
        print("4. Gerenciar Pedidos")
        print("5. Relatórios")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_menu_livros()
        elif opcao == "2":
            exibir_menu_autores()
        elif opcao == "3":
            exibir_menu_generos()
        elif opcao == "4":
            exibir_menu_pedidos()
        elif opcao == "5":
            exibir_relatorios()
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_menu_livros():

    while True:
        print("\nMenu de Livros:")
        print("1. Listar Livros")
        print("2. Adicionar Livro")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            livro_view.listar_livros()
        elif opcao == "2":
            livro_view.criar_livro()
        elif opcao == "3":
            livro_view.atualizar_livro()
        elif opcao == "4":
            livro_view.deletar_livro()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_menu_autores():

    while True:
        print("\nMenu de Autores:")
        print("1. Listar Autores")
        print("2. Adicionar Autor")
        print("3. Atualizar Autor")
        print("4. Deletar Autor")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            autor_view.listar_autores()
        elif opcao == "2":
            autor_view.criar_autor()
        elif opcao == "3":
            autor_view.atualizar_autor()
        elif opcao == "4":
            autor_view.deletar_autor()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_menu_generos():

    while True:
        print("\nMenu de Gêneros:")
        print("1. Listar Gêneros")
        print("2. Adicionar Gênero")
        print("3. Atualizar Gênero")
        print("4. Deletar Gênero")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            genero_view.listar_generos()
        elif opcao == "2":
            genero_view.criar_genero()
        elif opcao == "3":
            genero_view.atualizar_genero()
        elif opcao == "4":
            genero_view.deletar_genero()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_menu_pedidos():

    while True:
        print("\nMenu de Pedidos:")
        print("1. Listar Pedidos")
        print("2. Adicionar Pedido")
        print("3. Atualizar Pedido")
        print("4. Deletar Pedido")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pedidos_view.listar_pedidos()
        elif opcao == "2":
            pedidos_view.criar_pedido()
        elif opcao == "3":
            pedidos_view.atualizar_pedido()
        elif opcao == "4":
            pedidos_view.deletar_pedido()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_relatorios():
    while True:
        print("\nRelatórios:")
        print("1. Todos os Autores com Pedidos")
        print("2. Pedidos por Gênero")
        print("3. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            resultados = relatorio_todos_autores_com_pedidos()
            for resultado in resultados:
                print(f"Autor: {resultado['_id']}, Total Quantidade: {resultado['total_quantidade']}")
        elif opcao == "2":
            resultados = relatorio_pedidos_por_genero()
            for resultado in resultados:
                print(f"Gênero: {resultado['_id']}, Total Quantidade: {resultado['total_quantidade']}")
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o menu principal
if __name__ == "__main__":
    initialize_database(drop_if_exists=True)
    splash_screen()
    exibir_menu_principal()
