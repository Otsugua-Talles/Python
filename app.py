import streamlit as st
import random
import time

# ===== Configuração da página =====
st.set_page_config(page_title="Pergunta Divertida", page_icon="🎉", layout="centered")
st.markdown(
    "<h1 style='text-align:center; color:#333; font-family:Helvetica;'>Hoje tem *?</h1>",
    unsafe_allow_html=True
)

# ===== Estilo do botão e layout =====
col1, col2 = st.columns([1,1])

# Controle se já clicou "Sim"
if "clicou_sim" not in st.session_state:
    st.session_state.clicou_sim = False

# ===== Função para animação do "Sim" =====
def animar_sim():
    st.session_state.clicou_sim = True
    for i in range(10):
        cor = random.choice(["#00CC00", "#FFAA00", "#FF5555", "#00AAFF", "#FF00FF"])
        st.markdown(
            f"<h2 style='text-align:center; color:{cor}; font-family:Helvetica;'>Finalmente! 🎉🎊✨</h2>",
            unsafe_allow_html=True
        )
        time.sleep(0.3)

# ===== Botão "Sim" =====
if not st.session_state.clicou_sim:
    if col1.button("Sim", key="sim"):
        animar_sim()

# ===== Botão "Não" - impossível de clicar =====
# Simula o botão fugindo com posições aleatórias
if not st.session_state.clicou_sim:
    if col2.button("Não", key="nao"):
        st.warning("Resposta errada!!!")

