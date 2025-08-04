import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('worldcup.csv', encoding='latin1')

df['given_name'] = df['given_name'].str.strip().replace("not applicable", "")
df['family_name'] = df['family_name'].str.strip().replace("not applicable", "")
df['jogador'] = (df['given_name'] + ' ' + df['family_name']).str.strip()

df_validos = df[(df['own_goal'] == 0) & (df['penalty'] == 0)]

df_validos['ano_copa'] = df_validos['tournament_id'].str.extract(r'WC-(\d{4})')

gols_por_edicao = df_validos['ano_copa'].value_counts().sort_index()

print("\nGols por edição da Copa do Mundo:")
print(gols_por_edicao)

plt.figure(figsize=(12, 6))
sns.barplot(x=gols_por_edicao.index, y=gols_por_edicao.values, palette='magma')
plt.title('Total de Gols por Edição da Copa do Mundo')
plt.xlabel('Ano da Copa do Mundo')
plt.ylabel('Total de Gols')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

