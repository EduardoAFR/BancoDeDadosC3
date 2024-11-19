# models/genero.py
from connection.connection import conectar

class Genero:
    def __init__(self, nome):
        self.nome = nome

    @staticmethod
    def listar_generos():
        db = conectar()
        collection = db["generos"]
        return list(collection.find())

    @staticmethod
    def criar_genero(nome):
        db = conectar()
        collection = db["generos"]
        novo_genero = {"nome": nome}
        result = collection.insert_one(novo_genero)
        return result.inserted_id

    @staticmethod
    def atualizar_genero(id_genero, novos_dados):
        db = conectar()
        collection = db["generos"]
        result = collection.update_one(
            {"_id": id_genero},
            {"$set": novos_dados}
        )
        return result.modified_count

    @staticmethod
    def deletar_genero(id_genero):
        db = conectar()
        collection = db["generos"]
        result = collection.delete_one({"_id": id_genero})
        return result.deleted_count
