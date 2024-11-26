from models.autor import Autor

class AutorController:
    @staticmethod
    def listar_autores():
        return Autor.listar_autores()

    @staticmethod
    def criar_autor(id_autor,nome):
        return Autor.criar_autor(id_autor,nome)

    @staticmethod
    def atualizar_autor(id_autor, nome):
        return Autor.atualizar_autor(id_autor, nome)

    @staticmethod
    def deletar_autor(id_autor):
        if Autor.deletar_autor(id_autor):
            return 1  # Indica que foi deletado
        return 0  # Indica que não foi deletado
