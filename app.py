# ============================================
# 🐍 Snake Game by Talles Rodrigues
# Desenvolvido em Python + Streamlit
# Versão: 3.0 (com reinício e saída)
# ============================================

import streamlit as st
import random
import time

# ==== CONFIGURAÇÕES ====
LARGURA = 20
ALTURA = 20
TAMANHO = 20

# ==== ESTILO ====
st.set_page_config(page_title="Snake Game 🐍", page_icon="🐍", layout="centered")
st.markdown("""
    <style>
        .stButton>button {
            width: 100%;
            font-size: 18px;
            border-radius: 10px;
        }
        .score {
            font-size: 22px;
            text-align: center;
            color: white;
            background-color: black;
            padding: 10px;
            border-radius: 10px;
        }
        .title {
            text-align: center;
            font-size: 26px;
            color: lime;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ==== FUNÇÕES DO JOGO ====
def nova_posicao():
    return (
        random.randint(0, LARGURA - 1),
        random.randint(0, ALTURA - 1)
    )

def desenhar_jogo(cobra, comida):
    grade = [["⬛" for _ in range(LARGURA)] for _ in range(ALTURA)]
    for (x, y) in cobra:
        grade[y][x] = "🟩"
    comida_x, comida_y = comida
    grade[comida_y][comida_x] = "🍎"
    return "\n".join("".join(linha) for linha in grade)

def mover_cobra(cobra, direcao):
    x, y = cobra[-1]
    if direcao == "direita": x += 1
    elif direcao == "esquerda": x -= 1
    elif direcao == "cima": y -= 1
    elif direcao == "baixo": y += 1
    novo = (x, y)
    cobra.append(novo)
    cobra.pop(0)
    return cobra

def colisao(cobra):
    x, y = cobra[-1]
    if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
        return True
    if (x, y) in cobra[:-1]:
        return True
    return False

# ==== ESTADO INICIAL ====
if "cobra" not in st.session_state:
    st.session_state.cobra = [(5, 5)]
    st.session_state.direcao = "direita"
    st.session_state.comida = nova_posicao()
    st.session_state.pontuacao = 0
    st.session_state.jogo_ativo = False

# ==== INTERFACE ====
st.markdown('<div class="title">🐍 Snake Game by Talles Rodrigues</div>', unsafe_allow_html=True)
st.markdown(f"<div class='score'>Pontuação: {st.session_state.pontuacao}</div>", unsafe_allow_html=True)
st.text("Use os botões abaixo para controlar a cobra:")

col1, col2, col3 = st.columns(3)
with col1:
    cima = st.button("⬆️ Cima")
with col2:
    esq = st.button("⬅️ Esquerda")
    dir = st.button("➡️ Direita")
with col3:
    baixo = st.button("⬇️ Baixo")

# ==== CONTROLES ====
if cima and st.session_state.direcao != "baixo":
    st.session_state.direcao = "cima"
elif baixo and st.session_state.direcao != "cima":
    st.session_state.direcao = "baixo"
elif esq and st.session_state.direcao != "direita":
    st.session_state.direcao = "esquerda"
elif dir and st.session_state.direcao != "esquerda":
    st.session_state.direcao = "direita"

# ==== BOTÕES DE CONTROLE ====
col_a, col_b = st.columns(2)
with col_a:
    if st.button("▶️ Iniciar Jogo"):
        st.session_state.jogo_ativo = True
        st.session_state.cobra = [(5, 5)]
        st.session_state.comida = nova_posicao()
        st.session_state.pontuacao = 0
with col_b:
    if st.button("❌ Sair / Resetar"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ==== LOOP DE JOGO ====
placeholder = st.empty()

if st.session_state.jogo_ativo:
    for _ in range(200):  # limite de frames
        st.session_state.cobra = mover_cobra(st.session_state.cobra, st.session_state.direcao)

        # Verifica colisão
        if colisao(st.session_state.cobra):
            placeholder.text("💀 Fim de Jogo!\nPontuação final: " + str(st.session_state.pontuacao))
            st.session_state.jogo_ativo = False
            break

        # Comer comida
        if st.session_state.cobra[-1] == st.session_state.comida:
            st.session_state.cobra.insert(0, st.session_state.cobra[0])
            st.session_state.comida = nova_posicao()
            st.session_state.pontuacao += 10

        # Atualiza tela
        placeholder.text(desenhar_jogo(st.session_state.cobra, st.session_state.comida))
        time.sleep(0.2)
        st.experimental_rerun()

else:
    placeholder.text(desenhar_jogo(st.session_state.cobra, st.session_state.comida))
