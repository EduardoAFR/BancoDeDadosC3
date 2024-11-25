# relatorios.py
from connection.connection import conectar
from bson.son import SON

def relatorio_todos_autores_com_pedidos():
    db = conectar()
    autores_collection = db["autores"]
    livros_collection = db["livros"]
    pedidos_collection = db["pedidos"]

    # Using MongoDB's aggregation framework to perform a left join-like operation
    pipeline = [
        {
            "$lookup": {
                "from": "livros",
                "localField": "_id",
                "foreignField": "id_autor",
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
                "localField": "livros_info._id",
                "foreignField": "id_livro",
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
                "_id": "$nome_autor",
                "total_quantidade": {"$sum": {"$ifNull": ["$pedidos_info.quantidade", 0]}}
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
    livros_collection = db["livros"]
    pedidos_collection = db["pedidos"]
    generos_collection = db["generos"]

    # Using aggregation to join and group data by genre
    pipeline = [
        {
            "$lookup": {
                "from": "livros",
                "localField": "id_livro",
                "foreignField": "_id",
                "as": "livros_info"
            }
        },
        {
            "$unwind": "$livros_info"
        },
        {
            "$lookup": {
                "from": "generos",
                "localField": "livros_info.id_genero",
                "foreignField": "_id",
                "as": "genero_info"
            }
        },
        {
            "$unwind": "$genero_info"
        },
        {
            "$group": {
                "_id": "$genero_info.nome_genero",
                "total_quantidade": {"$sum": "$quantidade"}
            }
        },
        {
            "$sort": {"_id": 1}
        }
    ]

    resultados = list(pedidos_collection.aggregate(pipeline))
    return resultados
