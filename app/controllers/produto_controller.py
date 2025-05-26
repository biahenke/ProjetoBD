from app.models import crud

def cadastrar_produto(nome, preco, fornecedor_id):
    dados = {
        "nome": nome,
        "preco": preco,
        "fornecedor_id": fornecedor_id
    }
    crud.inserir_dado("produtos", dados)

def consultar_produtos():
    return crud.consultar_todos("produtos")

def excluir_produto(produto_id):
    crud.excluir_dado("produtos", produto_id)