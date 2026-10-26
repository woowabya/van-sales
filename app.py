from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="VAN대리점 세일즈 표준 스크립트", page_icon="📞", layout="wide")

# Streamlit 기본 여백·메뉴를 숨겨서 index.html이 화면을 꽉 채우게 합니다.
st.markdown(
    """
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=1000, scrolling=True)
