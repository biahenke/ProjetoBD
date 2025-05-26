import streamlit as st
import pandas as pd
from app.controllers import (
    cliente_controller,
    fornecedor_controller,
    produto_controller,
    venda_controller, pagamento_controller, aula_controller,dependente_controller

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
    # CLIENTE
    if opcao == "Cadastrar Cliente":
        st.header("Cadastro de Cliente")
        id = st.text_input("ID")
        nome = st.text_input("Nome")
        idade = st.number_input("Idade", min_value=0)
        email = st.text_input("Email")
        if st.button("Salvar"):
            cliente_controller.cadastrar_cliente(id,nome, idade, email)
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
        id = st.number_input("ID", min_value=1)
        if st.button("Excluir"):
            cliente_controller.excluir_cliente(id)
            st.success("Cliente excluído com sucesso!")

    # FORNECEDOR
    elif opcao == "Cadastrar Fornecedor":
        st.header("Cadastro de Fornecedor")
        id = st.text_input("ID")
        nome = st.text_input("Nome")
        contato = st.text_input("Contato")
        if st.button("Salvar"):
            fornecedor_controller.cadastrar_fornecedor(id,nome, contato)
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
        id = st.number_input("ID", min_value=1)
        if st.button("Excluir"):
            fornecedor_controller.excluir_fornecedor(id)
            st.success("Fornecedor excluído com sucesso!")

    # PRODUTO
    elif opcao == "Cadastrar Produto":
        st.header("Cadastro de Produto")
        nome = st.text_input("Nome")
        preco = st.number_input("Preço", min_value=0.0)

        fornecedores = fornecedor_controller.consultar_fornecedores()
        if not fornecedores:
            st.warning("Nenhum fornecedor cadastrado.")
            return

        fornecedores_dict = {f"{f[0]} - {f[1]}": f[0] for f in fornecedores}
        fornecedor_id = st.selectbox("Fornecedor", list(fornecedores_dict.keys()))

        if st.button("Salvar"):
            produto_controller.cadastrar_produto(nome, preco, fornecedores_dict[fornecedor_id])
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
        id = st.number_input("ID", min_value=1)
        if st.button("Excluir"):
            produto_controller.excluir_produto(id)
            st.success("Produto excluído com sucesso!")

    # VENDA
    elif opcao == "Cadastrar Venda":
        st.header("Cadastro de Venda")
        clientes = cliente_controller.consultar_clientes()
        produtos = produto_controller.consultar_produtos()

        if not clientes or not produtos:
            st.warning("É necessário ter ao menos um cliente e um produto cadastrados.")
            return

        clientes_dict = {f"{c[0]} - {c[1]}": c[0] for c in clientes}
        produtos_dict = {f"{p[0]} - {p[1]}": p[0] for p in produtos}

        cliente_id = st.selectbox("Cliente", list(clientes_dict.keys()))
        produto_id = st.selectbox("Produto", list(produtos_dict.keys()))
        data = st.date_input("Data da Venda")

        if st.button("Salvar"):
            venda_controller.cadastrar_venda(
                clientes_dict[cliente_id],
                produtos_dict[produto_id],
                str(data)
            )
            st.success("Venda registrada com sucesso!")

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
        id = st.number_input("ID", min_value=1)
        if st.button("Excluir"):
            venda_controller.excluir_venda(id)
            st.success("Venda excluída com sucesso!")

from app.controllers import ficha_medica_controller, cliente_controller

def ficha_medica_view():
    st.header("Cadastro de Ficha Médica")
    cliente_id = st.number_input("ID do Cliente", min_value=1)
    altura = st.number_input("Altura (m)", format="%.2f")
    peso = st.number_input("Peso (kg)", format="%.2f")
    observacoes = st.text_area("Observações")
    if st.button("Salvar Ficha Médica"):
        ficha_medica_controller.cadastrar_ficha_medica(cliente_id, altura, peso, observacoes)
        st.success("Ficha médica salva com sucesso!")
def consultar_ficha_medica_view():
    st.header("Consulta de Ficha Médica")
    clientes = cliente_controller.consultar_clientes()
    if not clientes:
        st.info("Nenhum cliente cadastrado.")
        return

    cliente_dict = {f"{c[1]} (ID {c[0]})": c[0] for c in clientes}
    escolha = st.selectbox("Selecione um cliente:", list(cliente_dict.keys()))
    cliente_id = cliente_dict[escolha]

    ficha = ficha_medica_controller.consultar_ficha_medica_por_cliente(cliente_id)
    if ficha:
        import pandas as pd
        df = pd.DataFrame([ficha], columns=["ID", "Cliente_ID", "Altura (m)", "Peso (kg)", "Observações"])
        st.dataframe(df)
    else:
        st.warning("Este cliente ainda não possui ficha médica cadastrada.")


def aula_view():
    st.header("Cadastro de Aulas")
    nome = st.text_input("Nome da Aula")
    horario = st.text_input("Horário")
    if st.button("Salvar Aula"):
        aula_controller.cadastrar_aula(nome, horario)
        st.success("Aula cadastrada com sucesso!")
def consultar_aulas_view():
    st.header("Consulta de Aulas")
    aulas = aula_controller.consultar_aulas()
    if aulas:
        df = pd.DataFrame(aulas, columns=["ID", "Nome da Aula", "Horário"])
        st.dataframe(df)
    else:
        st.info("Nenhuma aula cadastrada.")


def cadastrar_dependente_view():
    st.header("Cadastro de Dependente")
    nome = st.text_input("Nome do Dependente", key="nome_dependente")
    idade = st.number_input("Idade", min_value=0, key="idade_dependente")

    clientes = cliente_controller.consultar_clientes()
    if not clientes:
        st.warning("Cadastre um cliente primeiro.")
        return

    cliente_dict = {f"{c[0]} - {c[1]}": c[0] for c in clientes}
    cliente_id = st.selectbox("Cliente Responsável", list(cliente_dict.keys()), key="cliente_responsavel_dependente")

    if st.button("Salvar Dependente", key="salvar_dependente_btn"):
        dependente_controller.cadastrar_dependente(nome, idade, cliente_dict[cliente_id])
        st.success("Dependente cadastrado com sucesso!")
def consultar_dependentes_view():
    st.header("Consulta de Dependentes")
    dependentes = dependente_controller.consultar_dependentes()
    if dependentes:
        import pandas as pd
        df = pd.DataFrame(dependentes, columns=["ID", "Nome", "Idade", "Cliente_ID"])
        st.dataframe(df)
    else:
        st.info("Nenhum dependente cadastrado.")



def pagamento_view():
    st.header("Cadastro de Pagamento")
    venda_id = st.number_input("ID da Venda", min_value=1)
    valor_pago = st.number_input("Valor Pago", format="%.2f")
    data_pagamento = st.date_input("Data do Pagamento")
    metodo = st.selectbox("Método de Pagamento", ["Dinheiro", "Cartão", "Pix", "Boleto"])

    if st.button("Salvar Pagamento"):
        pagamento_controller.registrar_pagamento(
            venda_id,
            valor_pago,
            data_pagamento.strftime("%Y-%m-%d"),
            metodo
        )
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
        import pandas as pd
        df = pd.DataFrame(pagamentos, columns=[
            "Pagamento_ID", "Venda_ID", "Valor Pago", "Data", "Método"
        ])
        st.dataframe(df)
    else:
        st.warning("Nenhum pagamento registrado para este cliente.")
      

def exibir_views_personalizadas():
    opcao = st.sidebar.selectbox("Escolha uma opção:", [
        "Ficha Médica",
        "Aulas",
        "Dependentes",
        "Pagamentos"
    ])

    if opcao == "Ficha Médica":
        acao = st.sidebar.radio("O que deseja fazer?", [
            "Cadastrar Ficha Médica", "Consultar Ficha Médica"
        ])
        if acao == "Cadastrar Ficha Médica":
            ficha_medica_view()
        elif acao == "Consultar Ficha Médica":
            consultar_ficha_medica_view()

    elif opcao == "Aulas":
        acao = st.sidebar.radio("O que deseja fazer?", [
            "Cadastrar Aula", "Consultar Aulas"
        ])
        if acao == "Cadastrar Aula":
            aula_view()
        elif acao == "Consultar Aulas":
            consultar_aulas_view()

    elif opcao == "Dependentes":
        acao = st.sidebar.radio("O que deseja fazer?", [
            "Cadastrar Dependente", "Consultar Dependentes"
        ])
        if acao == "Cadastrar Dependente":
            cadastrar_dependente_view()
        elif acao == "Consultar Dependentes":
            consultar_dependentes_view()

    elif opcao == "Pagamentos":
        acao = st.sidebar.radio("O que deseja fazer?", [
            "Registrar Pagamento", "Consultar Pagamentos"
        ])
        if acao == "Registrar Pagamento":
            pagamento_view()
        elif acao == "Consultar Pagamentos":
            consultar_pagamentos_view()
