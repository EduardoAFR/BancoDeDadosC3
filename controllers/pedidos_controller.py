from models.pedidos import Pedido

class PedidoController:
    
    @staticmethod
    def listar_pedidos():
        return Pedido.listar_pedidos()

    @staticmethod
    def criar_pedido(id_pedido, livro_id, quantidade, data_pedido=None):
        return Pedido.criar_pedido(id_pedido, livro_id, quantidade, data_pedido)

    @staticmethod
    def atualizar_pedido(id_pedido, livro_id=None, quantidade=None, data_pedido=None):
        # Passa os parâmetros diretamente para o model
        return Pedido.atualizar_pedido(id_pedido, livro_id, quantidade, data_pedido)

    @staticmethod
    def deletar_pedido(id_pedido):
        return Pedido.deletar_pedido(id_pedido)
