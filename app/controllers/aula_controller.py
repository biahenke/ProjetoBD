from app.models import crud

def cadastrar_aula(nome, horario):
    dados = {
        "nome": nome,
        "horario": horario
    }
    crud.inserir_dado("aulas", dados)

def consultar_aulas():
    return crud.consultar_todos("aulas")

def associar_cliente_aula(cliente_id, aula_id):
    dados = {
        "cliente_id": cliente_id,
        "aula_id": aula_id
    }
    crud.inserir_dado("clientes_aulas", dados)
