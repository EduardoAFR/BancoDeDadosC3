from pymongo import MongoClient
import logging

# Configuração de logging
logger = logging.getLogger(name="Library_DB_Initialization")
logger.setLevel(level=logging.WARNING)

# Lista de coleções necessárias no banco de dados
LIST_OF_COLLECTIONS = ["autores", "livros", "pedidos", "generos"]

def conectar():
    """
    Estabelece uma conexão com o banco de dados MongoDB e retorna a instância do banco.
    """
    client = MongoClient("mongodb://localhost:27017/")
    return client["libraryDB"]

def initialize_database(drop_if_exists: bool = False):
    """
    Inicializa o banco de dados MongoDB criando as coleções necessárias.

    Parâmetros:
    - drop_if_exists: Se True, exclui as coleções existentes e as recria.
    """
    db = conectar()
    existing_collections = db.list_collection_names()  # Lista as coleções existentes no banco
    
    for collection in LIST_OF_COLLECTIONS:
        if collection in existing_collections:
            if drop_if_exists:
                db.drop_collection(collection)  # Remove a coleção existente
                logger.warning(f"{collection} dropped!")
                db.create_collection(collection)  # Recria a coleção
                logger.warning(f"{collection} created!")
        else:
            db.create_collection(collection)  # Cria a coleção caso não exista
            logger.warning(f"{collection} created!")
    logger.warning("Database initialization complete.")
