import streamlit as st
import pandas as pd
import rede_social

st.title("Busca em profundidade em Grafos")

membros = st.number_input("Digite o número inteiro para quantidade de membros da rede social:",min_value=0, max_value=100000000,step=1)
relações = st.number_input("Digite o número inteiro para quantidade de relações de amizades para a rede social:",min_value=0, max_value=100000000,step=1)
dfe = pd.DataFrame({'Membros':[membros],'Relações':[relações]})
dfe.to_csv('entradas.csv')
dfs = pd.read_csv('resultados.csv')


if st.button("Calcular"):
    rede_social.main()
    st.write("Grau de separação:", dfs.iloc[0,0])
    st.write("Tempo de cálculo:", dfs.iloc[0,1])
   
    


