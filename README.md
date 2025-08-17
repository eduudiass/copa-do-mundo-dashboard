
🏆 Análise de Gols em Copas do Mundo

Este projeto é um dashboard interativo criado com Python e Streamlit, focado na visualização de estatísticas sobre gols em Copas do Mundo.
Os dados foram organizados em um conjunto customizado e explorados em múltiplas páginas com análises detalhadas.

⚙️ Funcionalidades

📊 Gols por edição da Copa

🏆 Gols por fase da competição

⏱️ Gols por minuto de jogo

🌍 Gols por país

🎯 Artilheiros das Copas do Mundo (com correções de nomes e acentos)

🎨 Dashboard visual, moderno e com menu lateral

📁 Organização modular com múltiplas páginas via pages/

🐍 Scripts de análise alternativos na pasta pages1/

📁 Estrutura do Projeto
📦 copa-do-mundo-dashboard
├── 📁 assets
│   └── capa_dashboard_copa.png
├── 📁 pages
│   ├── 1_Gols_por_edição.py
│   ├── 2_Gols_por_fase.py
│   ├── 3_Gols_por_minuto.py
│   ├── 4_Gols_por_país.py
│   └── 5_Artilheiros.py
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

🚀 Como executar

Clone o repositório:

git clone https://github.com/eduudiass/copa-do-mundo-dashboard.git
cd copa-do-mundo-dashboard


Instale as dependências:

pip install -r requirements.txt


Execute o dashboard:

streamlit run app.py

📌 Sobre os dados

Os dados foram coletados e tratados manualmente, com base em diferentes fontes (incluindo o Kaggle), e organizados em um arquivo CSV (worldcup.csv) contendo as principais informações sobre gols em Copas do Mundo.

👨‍💻 Autor

Eduardo Dias
📌 Estudante de Ciências de Dados e IA (PUCRS)
🔗 LinkedIn | GitHub

Desenvolvido por [Eduardo Dias](https://github.com/eduudiass)  
Estudante de Ciência de Dados e Inteligência Artificial  
Porto Alegre - RS, Brasil

---
