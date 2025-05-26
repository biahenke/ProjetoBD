import streamlit as st
from app.views.main_view import menu, interface
from app.views.main_view import exibir_views_personalizadas
from app.models import crud

def main():
    st.set_page_config(page_title="Sistema de Gestão da Academia", layout="wide")
    st.title("Sistema de Gestão da Academia")

    # Criação das tabelas principais se não existirem
    crud.criar_tabela_clientes()
    crud.criar_tabela_fornecedores()
    crud.criar_tabela_produtos()
    crud.criar_tabela_vendas()
    crud.criar_tabela_fichas_medicas()
    crud.criar_tabela_aulas()
    crud.criar_tabela_dependentes()
    crud.criar_tabela_pagamentos()



    # Menu Principal
    opcao = menu()
    interface(opcao)

    # Views Personalizadas
    st.sidebar.markdown("---")
    st.sidebar.markdown("## Opções Personalizadas")
    exibir_views_personalizadas()

if __name__ == '__main__':
    main()
