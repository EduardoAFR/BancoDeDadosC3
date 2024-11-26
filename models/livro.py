from connection.connection import conectar

class Livro:
    def __init__(self,id_livro, titulo, autor, genero):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    @staticmethod
    def listar_livros():
        db = conectar()
        collection = db["livros"]
        livros = list(collection.find())  # Obtém todos os livros

        # Enriquecendo os dados com os nomes de autor e gênero
        for livro in livros:
            autor = db["autores"].find_one({"IdAutor": livro['autor']})  # Busca por ID numérico
            genero = db["generos"].find_one({"IdGenero": livro['genero']})  # Busca por ID numérico
            
            livro['autor'] = autor['nome'] if autor else 'Desconhecido'
            livro['genero'] = genero['nome'] if genero else 'Desconhecido'
        
        return livros

    @staticmethod
    def criar_livro(id_livro, titulo, autor_id, genero_id):
        db = conectar()
        collection = db["livros"]
        autores_collection = db["autores"]
        generos_collection = db["generos"]

    # Verificar se o ID do livro já existe
        if collection.find_one({"id_livro": int(id_livro)}):
            return {"sucesso": False, "mensagem": f"Livro com ID {id_livro} já existe."}

        novo_livro = {
            "id_livro": int(id_livro),  # Garantir que seja um número
            "titulo": titulo,
            "autor": int(autor_id),  # Referência ao ID do autor
            "genero": int(genero_id)  # Referência ao ID do gênero
        }

        # Verificar se o autor existe
        if not autores_collection.find_one({"IdAutor": int(autor_id)}):
            return {"sucesso": False, "mensagem": f"Autor com ID {autor_id} não encontrado."}

        # Verificar se o gênero existe
        if not generos_collection.find_one({"IdGenero": int(genero_id)}):
            return {"sucesso": False, "mensagem": f"Gênero com ID {genero_id} não encontrado."}

        resultado = collection.insert_one(novo_livro)
        return {"sucesso": True, "mensagem": f"Livro criado com sucesso!"}

    @staticmethod
    def atualizar_livro(id_livro, titulo=None, autor_id=None, genero_id=None):
        db = conectar()
        collection = db["livros"]

        # Monta a atualização apenas com os campos preenchidos
        atualizacoes = {}
        if titulo.strip():
            atualizacoes["titulo"] = titulo
        if autor_id.strip():
            atualizacoes["autor"] = int(autor_id)  # Converte para inteiro, se necessário
        if genero_id.strip():
            atualizacoes["genero"] = int(genero_id)  # Converte para inteiro, se necessário

        # Atualiza apenas se houver campos para modificar
        if not atualizacoes:
            return False

        # Executa a atualização no banco de dados
        result = collection.update_one({"id_livro": int(id_livro)}, {"$set": atualizacoes})
        return result.modified_count > 0


    @staticmethod
    def deletar_livro(id_livro):
        db = conectar()
        collection = db["livros"]      

        resultado = collection.delete_one({"id_livro": id_livro})
        if resultado.deleted_count > 0:
            return {"sucesso": True, "mensagem": "Livro excluído com sucesso."}
        else:
            return {"sucesso": False, "mensagem": "Erro ao tentar excluir o livro."}
