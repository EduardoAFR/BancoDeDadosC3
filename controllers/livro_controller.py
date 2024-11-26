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
            resultado = Livro.deletar_livro(id_livro)
            if resultado["sucesso"]:
                return {"sucesso": True, "mensagem": resultado["mensagem"]}
            return {"sucesso": False, "mensagem": resultado["mensagem"]}
