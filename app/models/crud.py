import sqlite3

DB_PATH = "app/database/academia.db"


def conectar():
    return sqlite3.connect(DB_PATH)

def inserir_dado(tabela, dados):
    conn = conectar()
    c = conn.cursor()
    campos = ', '.join(dados.keys())
    valores = tuple(dados.values())
    placeholders = ', '.join('?' for _ in dados)
    c.execute(f"INSERT INTO {tabela} ({campos}) VALUES ({placeholders})", valores)
    conn.commit()
    conn.close()

def consultar_todos(tabela):
    conn = conectar()
    c = conn.cursor()
    c.execute(f"SELECT * FROM {tabela}")
    dados = c.fetchall()
    conn.close()
    return dados

def excluir_dado(tabela, id):
    conn = conectar()
    c = conn.cursor()
    c.execute(f"DELETE FROM {tabela} WHERE id = ?", (id,))
    conn.commit()
    conn.close()



def criar_tabela_clientes():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

def criar_tabela_fornecedores():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS fornecedores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            contato TEXT
        )
    ''')
    conn.commit()
    conn.close()

def criar_tabela_produtos():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            preco REAL,
            fornecedor_id INTEGER,
            FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
        )
    ''')
    conn.commit()
    conn.close()

def criar_tabela_vendas():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            produto_id INTEGER,
            data TEXT,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )
    ''')
    conn.commit()
    conn.close()

def criar_ficha_medica(cliente_id, altura, peso, observacoes):
    dados = {
        "cliente_id": cliente_id,
        "altura": altura,
        "peso": peso,
        "observacoes": observacoes
    }
    inserir_dado("fichas_medicas", dados)
def criar_tabela_fichas_medicas():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS fichas_medicas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            altura REAL,
            peso REAL,
            observacoes TEXT,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    ''')
    conn.commit()
    conn.close()
def consultar_ficha_medica_por_cliente(cliente_id):
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM fichas_medicas WHERE cliente_id = ?", (cliente_id,))
    ficha = c.fetchone()
    conn.close()
    return ficha

def criar_tabela_aulas():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS aulas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            horario TEXT
        )
    ''')
    conn.commit()
    conn.close()

def criar_tabela_dependentes():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS dependentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            cliente_id INTEGER,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    ''')
    conn.commit()
    conn.close()

def criar_tabela_pagamentos():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS pagamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            venda_id INTEGER,
            valor_pago REAL,
            data_pagamento TEXT,
            metodo_pagamento TEXT,
            FOREIGN KEY (venda_id) REFERENCES vendas(id)
        )
    ''')
    conn.commit()
    conn.close()
def criar_pagamento(venda_id, valor_pago, data_pagamento, metodo_pagamento):
    dados = {
        "venda_id": venda_id,
        "valor_pago": valor_pago,
        "data_pagamento": data_pagamento,
        "metodo_pagamento": metodo_pagamento
    }
    inserir_dado("pagamentos", dados)
def consultar_pagamentos_por_cliente(cliente_id):
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        SELECT p.id, p.venda_id, p.valor_pago, p.data_pagamento, p.metodo_pagamento
        FROM pagamentos p
        JOIN vendas v ON p.venda_id = v.id
        WHERE v.cliente_id = ?
    ''', (cliente_id,))
    resultados = c.fetchall()
    conn.close()
    return resultados


