# controllers/livro_controller.py
from models.livro import Livro
from bson.objectid import ObjectId

class LivroController:
    @staticmethod
    def listar_livros():
        return Livro.listar_livros()

    @staticmethod
    def criar_livro(titulo, autor, genero, ano):
        return Livro.criar_livro(titulo, autor, genero, ano)

    @staticmethod
    def atualizar_livro(id_livro, novos_dados):
        return Livro.atualizar_livro(ObjectId(id_livro), novos_dados)

    @staticmethod
    def deletar_livro(id_livro):
        return Livro.deletar_livro(ObjectId(id_livro))
