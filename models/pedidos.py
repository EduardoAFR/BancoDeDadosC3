import datetime
from connection.connection import conectar

class Pedido:
    def __init__(self,id_pedido, id_livro, quantidade, data_pedido=None):
        self.pedido = id_pedido
        self.livro = id_livro
        self.quantidade = quantidade
        self.data_pedido = data_pedido if data_pedido else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def listar_pedidos():
        db = conectar()
        collection = db["pedidos"]
        pedidos = list(collection.find())  # Obtém todos os pedidos

        # Enriquecendo os dados com o título do livro
        for pedido in pedidos:
            livro = db["livros"].find_one({"id_livro": int(pedido['livro'])})  # Busca pelo ID correto
            pedido['livro'] = livro['titulo'] if livro else 'Desconhecido'  # Adiciona o título ao pedido

        return pedidos

    @staticmethod
    def criar_pedido(id_pedido, livro_id, quantidade, data_pedido=None):
        db = conectar()
        collection = db["pedidos"]
        livros_collection = db["livros"]

         # Verificar se o ID do pedido já existe
        if collection.find_one({"id_pedido": int(id_pedido)}):
            return {"sucesso": False, "mensagem": f"Pedido com ID {id_pedido} já existe."}

        novo_pedido = {
            "id_pedido": int(id_pedido),
            "livro": int(livro_id),
            "quantidade": quantidade,
            "data_pedido": data_pedido if data_pedido else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        # Verificar se o livro existe
        if not livros_collection.find_one({"id_livro": int(livro_id)}):
         return {"sucesso": False, "mensagem": f"Livro com ID {livro_id} não encontrado."}

    # Validar a data
        try:
            datetime.datetime.strptime(data_pedido, "%Y-%m-%d")
        except ValueError:
            return {"sucesso": False, "mensagem": f"A data {data_pedido} não é válida. Use o formato AAAA-MM-DD."}


        result = collection.insert_one(novo_pedido)
        return {"sucesso": True, "mensagem": f"Pedido criado com sucesso!"}

    @staticmethod
    def atualizar_pedido(id_pedido, livro_id=None, quantidade=None, data_pedido=None):
        db = conectar()
        collection = db["pedidos"]
        
        # Monta a atualização apenas com os campos preenchidos
        atualizacoes = {}
        if livro_id.strip():
            atualizacoes["livro"] = int(livro_id)  # Converte para inteiro, se necessário
        if quantidade.strip():
            atualizacoes["quantidade"] = int(quantidade)
        if data_pedido.strip():
            atualizacoes["data_pedido"] = data_pedido

        # Atualiza apenas se houver campos para modificar
        if not atualizacoes:
            return False

        # Executa a atualização no banco de dados
        result = collection.update_one({"id_pedido": int(id_pedido)}, {"$set": atualizacoes})
        return result.modified_count > 0


    @staticmethod
    def deletar_pedido(id_pedido):
        db = conectar()
        collection = db["pedidos"]

        # Verificar se o pedido existe
        pedido = collection.find_one({"id_pedido": id_pedido})
        if not pedido:
            return {"sucesso": False, "mensagem": f"Pedido ID {id_pedido} não encontrado."}

        # Excluir o pedido
        resultado = collection.delete_one({"id_pedido": id_pedido})
        if resultado.deleted_count > 0:
            return {"sucesso": True, "mensagem": "Pedido excluído com sucesso."}
        else:
            return {"sucesso": False, "mensagem": "Erro ao tentar excluir o pedido."}
