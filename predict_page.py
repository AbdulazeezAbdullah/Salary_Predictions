import streamlit as st
import joblib
import numpy as np


# ── Model loader ──────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    try:
        with open('Random_Forest_Model.pkl', 'rb') as f:
            return joblib.load(f)
    except Exception:
        return None


def show_predict_page():
    data = load_model()

    # ── Top nav ───────────────────────────────────────────────────────────
    st.markdown("""
    <div class="topnav">
      <div class="topnav-left">
        <div class="brand">Dev<span>Salary</span>IQ</div>
        <div class="nav-links">
          <span>Dashboard</span>
          <span class="active">Predict</span>
          <span>Reports</span>
        </div>
      </div>
      <div class="topnav-right">
        <div class="notif-btn">🔔<span class="notif-dot"></span></div>
        <div class="avatar">DS</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Page hero ─────────────────────────────────────────────────────────
    st.markdown("""
    <div class="page-hero">
      <div class="hero-badge">🤖 Random Forest Model</div>
      <h1>Salary Predictor</h1>
      <p>Enter your profile details to get a personalised salary estimate.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Layout ────────────────────────────────────────────────────────────
    col_form, col_summary = st.columns([3, 2], gap="large")

    with col_form:

        # ── Section 1: Professional Info ───────────────────────────────
        st.markdown("""
        <div class="form-card">
          <div class="form-section-header">
            <div class="form-section-icon fi-blue">💼</div>
            <div>
              <div class="form-section-title">Professional Background</div>
              <div class="form-section-sub">Your employment and career details</div>
            </div>
          </div>
        """, unsafe_allow_html=True)

        mainbranch_opts = [
            'I am a developer by profession',
            'I am not primarily a developer, but I write code sometimes as part of my work'
        ]
        employment_opts = [
            'Employed full-time',
            'Independent contractor, freelancer, or self-employed',
            'Employed part-time',
            'Retired',
            'I prefer not to say'
        ]

        MainBranch = st.selectbox("Developer Category", mainbranch_opts)
        col1, col2 = st.columns(2)
        with col1:
            Employment = st.selectbox("Employment Status", employment_opts)
        with col2:
            OrgSize = st.selectbox("Organisation Size", [
                'Just me - I am a freelancer, sole proprietor, etc.',
                '2 to 9 employees', '10 to 19 employees', '20 to 99 employees',
                '100 to 499 employees', '500 to 999 employees',
                '1,000 to 4,999 employees', '5,000 to 9,999 employees',
                '10,000 or more employees', "I don't know"
            ])

        col3, col4 = st.columns(2)
        with col3:
            YearsCode = st.slider("Years Coding (Total)", min_value=0.5, max_value=50.0, value=5.0, step=0.5)
        with col4:
            YearsCodePro = st.slider("Years Coding (Professional)", min_value=0.5, max_value=50.0, value=3.0, step=0.5)

        st.markdown('</div>', unsafe_allow_html=True)

        # ── Section 2: Personal Info ────────────────────────────────────
        st.markdown("""
        <div class="form-card">
          <div class="form-section-header">
            <div class="form-section-icon fi-indigo">🎓</div>
            <div>
              <div class="form-section-title">Education & Demographics</div>
              <div class="form-section-sub">Your academic and personal profile</div>
            </div>
          </div>
        """, unsafe_allow_html=True)

        col5, col6 = st.columns(2)
        with col5:
            Education = st.selectbox("Education Level", [
                "Bachelor's degree", "Master's degree", "Post grad",
                "WAEC/NECO and it's equivalent worldwide"
            ])
            Age1stCode = st.selectbox("Age You First Coded", [
                'Younger than 5 years', '5 - 10 years', '11 - 17 years',
                '18 - 24 years', '25 - 34 years', '35 - 44 years',
                '45 - 54 years', '55 - 64 years', 'Older than 64 years'
            ])
        with col6:
            Age = st.selectbox("Current Age", [
                '18-24 years old', '25-34 years old', '35-44 years old',
                '45-54 years old', '55-64 years old',
                '65 years or older', 'Under 18 years old', 'Prefer not to say'
            ])
            Country = st.selectbox("Country", [
                'United States of America', 'United Kingdom of Great Britain and Northern Ireland',
                'Germany', 'Canada', 'India', 'France', 'Brazil', 'Australia',
                'Netherlands', 'Sweden', 'Spain', 'Switzerland', 'Poland',
                'Russian Federation', 'Turkey', 'Singapore', 'Israel', 'Ukraine',
                'Italy', 'Norway', 'Denmark', 'Austria', 'Belgium', 'Finland',
                'Czech Republic', 'Romania', 'Hungary', 'Bulgaria', 'Greece',
                'Portugal', 'Serbia', 'Croatia', 'Slovakia', 'Slovenia',
                'Lithuania', 'Ireland', 'Colombia', 'Argentina', 'Chile',
                'Mexico', 'South Africa', 'Kenya', 'Nigeria', 'Egypt',
                'Pakistan', 'Bangladesh', 'Sri Lanka', 'Nepal', 'Philippines',
                'Viet Nam', 'Indonesia', 'Malaysia', 'China', 'Taiwan', 'Japan',
                'New Zealand', 'Uruguay', 'Iran, Islamic Republic of...', 'Other'
            ])

        st.markdown('</div>', unsafe_allow_html=True)

        # ── Predict button ──────────────────────────────────────────────
        predict_btn = st.button("🔍  Predict My Salary", use_container_width=True)

    # ── Right summary panel ───────────────────────────────────────────────
    with col_summary:
        mb = "Developer" if "developer by profession" in MainBranch else "Non-dev Coder"

        st.markdown(f"""
        <div class="summary-widget">
          <div class="summary-widget-header">
            <div class="sw-title">Your Profile</div>
            <div class="sw-name">{Country} · {Age}</div>
          </div>
          <div class="summary-widget-body">
            <div class="sw-row">
              <span class="sw-key">Category</span>
              <span class="sw-val accent">{mb}</span>
            </div>
            <div class="sw-row">
              <span class="sw-key">Employment</span>
              <span class="sw-val">{Employment.split(",")[0]}</span>
            </div>
            <div class="sw-row">
              <span class="sw-key">Education</span>
              <span class="sw-val">{Education}</span>
            </div>
            <div class="sw-row">
              <span class="sw-key">Org Size</span>
              <span class="sw-val">{OrgSize.split(" employees")[0]}</span>
            </div>
            <div class="sw-row">
              <span class="sw-key">First Coded</span>
              <span class="sw-val accent">{Age1stCode}</span>
            </div>
            <div class="sw-row">
              <span class="sw-key">Total Coding Exp.</span>
              <span class="sw-val">{YearsCode:.1f} yrs</span>
            </div>
            <div class="sw-row">
              <span class="sw-key">Professional Exp.</span>
              <span class="sw-val">{YearsCodePro:.1f} yrs</span>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Result ───────────────────────────────────────────────────────
        if predict_btn:
            if data is None:
                st.error("⚠️ Model not found. Place `Random_Forest_Model.pkl` in the app directory.")
            else:
                try:
                    regressor         = data["model"]
                    MainBranch_encode = data["MainBranch_encoder"]
                    Employment_encode = data["Employment_encoder"]
                    Country_encode    = data["Country_encoder"]
                    EdLevel_encode    = data["EdLevel_encoder"]
                    Age1st_encode     = data["Age1st_encoder"]
                    OrgSize_encode    = data["OrgSize_encoder"]
                    Age_encode        = data["Age_encoder"]

                    X = np.array([[MainBranch, Employment, Country, Education,
                                   Age1stCode, YearsCode, YearsCodePro, OrgSize, Age]], dtype=object)

                    X[:, 0] = MainBranch_encode.transform(X[:, 0])
                    X[:, 1] = Employment_encode.transform(X[:, 1])
                    X[:, 2] = Country_encode.transform(X[:, 2])
                    X[:, 3] = EdLevel_encode.transform(X[:, 3])
                    X[:, 4] = Age1st_encode.transform(X[:, 4])
                    X[:, 7] = OrgSize_encode.transform(X[:, 7])
                    X[:, 8] = Age_encode.transform(X[:, 8])

                    salary = regressor.predict(X.astype(float))[0]

                    st.markdown(f"""
                    <div class="result-box primary">
                      <div class="result-label">Estimated Annual Salary</div>
                      <div class="result-value">${salary:,.0f}</div>
                      <div class="result-sub">USD · Based on {YearsCodePro:.0f} yrs professional experience in {Country}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    # Breakdown chips
                    monthly = salary / 12
                    st.markdown(f"""
                    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.8rem;margin-top:1rem;">
                      <div class="stat-card" style="margin:0;">
                        <div class="stat-label">Monthly Est.</div>
                        <div class="stat-value green" style="font-size:1.25rem;">${monthly:,.0f}</div>
                      </div>
                      <div class="stat-card" style="margin:0;">
                        <div class="stat-label">Daily Est.</div>
                        <div class="stat-value blue" style="font-size:1.25rem;">${salary/365:,.0f}</div>
                      </div>
                    </div>
                    """, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Prediction error: {e}")

    # ── Footer ────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="text-align:center;padding:2rem 0 .5rem;color:#b0bac9;font-size:.78rem;">
      DevSalaryIQ &nbsp;·&nbsp; Stack Overflow Survey 2021 &nbsp;·&nbsp;
      <span style="color:#4361ee;font-weight:700;">Powered by Random Forest</span>
    </div>
    """, unsafe_allow_html=True)
