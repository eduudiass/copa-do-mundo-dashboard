import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   
import streamlit as st

st.title("Gols por Fase de Copa do Mundo")

df = pd.read_csv("worldcup.csv", encoding="latin1")

df_validos = df[(df['own_goal'] == 0) & (df['penalty'] == 0)]

gols_por_fase = df_validos['stage_name'].value_counts()

traducao_fases = {
    'group stage': 'Fase de Grupos',
    'round of 16': 'Oitavas de Final',
    'quarter-finals': 'Quartas de Final',
    'semi-finals': 'Semi Finais',
    'third-place match': 'Disputa de 3º Lugar',
    'final': 'Final',
    'second group stage': '2ª Fase de Grupos',
    'final round': 'Fase Final'
}
gols_por_fase.index = gols_por_fase.index.map(lambda x: traducao_fases.get(x, x))

st.subheader("Tabela de Gols por Fase")
st.dataframe(gols_por_fase.reset_index().rename(columns={'index': 'Fase', 'stage_name': 'Gols'}))

st.subheader("Gráfico de Gols por Fase")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=gols_por_fase.values, y=gols_por_fase.index, palette='magma', ax=ax)
ax.set_xlabel("Número de Gols")
ax.set_ylabel("Fase")
ax.set_title("Gols por Fase de Copa do Mundo")
st.pyplot(fig)
