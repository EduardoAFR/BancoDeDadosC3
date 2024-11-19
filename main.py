from controllers.livro_controller import LivroController
from controllers.autor_controller import AutorController
from controllers.genero_controller import GeneroController
from controllers.pedidos_controller import PedidosController
from relatorios.relatorio import relatorio_todos_autores_com_pedidos, relatorio_pedidos_por_genero

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
    livro_controller = LivroController()

    while True:
        print("\nMenu de Livros:")
        print("1. Listar Livros")
        print("2. Adicionar Livro")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            livro_controller.listar_livros()
        elif opcao == "2":
            livro_controller.adicionar_livro()
        elif opcao == "3":
            livro_controller.atualizar_livro()
        elif opcao == "4":
            livro_controller.deletar_livro()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_menu_autores():
    autor_controller = AutorController()

    while True:
        print("\nMenu de Autores:")
        print("1. Listar Autores")
        print("2. Adicionar Autor")
        print("3. Atualizar Autor")
        print("4. Deletar Autor")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            autor_controller.listar_autores()
        elif opcao == "2":
            autor_controller.adicionar_autor()
        elif opcao == "3":
            autor_controller.atualizar_autor()
        elif opcao == "4":
            autor_controller.deletar_autor()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_menu_generos():
    genero_controller = GeneroController()

    while True:
        print("\nMenu de Gêneros:")
        print("1. Listar Gêneros")
        print("2. Adicionar Gênero")
        print("3. Atualizar Gênero")
        print("4. Deletar Gênero")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            genero_controller.listar_generos()
        elif opcao == "2":
            genero_controller.adicionar_genero()
        elif opcao == "3":
            genero_controller.atualizar_genero()
        elif opcao == "4":
            genero_controller.deletar_genero()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_menu_pedidos():
    pedidos_controller = PedidosController()

    while True:
        print("\nMenu de Pedidos:")
        print("1. Listar Pedidos")
        print("2. Adicionar Pedido")
        print("3. Atualizar Pedido")
        print("4. Deletar Pedido")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pedidos_controller.listar_pedidos()
        elif opcao == "2":
            pedidos_controller.adicionar_pedido()
        elif opcao == "3":
            pedidos_controller.atualizar_pedido()
        elif opcao == "4":
            pedidos_controller.deletar_pedido()
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
    exibir_menu_principal()
