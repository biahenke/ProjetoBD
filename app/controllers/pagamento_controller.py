from app.models import crud

def registrar_pagamento(venda_id, valor_pago, data_pagamento, metodo_pagamento):
    crud.criar_pagamento(venda_id, valor_pago, data_pagamento, metodo_pagamento)

def consultar_pagamentos_por_cliente(cliente_id):
    return crud.consultar_pagamentos_por_cliente(cliente_id)