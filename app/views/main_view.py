import streamlit as st
import pandas as pd
from app.controllers import (
    cliente_controller,
    fornecedor_controller,
    produto_controller,
    pagamento_controller,
    venda_controller
)

def menu():
    st.sidebar.title("Menu")
    opcao = st.sidebar.selectbox("Escolha a operação", [
        "Cadastrar Cliente", "Consultar Clientes", "Excluir Cliente",
        "Cadastrar Fornecedor", "Consultar Fornecedores", "Excluir Fornecedor",
        "Cadastrar Produto", "Consultar Produtos", "Excluir Produto",
        "Cadastrar Venda", "Consultar Vendas", "Excluir Venda"
    ])
    return opcao

def interface(opcao):
    if opcao == "Cadastrar Cliente":
        st.header("Cadastro de Cliente")
        nome = st.text_input("Nome")
        idade = st.number_input("Idade", min_value=0)
        email = st.text_input("Email")
        if st.button("Salvar"):
            cliente_controller.cadastrar_cliente(nome, idade, email)
            st.success("Cliente cadastrado com sucesso!")

    elif opcao == "Consultar Clientes":
        st.header("Consulta de Clientes")
        clientes = cliente_controller.consultar_clientes()
        if clientes:
            df = pd.DataFrame(clientes, columns=["ID", "Nome", "Idade", "Email"])
            st.dataframe(df)
        else:
            st.info("Nenhum cliente cadastrado.")

    elif opcao == "Excluir Cliente":
        st.header("Exclusão de Cliente")
        id = st.number_input("ID do Cliente", min_value=1)
        if st.button("Excluir"):
            cliente_controller.excluir_cliente(id)
            st.success("Cliente excluído com sucesso!")

    elif opcao == "Cadastrar Fornecedor":
        st.header("Cadastro de Fornecedor")
        nome = st.text_input("Nome do Fornecedor")
        contato = st.text_input("Contato")
        if st.button("Salvar"):
            fornecedor_controller.cadastrar_fornecedor(nome, contato)
            st.success("Fornecedor cadastrado com sucesso!")

    elif opcao == "Consultar Fornecedores":
        st.header("Consulta de Fornecedores")
        fornecedores = fornecedor_controller.consultar_fornecedores()
        if fornecedores:
            df = pd.DataFrame(fornecedores, columns=["ID", "Nome", "Contato"])
            st.dataframe(df)
        else:
            st.info("Nenhum fornecedor cadastrado.")

    elif opcao == "Excluir Fornecedor":
        st.header("Exclusão de Fornecedor")
        id = st.number_input("ID do Fornecedor", min_value=1)
        if st.button("Excluir"):
            fornecedor_controller.excluir_fornecedor(id)
            st.success("Fornecedor excluído com sucesso!")

    elif opcao == "Cadastrar Produto":
        st.header("Cadastro de Produto")
        nome = st.text_input("Nome do Produto")
        preco = st.number_input("Preço", min_value=0.0)
        fornecedor_id = st.number_input("ID do Fornecedor", min_value=1)
        if st.button("Salvar"):
            produto_controller.cadastrar_produto(nome, preco, fornecedor_id)
            st.success("Produto cadastrado com sucesso!")

    elif opcao == "Consultar Produtos":
        st.header("Consulta de Produtos")
        produtos = produto_controller.consultar_produtos()
        if produtos:
            df = pd.DataFrame(produtos, columns=["ID", "Nome", "Preço", "Fornecedor_ID"])
            st.dataframe(df)
        else:
            st.info("Nenhum produto cadastrado.")

    elif opcao == "Excluir Produto":
        st.header("Exclusão de Produto")
        id = st.number_input("ID do Produto", min_value=1)
        if st.button("Excluir"):
            produto_controller.excluir_produto(id)
            st.success("Produto excluído com sucesso!")

    elif opcao == "Cadastrar Venda":
        st.header("Cadastro de Venda")
        cliente_id = st.number_input("ID do Cliente", min_value=1)
        produto_id = st.number_input("ID do Produto", min_value=1)
        data = st.date_input("Data da Venda")
        if st.button("Salvar"):
            venda_controller.cadastrar_venda(cliente_id, produto_id, str(data))
            st.success("Venda cadastrada com sucesso!")

    elif opcao == "Consultar Vendas":
        st.header("Consulta de Vendas")
        vendas = venda_controller.consultar_vendas()
        if vendas:
            df = pd.DataFrame(vendas, columns=["ID", "Cliente_ID", "Produto_ID", "Data"])
            st.dataframe(df)
        else:
            st.info("Nenhuma venda registrada.")

    elif opcao == "Excluir Venda":
        st.header("Exclusão de Venda")
        id = st.number_input("ID da Venda", min_value=1)
        if st.button("Excluir"):
            venda_controller.excluir_venda(id)
            st.success("Venda excluída com sucesso!")

def exibir_views_personalizadas():
    st.sidebar.markdown("## Opções Personalizadas")
    opcao = st.sidebar.selectbox("Escolha uma opção:", [
        "Pagamentos", "Relatório de Vendas"
    ])

    if opcao == "Pagamentos":
        acao = st.sidebar.radio("O que deseja fazer?", [
            "Registrar Pagamento", "Consultar Pagamentos"
        ])
        if acao == "Registrar Pagamento":
            pagamento_view()
        elif acao == "Consultar Pagamentos":
            consultar_pagamentos_view()

    elif opcao == "Relatório de Vendas":
        relatorio_vendas_view()

def pagamento_view():
    st.header("Registro de Pagamento")
    venda_id = st.number_input("ID da Venda", min_value=1)
    valor_pago = st.number_input("Valor Pago", min_value=0.0)
    data_pagamento = st.date_input("Data do Pagamento")
    metodo_pagamento = st.selectbox("Método de Pagamento", ["Dinheiro", "Cartão", "Pix"])
    if st.button("Registrar"):
        pagamento_controller.registrar_pagamento(venda_id, valor_pago, str(data_pagamento), metodo_pagamento)
        st.success("Pagamento registrado com sucesso!")

def consultar_pagamentos_view():
    st.header("Consulta de Pagamentos")
    clientes = cliente_controller.consultar_clientes()
    if not clientes:
        st.info("Nenhum cliente cadastrado.")
        return

    cliente_dict = {f"{c[1]} (ID {c[0]})": c[0] for c in clientes}
    escolha = st.selectbox("Selecione um cliente:", list(cliente_dict.keys()))
    cliente_id = cliente_dict[escolha]

    pagamentos = pagamento_controller.consultar_pagamentos_por_cliente(cliente_id)
    if pagamentos:
        df = pd.DataFrame(pagamentos, columns=["Pagamento_ID", "Venda_ID", "Valor Pago", "Data", "Método"])
        st.dataframe(df)
    else:
        st.warning("Nenhum pagamento registrado para este cliente.")

def relatorio_vendas_view():
    st.header("Relatório de Vendas")
    data_inicial = st.date_input("Data inicial")
    data_final = st.date_input("Data final")

    if st.button("Gerar Relatório"):
        vendas = venda_controller.consultar_vendas_por_periodo(str(data_inicial), str(data_final))
        if vendas:
            import pandas as pd
            df = pd.DataFrame(vendas, columns=["ID", "Cliente_ID", "Produto_ID", "Data"])
            st.dataframe(df)
        else:
            st.info("Nenhuma venda encontrada no período.")
