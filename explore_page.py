import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


# ── Data helpers ──────────────────────────────────────────────────────────────
def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def convert_to_number(x):
    if x == 'More than 50 years':
        return 50
    elif x == 'Less than 1 year':
        return 0.5
    else:
        return float(x)


def education_group(x):
    if "Bachelor" in x:
        return "Bachelor's degree"
    elif "Master" in x:
        return "Master's degree"
    elif ("Professional degree" in x) or ("Other doctoral" in x):
        return "Post grad"
    else:
        return "WAEC/NECO and it's equivalent worldwide"


@st.cache_data
def load_data():
    file = pd.read_csv('survey_results_public.csv')
    loaded_data = file[['Country', 'EdLevel', 'YearsCodePro', 'Employment', 'ConvertedCompYearly']]
    loaded_data = loaded_data.rename({'ConvertedCompYearly': 'Salary'}, axis=1)
    loaded_data = loaded_data[loaded_data.Salary.notnull()]
    loaded_data = loaded_data.dropna()
    country_map = shorten_categories(loaded_data.Country.value_counts(), 100)
    loaded_data.Country = loaded_data.Country.map(country_map)
    loaded_data = loaded_data[loaded_data.Salary <= 250000]
    loaded_data.YearsCodePro = loaded_data.YearsCodePro.apply(convert_to_number)
    loaded_data.EdLevel = loaded_data.EdLevel.apply(education_group)
    return loaded_data


# ── Chart helpers ─────────────────────────────────────────────────────────────
BLUE   = "#4361ee"
INDIGO = "#7209b7"
TEAL   = "#06d6a0"
RED    = "#ef233c"
AMBER  = "#fb8500"
GREY   = "#e8ecf5"

def style_fig(fig, ax):
    """Apply clean dashboard styling to a matplotlib figure."""
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#e8ecf5')
    ax.spines['bottom'].set_color('#e8ecf5')
    ax.tick_params(colors='#8896b3', labelsize=9)
    ax.yaxis.label.set_color('#8896b3')
    ax.xaxis.label.set_color('#8896b3')
    fig.tight_layout()
    return fig, ax


