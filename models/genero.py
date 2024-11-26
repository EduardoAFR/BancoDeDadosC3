from connection.connection import conectar

class Genero:
    def __init__(self,id_genero, nome):
        self.id_genero = id_genero
        self.nome = nome

    @staticmethod
    def listar_generos():
        db = conectar()
        collection = db["generos"]
        return list(collection.find())

    @staticmethod
    def criar_genero(id_genero,nome):
        db = conectar()
        collection = db["generos"]
        novo_genero = {
            "IdGenero": int(id_genero),
            "nome": nome
            }
        result = collection.insert_one(novo_genero)
        return {"sucesso": True, "mensagem": f"Genero criado com sucesso!"}

    @staticmethod
    def atualizar_genero(id_genero, nome):
        db = conectar()
        collection = db["generos"]
        
        # Atualiza o campo 'nome' diretamente com a nova entrada
        result = collection.update_one(
            {"IdGenero": int(id_genero)},  # Busca pelo ID
            {"$set": {"nome": nome}}  # Atualiza diretamente o campo 'nome'
        )
        return result.modified_count  # Retorna quantos documentos foram atualizados

    @staticmethod
    def deletar_genero(id_genero):
        db = conectar()
        collection = db["generos"]

        # Verifica se o gênero está sendo referenciado em livros
        livros_collection = db["livros"]
        livro_count = livros_collection.count_documents({"genero": id_genero})

        if livro_count > 0:
            return False  # Não pode excluir o gênero, pois está em um livro

        result = collection.delete_one({"_id": id_genero})
        return result.deleted_count
