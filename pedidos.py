# models/pedidos.py
from connection.connection import conectar

class Pedido:
    def __init__(self, cliente, livros, total):
        self.cliente = cliente
        self.livros = livros
        self.total = total

    @staticmethod
    def listar_pedidos():
        db = conectar()
        collection = db["pedidos"]
        return list(collection.find())

    @staticmethod
    def criar_pedido(cliente, livros, total):
        db = conectar()
        collection = db["pedidos"]
        novo_pedido = {"cliente": cliente, "livros": livros, "total": total}
        result = collection.insert_one(novo_pedido)
        return result.inserted_id

    @staticmethod
    def atualizar_pedido(id_pedido, novos_dados):
        db = conectar()
        collection = db["pedidos"]
        result = collection.update_one(
            {"_id": id_pedido},
            {"$set": novos_dados}
        )
        return result.modified_count

    @staticmethod
    def deletar_pedido(id_pedido):
        db = conectar()
        collection = db["pedidos"]
        result = collection.delete_one({"_id": id_pedido})
        return result.deleted_count
