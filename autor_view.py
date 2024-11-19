# views/autor_view.py
from controllers.autor_controller import AutorController

def exibir_autores():
    autores = AutorController.listar_autores()
    for autor in autores:
        print(f"Nome: {autor['nome']}, Nacionalidade: {autor['nacionalidade']}, Data de Nascimento: {autor['data_nascimento']}")

def adicionar_autor():
    nome = input("Digite o nome do autor: ")
    nacionalidade = input("Digite a nacionalidade do autor: ")
    data_nascimento = input("Digite a data de nascimento do autor (YYYY-MM-DD): ")
    autor_id = AutorController.criar_autor(nome, nacionalidade, data_nascimento)
    print(f"Autor adicionado com ID: {autor_id}")

def atualizar_autor():
    id_autor = input("Digite o ID do autor que deseja atualizar: ")
    nome = input("Digite o novo nome (ou deixe em branco para manter o atual): ")
    nacionalidade = input("Digite a nova nacionalidade (ou deixe em branco para manter a atual): ")
    data_nascimento = input("Digite a nova data de nascimento (ou deixe em branco para manter a atual): ")

    novos_dados = {}
    if nome: novos_dados["nome"] = nome
    if nacionalidade: novos_dados["nacionalidade"] = nacionalidade
    if data_nascimento: novos_dados["data_nascimento"] = data_nascimento

    atualizados = AutorController.atualizar_autor(id_autor, novos_dados)
    print(f"{atualizados} registro(s) atualizado(s).")

def deletar_autor():
    id_autor = input("Digite o ID do autor que deseja deletar: ")
    deletados = AutorController.deletar_autor(id_autor)
    print(f"{deletados} registro(s) deletado(s).")
