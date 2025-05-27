from app.models import crud

def cadastrar_cliente(nome, idade, email):
    dados = {
        "nome": nome,
        "idade": idade,
        "email": email
    }
    crud.inserir_dado("clientes", dados)

def consultar_clientes():
    return crud.consultar_todos("clientes")

def excluir_cliente(cliente_id):
    crud.excluir_dado("clientes", cliente_id)
