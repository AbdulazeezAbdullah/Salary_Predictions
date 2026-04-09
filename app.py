import streamlit as st

st.set_page_config(
    page_title="DevSalaryIQ",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from styles import SHARED_CSS
st.markdown(SHARED_CSS, unsafe_allow_html=True)

# ── Extra nav-tab CSS ─────────────────────────────────────────────────────────
st.markdown("""
<style>
.nav-tab-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: .75rem 2rem;
    background: #ffffff;
    border-bottom: 1px solid #e8ecf5;
    border-radius: 0 0 20px 20px;
    box-shadow: 0 2px 16px rgba(90,110,200,.06);
    margin-bottom: .6rem;
}
.nav-brand {
    font-weight: 800;
    font-size: 1.15rem;
    color: #1a2035;
    letter-spacing: -.4px;
}
.nav-brand span { color: #4361ee; }
.nav-right {
    display: flex;
    align-items: center;
    gap: .8rem;
}
.nav-badge {
    background: #eef1ff;
    color: #4361ee;
    border-radius: 20px;
    padding: .3rem .9rem;
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: .4px;
}
/* ── Toggle button pair ── */
div[data-testid="stColumns"] > div:nth-child(1) [data-testid="stButton"] > button,
div[data-testid="stColumns"] > div:nth-child(2) [data-testid="stButton"] > button {
    border-radius: 12px !important;
    font-size: .88rem !important;
    padding: .55rem 1.2rem !important;
    font-weight: 700 !important;
    letter-spacing: .2px !important;
    width: 100% !important;
    transition: all .18s ease !important;
}
div[data-testid="stColumns"] > div:nth-child(1) [data-testid="stButton"] > button[kind="primary"],
div[data-testid="stColumns"] > div:nth-child(2) [data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(135deg, #4361ee 0%, #7209b7 100%) !important;
    color: #fff !important;
    border: none !important;
    box-shadow: 0 6px 18px rgba(67,97,238,.35) !important;
}
div[data-testid="stColumns"] > div:nth-child(1) [data-testid="stButton"] > button[kind="secondary"],
div[data-testid="stColumns"] > div:nth-child(2) [data-testid="stButton"] > button[kind="secondary"] {
    background: #f4f6fd !important;
    color: #5a6785 !important;
    border: 1.5px solid #e2e8f5 !important;
    box-shadow: none !important;
}
div[data-testid="stColumns"] > div:nth-child(1) [data-testid="stButton"] > button[kind="secondary"]:hover,
div[data-testid="stColumns"] > div:nth-child(2) [data-testid="stButton"] > button[kind="secondary"]:hover {
    background: #eef1ff !important;
    color: #4361ee !important;
    border-color: #c5cde8 !important;
    transform: none !important;
    box-shadow: none !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Explore"

# ── Navbar (decorative, brand + badge) ───────────────────────────────────────
st.markdown("""
<div class="nav-tab-bar">
  <div class="nav-brand">Dev<span>Salary</span>IQ</div>
  <div class="nav-right">
    <div class="nav-badge">SO Survey 2021</div>
    <div class="avatar">DS</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Functional toggle buttons (always visible, top of page) ──────────────────
c1, c2, _ = st.columns([1.4, 1.6, 9])

with c1:
    if st.button(
        "📊  Explore Data",
        type="primary" if st.session_state.page == "Explore" else "secondary",
        use_container_width=True,
    ):
        st.session_state.page = "Explore"
        st.rerun()

with c2:
    if st.button(
        "🤖  Predict Salary",
        type="primary" if st.session_state.page == "Predict" else "secondary",
        use_container_width=True,
    ):
        st.session_state.page = "Predict"
        st.rerun()

st.markdown("<div style='margin-bottom:1.2rem'></div>", unsafe_allow_html=True)

# ── Route ─────────────────────────────────────────────────────────────────────
if st.session_state.page == "Explore":
    from explore_page import show_explore_page
    show_explore_page()
else:
    from predict_page import show_predict_page
    show_predict_page()
