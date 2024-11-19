# views/pedidos_view.py
from controllers.pedidos_controller import PedidoController

def exibir_pedidos():
    pedidos = PedidoController.listar_pedidos()
    for pedido in pedidos:
        print(f"Cliente: {pedido['cliente']}, Livros: {pedido['livros']}, Total: {pedido['total']}")

def adicionar_pedido():
    cliente = input("Digite o nome do cliente: ")
    livros = input("Digite a lista de livros (separados por vírgula): ").split(",")
    total = float(input("Digite o valor total: "))
    pedido_id = PedidoController.criar_pedido(cliente, livros, total)
    print(f"Pedido adicionado com ID: {pedido_id}")

def atualizar_pedido():
    id_pedido = input("Digite o ID do pedido que deseja atualizar: ")
    cliente = input("Digite o novo nome do cliente (ou deixe em branco): ")
    livros = input("Digite a nova lista de livros (ou deixe em branco): ").split(",")
    total = input("Digite o novo valor total (ou deixe em branco): ")

    novos_dados = {}
    if cliente: novos_dados["cliente"] = cliente
    if livros: novos_dados["livros"] = livros
    if total: novos_dados["total"] = float(total)

    atualizados = PedidoController.atualizar_pedido(id_pedido, novos_dados)
    print(f"{atualizados} registro(s) atualizado(s).")

def deletar_pedido():
    id_pedido = input("Digite o ID do pedido que deseja deletar: ")
    deletados = PedidoController.deletar_pedido(id_pedido)
    print(f"{deletados} registro(s) deletado(s).")
