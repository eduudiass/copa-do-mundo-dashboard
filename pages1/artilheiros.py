import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('worldcup.csv', encoding='latin1')

df['given_name'] = df['given_name'].str.strip().replace("not applicable", "")
df['family_name'] = df['family_name'].str.strip().replace("not applicable", "")

df['jogador'] = (df['given_name'] + ' ' + df['family_name']).str.strip()

correcoes = {
    "Ronaldo": "Ronaldo Nazário",
    "Pelé": "Pelé",
    "Vavá": "Vavá",
    "Ademir": "Ademir",
    "Jairzinho": "Jairzinho",
    "Leônidas": "Leônidas",
    
    "Gerd Mï¿½Ller": "Gerd Müller",
    "Thomas Mï¿½Ller": "Thomas Müller",
    "Sï¿½Ndor Kocsis": "Sándor Kocsis",
    "Jï¿½Rgen Klinsmann": "Jürgen Klinsmann",
    "Kylian Mbappï¿½": "Kylian Mbappé",
    "Rudi Vï¿½Ller": "Rudi Völler",
    "Teï¿½Filo Cubillas": "Teófilo Cubillas",
    "Oscar Mï¿½Guez": "Óscar Míguez",
    "Guillermo Stï¿½Bile": "Guillermo Stábile",
    "Hans Schï¿½Fer": "Hans Schäfer",
}

df['jogador'] = df['jogador'].replace(correcoes)
df['jogador'] = df['jogador'].str.replace("Mï¿½ller", "Müller", regex=False)
df['jogador'] = df['jogador'].str.replace("Pelï¿½", "Pelé", regex=False)
df['jogador'] = df['jogador'].str.replace("Sï¿½ndor", "Sándor", regex=False)
df['jogador'] = df['jogador'].str.replace("Jï¿½rgen", "Jürgen", regex=False)


df_validos = df[(df['own_goal'] == 0) & (df['penalty'] == 0)]

print("\nTop 30 nomes (validação):")
print(df_validos['jogador'].value_counts().head(30))

artilheiros = df_validos['jogador'].value_counts().head(10)

print("\nTop 10 Artilheiros da Copa do Mundo:")
print(artilheiros)

plt.figure(figsize=(10, 6))
sns.barplot(x=artilheiros.values, y=artilheiros.index, palette='rocket')
plt.title('Top 10 Artilheiros da Copa do Mundo (Gols válidos)')
plt.xlabel('Número de Gols')
plt.ylabel('Jogador')
plt.tight_layout()
plt.show()

plt.savefig("top_10_artilheiros.png")
