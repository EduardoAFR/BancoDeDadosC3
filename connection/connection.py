from pymongo import MongoClient

def conectar():
    # Replace the URL with your MongoDB instance details
    client = MongoClient("mongodb://localhost:27017/")
    db = client["LibraryDB"]  # Specify your database name
    return db
