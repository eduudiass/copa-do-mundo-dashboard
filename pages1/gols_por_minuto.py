import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   

df = pd.read_csv('worldcup.csv', encoding='latin1')

df['given_name'] = df['given_name'].str.strip().replace("not applicable", "")
df['family_name'] = df['family_name'].str.strip().replace("not applicable", "")     
df['jogador'] = (df['given_name'] + ' ' + df['family_name']).str.strip()

df_validos = df[(df['own_goal'] == 0) & (df['penalty'] == 0)]

df_90min = df_validos[(df_validos['minute_regulation'] >= 1) & (df_validos['minute_regulation'] <= 90)]

gols_por_minuto = df_90min['minute_regulation'].value_counts().sort_index()
print("\nMinutos com mais gols")
print(gols_por_minuto.tail)

plt.figure(figsize=(14, 6))
sns.barplot(x=gols_por_minuto.index, y=gols_por_minuto.values, palette='mako')
plt.title('Gols por Minuto na Copa do Mundo (1-90 minutos)')
plt.xlabel('Minuto')
plt.ylabel('Número de Gols')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()