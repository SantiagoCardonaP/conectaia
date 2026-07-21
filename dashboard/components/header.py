import streamlit as st

def render_header():
    st.markdown("""
        <div class="main-header">
            <img src="assets/img/logo-epm.png" />
            <div class="titulo">
                <h1>ConectaIA</h1>
                <p>Impacto de los Centros Digitales Rurales</p>
                <p>Análisis del impacto educativo de los Centros Digitales Rurales en Colombia · EPM & Julius AI</p>
            </div>
            <img src="assets/img/logo-julius.png" />
        </div>
    """, unsafe_allow_html=True)