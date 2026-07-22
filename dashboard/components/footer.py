import streamlit as st
from pathlib import Path
import base64

def img_to_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

def render_footer():
    img_dir = Path(__file__).parent.parent / "assets" / "img"
    logo_footer = img_to_base64(img_dir / "logos-footer.svg")

    st.markdown(f"""
        <div class="footerP">
            <img src="data:image/svg+xml;base64,{logo_footer}" class="footerP__img">
        </div>
    """, unsafe_allow_html=True)