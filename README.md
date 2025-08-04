
# 🏆 Análise de Gols em Copas do Mundo

Este projeto é um **dashboard interativo** criado com **Python** e **Streamlit**, com foco na visualização de dados sobre gols em Copas do Mundo, utilizando um conjunto de dados customizado.

---

## ⚙️ Funcionalidades

- 📊 Gols por edição da Copa
- 🏆 Gols por fase da competição
- ⏱️ Gols por minuto de jogo
- 🌍 Gols por país
- 🎨 Dashboard visual, moderno e com menu lateral
- 📁 Organização com múltiplas páginas via `pages/`
- 🐍 Scripts de análise alternativos na pasta `pages1/`

---

## 📁 Estrutura do Projeto

```
📦 copa-do-mundo-dashboard
├── 📁 assets
│   └── capa_dashboard_copa.jpg
├── 📁 pages
│   ├── 1_Gols_por_edição.py
│   ├── 2_Gols_por_fase.py
│   ├── 3_Gols_por_minuto.py
│   └── 4_Gols_por_país.py
├── 📁 pages1
│   ├── analise_gols_copa.py
│   ├── artilheiros.py
│   ├── gols_por_edicao.py
│   ├── gols_por_fase.py
│   ├── gols_por_minuto.py
│   └── gols_por_pais.py
├── .gitignore
├── app.py
├── worldcup.csv
├── requirements.txt
└── README.md
```

---

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/eduudiass/copa-do-mundo-dashboard.git
   cd copa-do-mundo-dashboard
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o dashboard:
   ```bash
   streamlit run app.py
   ```

---

## 📌 Sobre os dados

Os dados foram extraídos e tratados manualmente a partir do site [Kaggle](https://www.kaggle.com/), e organizados em um arquivo CSV com as principais informações sobre gols em Copas do Mundo.

---

## 👨‍💻 Autor

Desenvolvido por [Eduardo Dias](https://github.com/eduudiass)  
Estudante de Ciência de Dados e Inteligência Artificial  
Porto Alegre - RS, Brasil

---
