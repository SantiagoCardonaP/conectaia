import streamlit as st
import base64
from pathlib import Path
from components.header import render_header
from components.mapa import render_mapa
from components.simulador import render_simulador
from components.preguntas import render_chat_flotante
from components.footer import render_footer

st.set_page_config(
    page_title="ConectaIA — Centros Digitales Ruraless",
    page_icon="🌐",
    layout="wide"
)

def load_css():
    css_path = Path(__file__).parent / "assets" / "css" / "styles.css"
    font_path = Path(__file__).parent / "assets" / "css" / "EPMRoundedBTVF.ttf"
    css = css_path.read_text(encoding="utf-8")
    font = base64.b64encode(font_path.read_bytes()).decode()
    css = css.replace(
        "__EPM_FONT__",
        f"data:font/ttf;base64,{font}"
    )
    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )
load_css()

render_header()

tab_mapa, tab_simulador = st.tabs(["Mapa de municipios", "Simulador de impacto"])

with tab_mapa:
    render_mapa()

with tab_simulador:
    render_simulador()

render_chat_flotante()

render_footer()