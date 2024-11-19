# views/genero_view.py
from controllers.genero_controller import GeneroController

def exibir_generos():
    generos = GeneroController.listar_generos()
    for genero in generos:
        print(f"Nome: {genero['nome']}")

def adicionar_genero():
    nome = input("Digite o nome do gênero: ")
    genero_id = GeneroController.criar_genero(nome)
    print(f"Gênero adicionado com ID: {genero_id}")

def atualizar_genero():
    id_genero = input("Digite o ID do gênero que deseja atualizar: ")
    nome = input("Digite o novo nome (ou deixe em branco para manter o atual): ")

    novos_dados = {}
    if nome: novos_dados["nome"] = nome

    atualizados = GeneroController.atualizar_genero(id_genero, novos_dados)
    print(f"{atualizados} registro(s) atualizado(s).")

def deletar_genero():
    id_genero = input("Digite o ID do gênero que deseja deletar: ")
    deletados = GeneroController.deletar_genero(id_genero)
    print(f"{deletados} registro(s) deletado(s).")
