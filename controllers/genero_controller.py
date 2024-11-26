from models.genero import Genero

class GeneroController:
    @staticmethod
    def listar_generos():
        return Genero.listar_generos()

    @staticmethod
    def criar_genero(id_genero,nome):
        return Genero.criar_genero(id_genero,nome)

    @staticmethod
    def atualizar_genero(id_genero, nome):
        return Genero.atualizar_genero(id_genero, nome)
   
    @staticmethod
    def deletar_genero(id_genero):
        if Genero.deletar_genero(id_genero):
            return 1  # Indica que foi deletado
        return 0  # Indica que não foi deletado
