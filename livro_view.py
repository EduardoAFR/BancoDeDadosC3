# views/livro_view.py
from controllers.livro_controller import LivroController

def exibir_livros():
    livros = LivroController.listar_livros()
    for livro in livros:
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Gênero: {livro['genero']}, Ano: {livro['ano']}")

def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    ano = int(input("Digite o ano de publicação: "))
    livro_id = LivroController.criar_livro(titulo, autor, genero, ano)
    print(f"Livro adicionado com ID: {livro_id}")

def atualizar_livro():
    id_livro = input("Digite o ID do livro que deseja atualizar: ")
    titulo = input("Digite o novo título (ou deixe em branco para manter o atual): ")
    autor = input("Digite o novo autor (ou deixe em branco para manter o atual): ")
    genero = input("Digite o novo gênero (ou deixe em branco para manter o atual): ")
    ano = input("Digite o novo ano de publicação (ou deixe em branco para manter o atual): ")

    novos_dados = {}
    if titulo: novos_dados["titulo"] = titulo
    if autor: novos_dados["autor"] = autor
    if genero: novos_dados["genero"] = genero
    if ano: novos_dados["ano"] = int(ano)

    atualizados = LivroController.atualizar_livro(id_livro, novos_dados)
    print(f"{atualizados} registro(s) atualizado(s).")

def deletar_livro():
    id_livro = input("Digite o ID do livro que deseja deletar: ")
    deletados = LivroController.deletar_livro(id_livro)
    print(f"{deletados} registro(s) deletado(s).")
