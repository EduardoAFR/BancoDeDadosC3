# models/autor.py
from connection.connection import conectar

class Autor:
    def __init__(self, nome, nacionalidade, data_nascimento):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.data_nascimento = data_nascimento

    @staticmethod
    def listar_autores():
        db = conectar()
        collection = db["autores"]
        return list(collection.find())

    @staticmethod
    def criar_autor(nome, nacionalidade, data_nascimento):
        db = conectar()
        collection = db["autores"]
        novo_autor = {
            "nome": nome,
            "nacionalidade": nacionalidade,
            "data_nascimento": data_nascimento
        }
        result = collection.insert_one(novo_autor)
        return result.inserted_id

    @staticmethod
    def atualizar_autor(id_autor, novos_dados):
        db = conectar()
        collection = db["autores"]
        result = collection.update_one(
            {"_id": id_autor},
            {"$set": novos_dados}
        )
        return result.modified_count

    @staticmethod
    def deletar_autor(id_autor):
        db = conectar()
        collection = db["autores"]
        result = collection.delete_one({"_id": id_autor})
        return result.deleted_count
