from app.models import crud

def cadastrar_venda(cliente_id, produto_id, data):
    dados = {
        "cliente_id": cliente_id,
        "produto_id": produto_id,
        "data": data
    }
    crud.inserir_dado("vendas", dados)

def consultar_vendas():
    return crud.consultar_todos("vendas")

def excluir_venda(venda_id):
    crud.excluir_dado("vendas", venda_id)

def consultar_vendas_por_periodo(data_inicial, data_final):
    return crud.consultar_vendas_por_periodo(data_inicial, data_final)
