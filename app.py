import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Dashboard - Copa do Mundo",
    page_icon="🏆",
    layout="centered"
)

imagem = Image.open("assets/capa_dashboard_copa.png")
st.image(imagem, use_container_width=True)

st.markdown("""
    <h1 style='text-align: center;'>Análise de Gols na Copa do Mundo</h1>
    <p style='text-align: center;'>Navegue no menu lateral para explorar diferentes análises interativas!</p>
    <hr>
""", unsafe_allow_html=True)

st.markdown("""
### 📊 Como navegar:

Use o menu lateral à esquerda para acessar as diferentes análises disponíveis:

- **Gols por edição**
- **Gols por fase**
- **Gols por minuto**
- **Gols por país**
""")

with st.expander("ℹ️ Sobre o Projeto"):
    st.markdown("""
        Este dashboard foi desenvolvido por **Eduardo Dias** como um projeto de prática em análise de dados e visualização com Streamlit.
        
        Tecnologias utilizadas:
        - Python 🐍
        - Pandas 📊
        - Seaborn 🎨
        - Streamlit 🚀

        ---
        **LinkedIn:** [Eduardo Dias](https://www.linkedin.com/in/eduardo-dias-201756190/)  
        **GitHub:** [eduardodiasds](https://github.com/eduudiass)
    """, unsafe_allow_html=True)
