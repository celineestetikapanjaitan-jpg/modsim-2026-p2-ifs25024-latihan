import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Dashboard Analisis Kuesioner",
    page_icon="📊",
    layout="wide",
)

# =========================
# CUSTOM CSS STYLE
# =========================
st.markdown("""
<style>
.main {
    background-color: #f4f6f9;
}
.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
}
.big-title {
    font-size: 42px;
    font-weight: 700;
    color: white;
}
.hero {
    background: linear-gradient(135deg,#4e73df,#1cc88a);
    padding: 40px;
    border-radius: 20px;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HERO HEADER
# =========================
st.markdown("""
<div class="hero">
<div class="big-title">📊 Dashboard Analisis Kuesioner</div>
<p style="color:white;font-size:18px;">
Visualisasi interaktif hasil survei responden
</p>
</div>
""", unsafe_allow_html=True)

# =========================
# LOAD DATA
# =========================
df = pd.read_excel("data_kuesioner.xlsx")
questions = [c for c in df.columns if c.startswith("Q")]

skala_order = ["SS", "S", "CS", "CTS", "TS", "STS"]

score_map = {
    "SS": 6, "S": 5, "CS": 4,
    "CTS": 3, "TS": 2, "STS": 1
}

kategori_map = {
    "SS": "Positif", "S": "Positif",
    "CS": "Netral",
    "CTS": "Negatif", "TS": "Negatif", "STS": "Negatif"
}

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.header("🔎 Filter")
selected_question = st.sidebar.selectbox(
    "Pilih Pertanyaan",
    ["Semua"] + questions
)

# =========================
# PREP DATA
# =========================
long_df = df.melt(
    id_vars=["Partisipan"],
    value_vars=questions,
    var_name="Pertanyaan",
    value_name="Jawaban"
)

if selected_question != "Semua":
    long_df = long_df[long_df["Pertanyaan"] == selected_question]

# =========================
# METRIC SECTION
# =========================
col1, col2, col3 = st.columns(3)

total_responden = df["Partisipan"].nunique()
total_jawaban = len(long_df)
avg_global = df[questions].replace(score_map).mean().mean()

col1.markdown(f"""
<div class="metric-card">
<h3>👥 Total Responden</h3>
<h2>{total_responden}</h2>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="metric-card">
<h3>📝 Total Jawaban</h3>
<h2>{total_jawaban}</h2>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="metric-card">
<h3>⭐ Rata-rata Global</h3>
<h2>{round(avg_global,2)}</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# TABS SECTION
# =========================
tab1, tab2, tab3 = st.tabs(["📊 Distribusi", "📈 Rata-rata Skor", "📌 Kategori"])

# =========================
# TAB 1
# =========================
with tab1:
    overall_count = long_df["Jawaban"].value_counts().reindex(skala_order)

    fig1 = px.bar(
        x=overall_count.index,
        y=overall_count.values,
        color=overall_count.index,
        title="Distribusi Jawaban",
        template="plotly_white"
    )
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.pie(
        names=overall_count.index,
        values=overall_count.values,
        hole=0.5,
        title="Proporsi Jawaban",
        template="plotly_white"
    )
    st.plotly_chart(fig2, use_container_width=True)

# =========================
# TAB 2
# =========================
with tab2:
    score_df = df[questions].replace(score_map)
    avg_scores = score_df.mean()

    fig3 = px.bar(
        x=avg_scores.index,
        y=avg_scores.values,
        color=avg_scores.values,
        color_continuous_scale="viridis",
        title="Rata-rata Skor per Pertanyaan",
        template="plotly_white"
    )
    st.plotly_chart(fig3, use_container_width=True)

# =========================
# TAB 3
# =========================
with tab3:
    long_df["Kategori"] = long_df["Jawaban"].map(kategori_map)
    cat_count = long_df["Kategori"].value_counts()

    fig4 = px.bar(
        x=cat_count.index,
        y=cat_count.values,
        color=cat_count.index,
        title="Distribusi Kategori",
        template="plotly_white"
    )
    st.plotly_chart(fig4, use_container_width=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("© 2026 | Dashboard Kuesioner Interaktif | Dibuat dengan Streamlit & Plotly")