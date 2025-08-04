import pandas as pd

df = pd.read_csv('worldcup.csv')

print(df.head())
print(df.info())    
print("Colunas", df.columns)

import matplotlib.pyplot as plt
import seaborn as sns

gols_por_ano = df['year'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.barplot(x=gols_por_ano.index, y=gols_por_ano.values, palette="viridis")
plt.title('Total de gols por Edição na Copa do Mundo')
plt.xlabel('Ano da Copa do Mundo')
plt.ylabel('Total de Gols')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

artilheiros = df['player'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=artilheiros.values, y=artilheiros.index, pallet='rockets')
plt.title('Top 10 Artilheiros da Copa do Mundo')
plt.xlabel('Número de Gols')
plt.ylabel('Jogador')
plt.tight_layout()
plt.show()