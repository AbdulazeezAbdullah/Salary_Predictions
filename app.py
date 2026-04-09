import streamlit as st

st.set_page_config(
    page_title="DevSalaryIQ",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Inject shared CSS ─────────────────────────────────────────────────────────
from styles import SHARED_CSS
st.markdown(SHARED_CSS, unsafe_allow_html=True)

# ── Page routing via sidebar radio ────────────────────────────────────────────
with st.sidebar:
    st.markdown("### DevSalaryIQ")
    page = st.radio(
        "Navigate",
        ("📊 Explore", "🤖 Predict"),
        label_visibility="collapsed"
    )

if page == "📊 Explore":
    from explore_page import show_explore_page
    show_explore_page()
else:
    from predict_page import show_predict_page
    show_predict_page()
