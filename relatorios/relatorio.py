# relatorios.py
from connection.connection import conectar

def relatorio_todos_autores_com_pedidos():
    db = conectar()
    autores_collection = db["autores"]

    # Pipeline para agregar autores, livros e pedidos
    pipeline = [
        {
            "$lookup": {
                "from": "livros",
                "localField": "IdAutor",  # Campo usado na coleção autores
                "foreignField": "autor",  # Campo usado na coleção livros
                "as": "livros_info"
            }
        },
        {
            "$unwind": {
                "path": "$livros_info",
                "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$lookup": {
                "from": "pedidos",
                "localField": "livros_info.id_livro",
                "foreignField": "livro",
                "as": "pedidos_info"
            }
        },
        {
            "$unwind": {
                "path": "$pedidos_info",
                "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$group": {
                "_id": "$nome",  # Nome do autor
                "total_quantidade": {"$sum": {"$ifNull": ["$pedidos_info.quantidade", 0]}},
            }
        },
        {
            "$sort": {"_id": 1}
        }
    ]

    resultados = list(autores_collection.aggregate(pipeline))
    return resultados


def relatorio_pedidos_por_genero():
    db = conectar()
    pedidos_collection = db["pedidos"]


    # Pipeline para agregar pedidos por gênero
    pipeline = [
        {
            "$lookup": {
                "from": "livros",
                "localField": "livro",  # Campo na coleção pedidos
                "foreignField": "id_livro",  # Campo na coleção livros
                "as": "livros_info"
            }
        },
        {
            "$unwind": {
                "path": "$livros_info",
                "preserveNullAndEmptyArrays": False
            }
        },
        {
            "$lookup": {
                "from": "generos",
                "localField": "livros_info.genero",  # Campo na coleção livros
                "foreignField": "IdGenero",  # Campo na coleção gêneros
                "as": "genero_info"
            }
        },
        {
            "$unwind": {
                "path": "$genero_info",
                "preserveNullAndEmptyArrays": False
            }
        },
        {
            "$group": {
                "_id": "$genero_info.nome",  # Nome do gênero
                "total_quantidade": {"$sum": "$quantidade"}  # Soma das quantidades de pedidos
            }
        },
        {
            "$sort": {"_id": 1}
        }
    ]

    resultados = list(pedidos_collection.aggregate(pipeline))
    return resultados
