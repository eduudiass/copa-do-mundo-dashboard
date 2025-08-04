import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Gols por País na Copa do Mundo")

df = pd.read_csv("worldcup.csv", encoding="latin1")
df_validos = df[(df['own_goal'] == 0) & (df['penalty'] == 0)].copy()

gols_por_pais = df_validos["team_name"].value_counts().head(15)

traducao_paises = {
    'Brazil': 'Brasil',
    'Argentina': 'Argentina',
    'West Germany': 'Alemanha',
    'Germany': 'Alemanha',
    'Italy': 'Itália',
    'France': 'França',
    'England': 'Inglaterra',
    'Spain': 'Espanha',
    'Netherlands': 'Países Baixos',
    'Uruguay': 'Uruguai',
    'Hungary': 'Hungria',
    'Sweden': 'Suécia',
    'Belgium': 'Bélgica',
    'Yugoslavia': 'Iugoslávia',
    'Switzerland': 'Suíça'
}
gols_por_pais.index = gols_por_pais.index.map(lambda x: traducao_paises.get(x, x))

st.subheader("Tabela de Gols por País")
st.dataframe(gols_por_pais.reset_index().rename(columns={'index': 'País', 'team_name': 'Gols'}))

st.subheader("Gráfico de Gols por País")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=gols_por_pais.values, y=gols_por_pais.index, palette='cubehelix', ax=ax)
ax.set_xlabel("Número de Gols")
ax.set_ylabel("País")
ax.set_title("Top 15 Seleções com mais Gols Copa do Mundo")
st.pyplot(fig)