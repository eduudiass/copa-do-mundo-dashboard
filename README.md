# 🏆 Dashboard Interativo: Gols em Copas do Mundo

Projeto de dashboard interativo em Python com Streamlit, focado na análise visual de estatísticas de gols em Copas do Mundo.  
Permite explorar dados de forma intuitiva por meio de múltiplas páginas e gráficos dinâmicos.

---

## ⚽ Funcionalidades

### 📊 Análises Disponíveis
- Gols por edição da Copa
- Gols por fase da competição
- Gols por minuto de jogo
- Gols por país
- Artilheiros das Copas do Mundo (com correção de nomes e acentos)

### 🛠️ Recursos do App
- Dashboard visual e moderno, com menu lateral interativo
- Organização das páginas com múltiplas seções via `pages/`
- Scripts alternativos de análise salvos em `pages1/`

---

## 📁 Estrutura do Projeto

```
copa-do-mundo-dashboard/
│
├── assets/
│   └── capa_dashboard_copa.png
│
├── pages/
│   ├── 1_Gols_por_edição.py
│   ├── 2_Gols_por_fase.py
│   ├── 3_Gols_por_minuto.py
│   └── 4_Gols_por_país.py
│
├── pages1/
│   ├── analise_gols_copa.py
│   ├── artilheiros.py
│   ├── gols_por_edicao.py
│   ├── gols_por_fase.py
│   ├── gols_por_minuto.py
│   └── gols_por_pais.py
│
├── worldcup.csv
├── requirements.txt
├── app.py
├── .gitignore
└── README.md
```

---

## 💻 Como Executar

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/eduudiass/copa-do-mundo-dashboard.git
cd copa-do-mundo-dashboard
```

Crie um ambiente virtual (opcional, mas recomendado) e ative:

```bash
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Rode o dashboard:

```bash
streamlit run app.py
```

---

## 📷 Preview

![Dashboard Copa do Mundo](assets/capa_dashboard_copa.png)

---

## ✍️ Autor

**Eduardo Dias**  
Estudante de Ciências de Dados e IA (PUCRS)  
🔗 [LinkedIn](https://www.linkedin.com/in/eduardo-dias-201756190/) | [GitHub](https://github.com/eduudiass)
