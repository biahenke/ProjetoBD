import streamlit as st
from app.views.main_view import menu, interface, exibir_views_personalizadas
from app.models import crud

def main():
    st.set_page_config(page_title="Gestão de Vendas - Academia", layout="wide")
    st.title("Sistema de Gestão de Vendas de Equipamentos")

    crud.criar_tabela_clientes()
    crud.criar_tabela_fornecedores()
    crud.criar_tabela_produtos()
    crud.criar_tabela_vendas()
    crud.criar_tabela_pagamentos()

    opcao = menu()
    interface(opcao)


    exibir_views_personalizadas()

if __name__ == "__main__":
    main()
