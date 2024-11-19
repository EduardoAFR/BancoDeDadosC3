# controllers/autor_controller.py
from models.autor import Autor
from bson.objectid import ObjectId

class AutorController:
    @staticmethod
    def listar_autores():
        return Autor.listar_autores()

    @staticmethod
    def criar_autor(nome, nacionalidade, data_nascimento):
        return Autor.criar_autor(nome, nacionalidade, data_nascimento)

    @staticmethod
    def atualizar_autor(id_autor, novos_dados):
        return Autor.atualizar_autor(ObjectId(id_autor), novos_dados)

    @staticmethod
    def deletar_autor(id_autor):
        return Autor.deletar_autor(ObjectId(id_autor))
