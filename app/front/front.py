from utils.utils import tabela_Frequencia_Decadas
import streamlit as st
import pandas as pd
from pprint import pprint

def interface():
    st.title('ANÁLISE DE NOMES - IBGE')
    st.write('FONTE -> (https://servicodados.ibge.gov.br/api/v1/localidades/estados)')

    nome = st.text_input('Consulte um nome: ')

    if not nome:
        st.stop()

    dict_decadas = tabela_Frequencia_Decadas(nome)

    if not dict_decadas:
        st.write('Nome não encontrado')
        st.stop()

    df = pd.DataFrame.from_dict(dict_decadas,orient='index')

    st.line_chart(df)

    return nome

if __name__ == '__main__':
    pass