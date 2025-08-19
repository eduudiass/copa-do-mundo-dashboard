# 🏆 Análise de Gols em Copas do Mundo

Este projeto é um **dashboard interativo** criado com **Python** e **Streamlit**, com foco na visualização de estatísticas sobre gols em Copas do Mundo. O objetivo é explorar os dados de forma intuitiva através de múltiplas páginas e gráficos dinâmicos.

## ⚙️ Funcionalidades
- 📊 Gols por edição da Copa  
- 🏆 Gols por fase da competição  
- ⏱️ Gols por minuto de jogo  
- 🌍 Gols por país  
- 🎯 Artilheiros das Copas do Mundo (com correções de nomes e acentos)  
- 🎨 Dashboard visual e moderno, com menu lateral interativo  
- 📁 Organização modular com múltiplas páginas via `pages/`  
- 🐍 Scripts de análise alternativos na pasta `pages1/`  

## 📁 Estrutura do Projeto
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
├── app.py  
├── worldcup.csv  
├── requirements.txt  
├── README.md  
└── .gitignore  

## 🚀 Como Executar
Clone o repositório e entre na pasta:
```bash
git clone https://github.com/eduudiass/copa-do-mundo-dashboard.git
cd copa-do-mundo-dashboard
Crie um ambiente virtual (opcional, mas recomendado) e ative:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Instale as dependências do projeto:

bash
Copiar
Editar
pip install -r requirements.txt
Por fim, execute o dashboard:

bash
Copiar
Editar
streamlit run app.py
📌 Sobre os Dados
Os dados foram coletados e tratados manualmente, com base em diferentes fontes (incluindo o Kaggle), e organizados em um arquivo CSV (worldcup.csv) contendo as principais informações sobre gols em Copas do Mundo.

🎨 Preview

👨‍💻 Autor
Eduardo Dias
📌 Estudante de Ciências de Dados e IA (PUCRS)
🔗 LinkedIn | GitHub

yaml
Copiar
Editar

---
