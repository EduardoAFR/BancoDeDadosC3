from models.livro import Livro

class LivroController:
    @staticmethod
    def listar_livros():
        return Livro.listar_livros()

    @staticmethod
    def criar_livro(id_livro,titulo, autor, genero):
        return Livro.criar_livro(id_livro,titulo, autor, genero)

    @staticmethod
    def atualizar_livro(id_livro, titulo, autor_id, genero_id):
        return Livro.atualizar_livro(id_livro, titulo, autor_id, genero_id)


    @staticmethod
    def deletar_livro(id_livro):
        if Livro.deletar_livro(id_livro):
            return 1  # Indica que foi deletado
        return 0  # Indica que não foi deletado
