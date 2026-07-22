import streamlit as st
from pathlib import Path
import base64

def img_to_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

def render_header():
    img_dir = Path(__file__).parent.parent / "assets" / "img"
    conectaia = img_to_base64(img_dir / "conectaia.svg")
    volver = img_to_base64(img_dir / "icon-volver.svg")

    st.markdown(f"""
        <div class="headerP">
            <a href="https://www.epm.com.co/" class="headerP__volver" target="_blank"><img src="data:image/svg+xml;base64,{volver}">Ir a epm.com.co</a>
            <img src="data:image/svg+xml;base64,{conectaia}" class="headerP__img">
            <h1 class="headerP__title">Impacto de los Centros Digitales Rurales</h1>
            <p>Análisis del impacto educativo de los Centros Digitales Rurales en Colombia · EPM & Julius AI</p>
        </div>
    """, unsafe_allow_html=True)