def show_explore_page():
    import_data = load_data()

    # ── Top nav ───────────────────────────────────────────────────────────
    st.markdown("""
    <div class="topnav">
      <div class="topnav-left">
        <div class="brand">Dev<span>Salary</span>IQ</div>
        <div class="nav-links">
          <span class="active">Dashboard</span>
          <span>Predict</span>
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
      <div class="hero-badge">📊 Stack Overflow Survey 2021</div>
      <h1>Explore Developer Salaries</h1>
      <p>Global salary trends, education impact, and experience data from 80,000+ developers.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── KPI cards ─────────────────────────────────────────────────────────
    total     = len(import_data)
    avg_sal   = import_data['Salary'].mean()
    max_sal   = import_data['Salary'].max()
    countries = import_data['Country'].nunique()

    st.markdown(f"""
    <div class="stat-row">
      <div class="stat-card">
        <div class="stat-label">Total Respondents</div>
        <div class="stat-value blue">{total:,}</div>
        <div class="stat-delta">↑ Globally sourced</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Average Salary</div>
        <div class="stat-value green">${avg_sal:,.0f}</div>
        <div class="stat-delta">USD · Yearly</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Countries Covered</div>
        <div class="stat-value" style="color:#fb8500;">{countries}</div>
        <div class="stat-delta">After grouping</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Two-column layout ─────────────────────────────────────────────────
    col_left, col_right = st.columns([1, 2], gap="large")

    with col_left:
        # Country distribution pie
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-header">
          <div class="card-title">Respondents by <span>Country</span></div>
        </div>
        """, unsafe_allow_html=True)

        df_country = import_data.Country.value_counts().head(10)
        palette = [BLUE, INDIGO, TEAL, AMBER, RED,
                   "#4cc9f0", "#f72585", "#3a86ff", "#8338ec", "#06d6a0"]
        fig1, ax1 = plt.subplots(figsize=(4, 4))
        wedges, texts, autotexts = ax1.pie(
            df_country,
            labels=None,
            autopct="%1.0f%%",
            startangle=90,
            colors=palette,
            pctdistance=0.75,
            wedgeprops=dict(width=0.55, edgecolor='white', linewidth=2)
        )
        for at in autotexts:
            at.set_fontsize(8)
            at.set_color('#1a2035')
            at.set_fontweight('600')
        ax1.axis("equal")
        fig1.patch.set_facecolor('#ffffff')
        # Legend
        legend_patches = [mpatches.Patch(color=palette[i], label=df_country.index[i])
                          for i in range(len(df_country))]
        ax1.legend(handles=legend_patches, loc='lower center',
                   bbox_to_anchor=(0.5, -0.3), ncol=2,
                   fontsize=7.5, frameon=False,
                   labelcolor='#5a6785')
        fig1.tight_layout()
        st.pyplot(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Education breakdown
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-header">
          <div class="card-title">Salary by <span>Education</span></div>
        </div>
        """, unsafe_allow_html=True)

        df_edu = import_data.groupby('EdLevel')['Salary'].mean().sort_values()
        labels_short = {
            "Bachelor's degree": "Bachelor's",
            "Master's degree": "Master's",
            "Post grad": "Post Grad",
            "WAEC/NECO and it's equivalent worldwide": "WAEC/NECO"
        }
        df_edu.index = [labels_short.get(l, l) for l in df_edu.index]

        fig_edu, ax_edu = plt.subplots(figsize=(4, 2.8))
        bars = ax_edu.barh(df_edu.index, df_edu.values,
                           color=[BLUE, INDIGO, TEAL, AMBER],
                           height=0.55, edgecolor='none')
        for bar in bars:
            ax_edu.text(bar.get_width() + 800, bar.get_y() + bar.get_height() / 2,
                        f"${bar.get_width():,.0f}",
                        va='center', ha='left', fontsize=8,
                        color='#1a2035', fontweight='600')
        style_fig(fig_edu, ax_edu)
        ax_edu.set_xlabel('')
        ax_edu.set_xlim(0, df_edu.max() * 1.22)
        ax_edu.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
        ax_edu.set_title('')
        st.pyplot(fig_edu, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        # Salary by country bar
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-header">
          <div class="card-title">Mean Salary by <span>Country</span></div>
          <div class="period-tabs">
            <span class="period-tab active">USD</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        df_sal = import_data.groupby('Country')['Salary'].mean().sort_values(ascending=True)
        top15  = df_sal.tail(15)

        fig2, ax2 = plt.subplots(figsize=(7, 5))
        colors_bar = [BLUE if v >= df_sal.median() else '#c5cde8' for v in top15.values]
        ax2.barh(top15.index, top15.values, color=colors_bar, height=0.65, edgecolor='none')
        for i, (val, label) in enumerate(zip(top15.values, top15.index)):
            ax2.text(val + 600, i, f"${val:,.0f}",
                     va='center', fontsize=8.5, color='#1a2035', fontweight='600')
        style_fig(fig2, ax2)
        ax2.set_xlim(0, top15.max() * 1.2)
        ax2.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
        ax2.tick_params(axis='y', labelsize=9)
        fig2.tight_layout()
        st.pyplot(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Salary by experience line
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-header">
          <div class="card-title">Salary vs <span>Experience</span></div>
          <div class="period-tabs">
            <span class="period-tab active">Years</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        df_exp = import_data.groupby('YearsCodePro')['Salary'].mean().sort_index()

        fig3, ax3 = plt.subplots(figsize=(7, 3))
        ax3.fill_between(df_exp.index, df_exp.values,
                         alpha=0.12, color=BLUE)
        ax3.plot(df_exp.index, df_exp.values,
                 color=BLUE, linewidth=2.5, solid_capstyle='round')
        ax3.scatter(df_exp.index, df_exp.values,
                    color=BLUE, s=40, zorder=5, edgecolors='white', linewidths=1.5)
        style_fig(fig3, ax3)
        ax3.set_xlabel('Years of Professional Experience', fontsize=9, color='#8896b3')
        ax3.set_ylabel('Avg Salary (USD)', fontsize=9, color='#8896b3')
        ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1000:.0f}k'))
        fig3.tight_layout()
        st.pyplot(fig3, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Footer ────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="text-align:center;padding:2rem 0 .5rem;color:#b0bac9;font-size:.78rem;">
      DevSalaryIQ &nbsp;·&nbsp; Stack Overflow Survey 2021 &nbsp;·&nbsp;
      <span style="color:#4361ee;font-weight:700;">Powered by Random Forest</span>
    </div>
    """, unsafe_allow_html=True)
