import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Gols por Edição de Copa do Mundo")

df = pd.read_csv("worldcup.csv", encoding="latin1")

df_validos = df[(df['own_goal'] == 0) & (df['penalty'] == 0)].copy()

df_validos['ano_copa'] = df_validos['tournament_id'].str.extract(r'WC-(\d{4})')

gols_por_edicao = df_validos['ano_copa'].value_counts().sort_index()

st.subheader("Tabela de Gols por Edição da Copa do Mundo")
st.dataframe(gols_por_edicao.reset_index().rename(columns={'index': 'Ano', 'ano_copa': 'Gols'}))

st.subheader("Gráfico de Gols por Edição da Copa do Mundo")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=gols_por_edicao.index, y=gols_por_edicao.values, palette='viridis', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_xlabel("Ano da Copa do Mundo")
ax.set_ylabel("Número de Gols")
ax.set_title("Gols por Edição de Copa do Mundo")
st.pyplot(fig)
