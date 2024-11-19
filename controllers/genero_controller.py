# controllers/genero_controller.py
from models.genero import Genero
from bson.objectid import ObjectId

class GeneroController:
    @staticmethod
    def listar_generos():
        return Genero.listar_generos()

    @staticmethod
    def criar_genero(nome):
        return Genero.criar_genero(nome)

    @staticmethod
    def atualizar_genero(id_genero, novos_dados):
        return Genero.atualizar_genero(ObjectId(id_genero), novos_dados)

    @staticmethod
    def deletar_genero(id_genero):
        return Genero.deletar_genero(ObjectId(id_genero))
