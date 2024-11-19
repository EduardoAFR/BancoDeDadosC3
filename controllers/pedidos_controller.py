# controllers/pedidos_controller.py
from models.pedidos import Pedido
from bson.objectid import ObjectId

class PedidosController:
    @staticmethod
    def listar_pedidos():
        return Pedido.listar_pedidos()

    @staticmethod
    def criar_pedido(cliente, livros, total):
        return Pedido.criar_pedido(cliente, livros, total)

    @staticmethod
    def atualizar_pedido(id_pedido, novos_dados):
        return Pedido.atualizar_pedido(ObjectId(id_pedido), novos_dados)

    @staticmethod
    def deletar_pedido(id_pedido):
        return Pedido.deletar_pedido(ObjectId(id_pedido))
