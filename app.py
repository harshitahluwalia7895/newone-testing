"""
Solution 4 Finance - website served through Streamlit.

Run locally:
    pip install -r requirements.txt
    streamlit run app.py

Keep index.html in the same folder as this file.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

HTML_FILE = Path(__file__).parent / "index.html"

st.set_page_config(
    page_title="Solution 4 Finance | Home, Personal, Business & Car Loans",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own chrome and let the website fill the whole browser window.
# The page scrolls inside the iframe, so the sticky navigation keeps working.
st.markdown(
    """
    <style>
      #MainMenu, header, footer,
      [data-testid="stHeader"], [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"],
      [data-testid="stSidebar"], [data-testid="collapsedControl"] {
        display: none !important;
      }
      html, body, .stApp,
      [data-testid="stAppViewContainer"], [data-testid="stMain"], .main {
        background: #10302B;
        overflow: hidden !important;
      }
      .block-container, [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      [data-testid="stElementContainer"], .element-container { margin: 0 !important; }
      iframe {
        display: block;
        width: 100vw !important;
        height: 100vh !important;
        height: 100dvh !important;
        border: none;
      }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_html(path: Path) -> str:
    return path.read_text(encoding="utf-8")


if not HTML_FILE.exists():
    st.error(
        "index.html was not found. Put it in the same folder as app.py and redeploy."
    )
    st.stop()

# height is a fallback; the CSS above stretches the frame to the full window.
components.html(load_html(HTML_FILE), height=900, scrolling=True)
