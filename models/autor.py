from connection.connection import conectar

class Autor:
    def __init__(self,id_autor, nome):
        self.id_autor = id_autor
        self.nome = nome

    @staticmethod
    def listar_autores():
        db = conectar()
        collection = db["autores"]
        return list(collection.find())

    @staticmethod
    def criar_autor(id_autor,nome):
        db = conectar()
        collection = db["autores"]
        novo_autor = {
            "IdAutor": int(id_autor),
            "nome": nome
            }
        result = collection.insert_one(novo_autor)
        return {"sucesso": True, "mensagem": f"Autor criado com sucesso!"}

    @staticmethod
    def atualizar_autor(id_autor, nome):
        db = conectar()
        collection = db["autores"]

        result = collection.update_one(
            {"IdAutor": int(id_autor)},
            {"$set": {"nome": nome}}
        )
        return result.modified_count

    @staticmethod
    def deletar_autor(id_autor):
        db = conectar()
        collection = db["autores"]

        # Verifica se o autor está sendo referenciado em livros
        livros_collection = db["livros"]
        livro_count = livros_collection.count_documents({"autor": id_autor})

        if livro_count > 0:
            return False  # Não pode excluir o autor, pois está em um livro

        result = collection.delete_one({"_id": id_autor})
        return result.deleted_count
