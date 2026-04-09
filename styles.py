SHARED_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; }

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background: #eef1f8;
    color: #1a2035;
}

[data-testid="stAppViewContainer"] {
    background: #eef1f8;
    min-height: 100vh;
}

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }
[data-testid="collapsedControl"] { display: none; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #eef1f8; }
::-webkit-scrollbar-thumb { background: #c5cde8; border-radius: 10px; }

/* ── Top nav ── */
.topnav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: .9rem 2rem;
    background: #ffffff;
    border-bottom: 1px solid #e8ecf5;
    border-radius: 0 0 20px 20px;
    box-shadow: 0 2px 16px rgba(90,110,200,.06);
    margin-bottom: 1.8rem;
}
.topnav-left {
    display: flex;
    align-items: center;
    gap: 2rem;
}
.brand {
    font-weight: 800;
    font-size: 1.15rem;
    color: #1a2035;
    letter-spacing: -.4px;
}
.brand span { color: #4361ee; }
.nav-links {
    display: flex;
    gap: 1.8rem;
    font-size: .88rem;
    font-weight: 500;
    color: #8896b3;
}
.nav-links .active {
    color: #1a2035;
    font-weight: 700;
    border-bottom: 2px solid #4361ee;
    padding-bottom: 2px;
}
.topnav-right {
    display: flex;
    align-items: center;
    gap: 1rem;
}
.notif-btn {
    width: 36px; height: 36px;
    border-radius: 10px;
    background: #f4f6fd;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem;
    cursor: pointer;
    position: relative;
}
.notif-dot {
    width: 8px; height: 8px;
    background: #f72585;
    border-radius: 50%;
    position: absolute;
    top: 5px; right: 5px;
    border: 1.5px solid #fff;
}
.avatar {
    width: 36px; height: 36px;
    border-radius: 50%;
    background: linear-gradient(135deg, #4361ee, #7209b7);
    display: flex; align-items: center; justify-content: center;
    color: #fff;
    font-weight: 700;
    font-size: .85rem;
}

/* ── Sidebar panel (left column) ── */
.sidebar-panel {
    background: #ffffff;
    border-radius: 20px;
    padding: 1.5rem;
    border: 1px solid #e8ecf5;
    box-shadow: 0 4px 24px rgba(90,110,200,.06);
    height: fit-content;
}
.sidebar-search {
    display: flex;
    align-items: center;
    gap: .6rem;
    background: #f4f6fd;
    border-radius: 12px;
    padding: .65rem 1rem;
    margin-bottom: 1.5rem;
    color: #8896b3;
    font-size: .85rem;
}
.sidebar-section-title {
    font-size: .7rem;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #8896b3;
    margin-bottom: .9rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.sidebar-section-title a {
    color: #4361ee;
    font-size: .72rem;
    font-weight: 600;
    letter-spacing: 0;
    text-decoration: none;
    text-transform: none;
}

/* ── Stat cards ── */
.stat-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.2rem;
    margin-bottom: 1.8rem;
}
.stat-card {
    background: #ffffff;
    border-radius: 18px;
    padding: 1.4rem 1.6rem;
    border: 1px solid #e8ecf5;
    box-shadow: 0 4px 20px rgba(90,110,200,.05);
}
.stat-label {
    font-size: .72rem;
    color: #8896b3;
    font-weight: 500;
    letter-spacing: .3px;
    margin-bottom: .4rem;
}
.stat-value {
    font-size: 1.7rem;
    font-weight: 800;
    letter-spacing: -1px;
    line-height: 1;
}
.stat-value.blue  { color: #4361ee; }
.stat-value.green { color: #06d6a0; }
.stat-value.red   { color: #ef233c; }
.stat-delta {
    font-size: .75rem;
    color: #8896b3;
    margin-top: .4rem;
    font-weight: 500;
}

/* ── Content card ── */
.content-card {
    background: #ffffff;
    border-radius: 20px;
    padding: 1.6rem 1.8rem;
    border: 1px solid #e8ecf5;
    box-shadow: 0 4px 24px rgba(90,110,200,.05);
    margin-bottom: 1.4rem;
}
.card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1.4rem;
}
.card-title {
    font-size: 1rem;
    font-weight: 700;
    color: #1a2035;
    letter-spacing: -.3px;
}
.card-title span { color: #4361ee; }
.period-tabs {
    display: flex;
    gap: .4rem;
}
.period-tab {
    padding: .3rem .75rem;
    border-radius: 8px;
    font-size: .75rem;
    font-weight: 600;
    color: #8896b3;
    cursor: pointer;
}
.period-tab.active {
    background: #4361ee;
    color: #fff;
}

/* ── Form section card ── */
.form-card {
    background: #ffffff;
    border-radius: 20px;
    padding: 1.6rem 1.8rem;
    border: 1px solid #e8ecf5;
    box-shadow: 0 4px 20px rgba(90,110,200,.05);
    margin-bottom: 1.2rem;
}
.form-section-header {
    display: flex;
    align-items: center;
    gap: .75rem;
    margin-bottom: 1.3rem;
    padding-bottom: .9rem;
    border-bottom: 1px solid #f0f3fb;
}
.form-section-icon {
    width: 36px; height: 36px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.05rem;
    flex-shrink: 0;
}
.fi-blue   { background: #eef1ff; }
.fi-indigo { background: #f0eeff; }
.fi-teal   { background: #e6fdf6; }
.form-section-title {
    font-size: .92rem;
    font-weight: 700;
    color: #1a2035;
}
.form-section-sub {
    font-size: .72rem;
    color: #8896b3;
    margin-top: .1rem;
}

/* ── Streamlit label override ── */
[data-testid="stSelectbox"] label,
[data-testid="stSlider"] label {
    font-weight: 600 !important;
    font-size: .78rem !important;
    color: #5a6785 !important;
    letter-spacing: .3px !important;
    text-transform: uppercase !important;
}

/* ── Select boxes ── */
[data-baseweb="select"] > div {
    border-radius: 11px !important;
    border: 1.5px solid #e2e8f5 !important;
    background: #f8faff !important;
    color: #1a2035 !important;
}
[data-baseweb="select"] span,
[data-baseweb="select"] > div > div,
[data-baseweb="select"] input {
    color: #1a2035 !important;
    font-weight: 600 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: .88rem !important;
}

/* ── Dropdown menu ── */
[data-baseweb="popover"],
[data-baseweb="popover"] > div,
[data-baseweb="menu"],
ul[role="listbox"] {
    background: #ffffff !important;
    border: 1.5px solid #e2e8f5 !important;
    border-radius: 14px !important;
    box-shadow: 0 12px 40px rgba(67,97,238,.12) !important;
}
[data-baseweb="popover"] li,
[data-baseweb="menu"] li,
[role="option"] {
    background: #ffffff !important;
    color: #1a2035 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: .86rem !important;
    font-weight: 500 !important;
}
[role="option"]:hover {
    background: #eef1ff !important;
    color: #4361ee !important;
}
[aria-selected="true"] {
    background: #eef1ff !important;
    color: #4361ee !important;
    font-weight: 700 !important;
}

/* ── Sliders ── */
[data-testid="stSlider"] > div > div > div > div {
    background: #4361ee !important;
}
[data-testid="stSlider"] [data-baseweb="slider"] > div:first-child {
    background: #e2e8f5 !important;
}

/* ── Button ── */
[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #4361ee 0%, #7209b7 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: .9rem 2rem !important;
    font-size: .95rem !important;
    font-weight: 700 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    width: 100% !important;
    letter-spacing: .3px !important;
    box-shadow: 0 8px 24px rgba(67,97,238,.3) !important;
    transition: all .2s ease !important;
}
[data-testid="stButton"] > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 14px 36px rgba(67,97,238,.45) !important;
}

/* ── Tab styling ── */
[data-testid="stTabs"] [data-baseweb="tab-list"] {
    background: transparent !important;
    gap: .5rem !important;
    border-bottom: 2px solid #e8ecf5 !important;
    padding-bottom: 0 !important;
}
[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent !important;
    color: #8896b3 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: .88rem !important;
    border-radius: 0 !important;
    padding: .6rem 1.2rem !important;
    border: none !important;
}
[data-testid="stTabs"] [aria-selected="true"] {
    color: #1a2035 !important;
    border-bottom: 2px solid #4361ee !important;
    margin-bottom: -2px !important;
}
[data-testid="stTabs"] [data-baseweb="tab-highlight"] {
    background: #4361ee !important;
    height: 2px !important;
}

/* ── Result box ── */
.result-box {
    border-radius: 18px;
    padding: 2rem;
    text-align: center;
    margin-top: 1rem;
}
.result-box.success {
    background: linear-gradient(135deg, #06d6a0 0%, #0cb37a 100%);
    box-shadow: 0 10px 36px rgba(6,214,160,.25);
}
.result-box.primary {
    background: linear-gradient(135deg, #4361ee 0%, #7209b7 100%);
    box-shadow: 0 10px 36px rgba(67,97,238,.3);
}
.result-label {
    font-size: .68rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: rgba(255,255,255,.7);
    margin-bottom: .5rem;
    font-weight: 700;
}
.result-value {
    font-size: 2.4rem;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -1px;
    font-family: 'Fira Code', monospace;
}
.result-sub {
    font-size: .8rem;
    color: rgba(255,255,255,.65);
    margin-top: .5rem;
}

/* ── Summary panel ── */
.summary-widget {
    background: #ffffff;
    border-radius: 20px;
    border: 1px solid #e8ecf5;
    box-shadow: 0 4px 24px rgba(90,110,200,.06);
    overflow: hidden;
}
.summary-widget-header {
    background: linear-gradient(135deg, #4361ee 0%, #7209b7 100%);
    padding: 1.4rem 1.6rem;
    color: #fff;
}
.summary-widget-header .sw-title {
    font-size: .68rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    opacity: .8;
    margin-bottom: .3rem;
}
.summary-widget-header .sw-name {
    font-size: 1.1rem;
    font-weight: 800;
    letter-spacing: -.3px;
}
.summary-widget-body { padding: 1.2rem 1.6rem; }
.sw-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: .5rem 0;
    border-bottom: 1px solid #f0f3fb;
    font-size: .82rem;
}
.sw-row:last-of-type { border: none; }
.sw-key { color: #8896b3; font-weight: 500; }
.sw-val { color: #1a2035; font-weight: 700; font-size: .8rem; }
.sw-val.accent { color: #4361ee; }

/* ── Matplotlib chart override ── */
[data-testid="stPyplotChartElement"] {
    border-radius: 14px;
    overflow: hidden;
}

/* ── Page hero ── */
.page-hero { margin-bottom: 1.8rem; }
.page-hero h1 {
    font-size: 1.7rem;
    font-weight: 800;
    color: #1a2035;
    letter-spacing: -.6px;
}
.page-hero p { color: #8896b3; font-size: .9rem; margin-top: .3rem; }
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: .4rem;
    background: #eef1ff;
    color: #4361ee;
    border-radius: 20px;
    padding: .3rem .9rem;
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: .5px;
    text-transform: uppercase;
    margin-bottom: .7rem;
}
</style>
"""
