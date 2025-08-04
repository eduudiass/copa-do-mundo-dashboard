import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('worldcup.csv', encoding='latin1')

df['given_name'] = df['given_name'].str.strip().replace("not applicable", "")
df['family_name'] = df['family_name'].str.strip().replace("not applicable", "")
df['jogador'] = (df['given_name'] + ' ' + df['family_name']).str.strip()

df_validos = df[(df['own_goal'] == 0) & (df['penalty'] == 0)]

mapeamento_fases = {
    "group stage": "Fase de Grupos",
    "round of 16": "Oitavas de Final",
    "quarter-finals": "Quartas de Final",
    "semi-finals": "Semifinais",
    "final": "Final",
    "third-place match": "Terceiro Lugar",
    "second group stage": "Segunda Fase de Grupos",
    "final round": "Fase Final em Grupo"
}

df_validos['stage_name'] = df_validos['stage_name'].replace(mapeamento_fases)

gols_por_fase = df_validos['stage_name'].value_counts()
print("\nGols por fase da Copa do Mundo:")
print(gols_por_fase)

plt.figure(figsize=(12, 6))
sns.barplot(x=gols_por_fase.index, y=gols_por_fase.values, palette='viridis')
plt.title('Gols por Fase da Copa do Mundo')
plt.xlabel('Numero de Gols')
plt.ylabel('Fase')
plt.tight_layout()
plt.show()  


