from app.models import crud

def cadastrar_ficha_medica(cliente_id, altura, peso, observacoes):
    crud.criar_ficha_medica(cliente_id, altura, peso, observacoes)

def consultar_ficha_medica_por_cliente(cliente_id):
    return crud.consultar_ficha_medica_por_cliente(cliente_id)