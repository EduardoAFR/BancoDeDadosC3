# models/livro.py
from connection.connection import conectar

class Livro:
    def __init__(self, titulo, autor, genero, ano):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano

    @staticmethod
    def listar_livros():
        db = conectar()
        collection = db["livros"]
        return list(collection.find())

    @staticmethod
    def criar_livro(titulo, autor, genero, ano):
        db = conectar()
        collection = db["livros"]
        novo_livro = {
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "ano": ano
        }
        result = collection.insert_one(novo_livro)
        return result.inserted_id

    @staticmethod
    def atualizar_livro(id_livro, novos_dados):
        db = conectar()
        collection = db["livros"]
        result = collection.update_one(
            {"_id": id_livro},
            {"$set": novos_dados}
        )
        return result.modified_count

    @staticmethod
    def deletar_livro(id_livro):
        db = conectar()
        collection = db["livros"]
        result = collection.delete_one({"_id": id_livro})
        return result.deleted_count
