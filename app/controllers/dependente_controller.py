from app.models import crud

def cadastrar_dependente(nome, idade, cliente_id):
    dados = {
        "nome": nome,
        "idade": idade,
        "cliente_id": cliente_id
    }
    crud.inserir_dado("dependentes", dados)

def consultar_dependentes():
    return crud.consultar_todos("dependentes")