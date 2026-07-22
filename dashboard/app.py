import os
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

def to_base64(path):
    return base64.b64encode(path.read_bytes()).decode()

def load_css():
    assets = Path(__file__).parent / "assets"
    css_path = assets / "css" / "styles.css"
    css = css_path.read_text(encoding="utf-8")
    recursos = {
        "__FONT_EPM__": ("css/EPMRoundedBTVF.ttf", "font/ttf"),
        "__ICON_VOLVER__": ("img/icon-volver.svg", "image/svg+xml"),
        "__ICON_PREGUNTAS__": ("img/icon-preguntas.svg", "image/svg+xml"),
        "__ICON_MAPA__": ("img/icon-mapa.svg", "image/svg+xml"),
        "__ICON_SIMULADOR__": ("img/icon-simulador.svg", "image/svg+xml"),
        "__ICON_SELECT__": ("img/icon-select.svg", "image/svg+xml"),
        "__ICON_PAPELERA__": ("img/icon-papalera.svg", "image/svg+xml")
    }

    for variable, (archivo, mime) in recursos.items():
        ruta = assets / archivo
        contenido = to_base64(ruta)
        css = css.replace(
            variable,
            f"data:{mime};base64,{contenido}"
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