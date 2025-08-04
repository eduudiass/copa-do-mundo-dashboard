import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Gols por Minuto da Copa do Mundo")

df = pd.read_csv("worldcup.csv", encoding="latin1")
df_validos = df[(df['own_goal'] == 0) & (df['penalty'] == 0)]

df_90min = df_validos[(df_validos['minute_regulation'] >= 1) & (df_validos['minute_regulation'] <= 90)]
gols_por_minuto = df_90min['minute_regulation'].value_counts().sort_index()

st.subheader("Tabela de Gols por Minuto")
st.dataframe(gols_por_minuto.reset_index().rename(columns={'index': 'Minuto', 'minute_regulation': 'Gols'}))

st.subheader("Gráfico de Gols por Minuto (1 a 90)")

fig, ax = plt.subplots(figsize=(14, 6))

# Gráfico
sns.barplot(x=gols_por_minuto.index, y=gols_por_minuto.values, palette='plasma', ax=ax)

ax.set_xlabel("Minuto")
ax.set_ylabel("Número de Gols")
ax.set_title("Distribuição de Gols por Minuto (Tempo Normal)")

ax.set_xticks(range(0, 91, 10)) 
ax.set_xticklabels(range(0, 91, 10), rotation=45)

st.pyplot(fig)
