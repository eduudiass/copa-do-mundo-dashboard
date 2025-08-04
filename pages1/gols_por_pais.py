import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('worldcup.csv', encoding='latin1')

df['given_name'] = df['given_name'].str.strip().replace("not applicable", "")
df['family_name'] = df['family_name'].str.strip().replace("not applicable", "")
df['jogador'] = (df['given_name'] + ' ' + df['family_name']).str.strip()

df_validos = df[(df['own_goal'] == 0) & (df['penalty'] == 0)]

gols_por_pais = df_validos['player_team_name'].value_counts().head(15)

#traduzindo os nomes dos países para português
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

gols_por_pais.rename(index=traducao_paises, inplace=True)


#conta os numeros de gols por país sem considerar gols contra e de pênalti
print("\nTop 15 Países com mais gols na Copa do Mundo:")
print(gols_por_pais)

plt.figure(figsize=(12, 6))
sns.barplot(x=gols_por_pais.index, y=gols_por_pais.values, palette='viridis')
plt.title('Top 15 Países com mais gols na Copa do Mundo')
plt.xlabel('Número de Gols')
plt.ylabel('País')
plt.tight_layout()
plt.show()