import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Artilheiros da Copa do Mundo")

try:
    df = pd.read_csv("worldcup.csv", encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv("worldcup.csv", encoding="latin1")

if {"given_name", "family_name"}.issubset(df.columns):
    df["player"] = (df["given_name"].fillna("") + " " + df["family_name"].fillna("")).str.strip()
elif "player_name" in df.columns:
    df["player"] = df["player_name"].astype(str)
else:
    st.error("Não encontrei colunas de nome no CSV")
    st.stop()

df["player"] = df["player"].str.replace(r"^not applicable\s*", "", regex=True)

def fix_encoding(s):
    try:
        return s.encode("latin1").decode("utf-8")
    except:
        return s
df["player"] = df["player"].map(fix_encoding)

correcoes = {
    "Ronaldo": "Ronaldo Nazário",
    "Gerd M�ller": "Gerd Müller",
    "Thomas M�ller": "Thomas Müller",
    "J�rgen Klinsmann": "Jürgen Klinsmann",
    "S�ndor Kocsis": "Sándor Kocsis",
    "Kylian Mbapp�": "Kylian Mbappé",
    "Rudi V�ller": "Rudi Völler",
    "Pel�": "Pelé"
}
df["player"] = df["player"].replace(correcoes)

df_validos = df[(df.get("own_goal", 0) == 0) & (df.get("penalty", 0) == 0)]

TOP = 10
artilheiros = df_validos["player"].value_counts().head(TOP)
df_top = artilheiros.rename_axis("Jogador").reset_index(name="Gols")

st.subheader("Tabela de Artilheiros")
st.dataframe(df_top)

st.subheader("Gráfico de Artilheiros")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df_top, x="Gols", y="Jogador", palette="rocket", ax=ax)
ax.set_xlabel("Número de Gols")
ax.set_ylabel("Jogador")
ax.set_title(f"Top {TOP} Artilheiros da Copa do Mundo (sem pênalti e contra)")
st.pyplot(fig)
