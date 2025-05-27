from app.models import crud

def cadastrar_fornecedor(nome, contato):
    dados = {"nome": nome, "contato": contato}
    crud.inserir_dado("fornecedores", dados)

def consultar_fornecedores():
    return crud.consultar_todos("fornecedores")

def excluir_fornecedor(fornecedor_id):
    crud.excluir_dado("fornecedores", fornecedor_id)