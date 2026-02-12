import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# LOAD DATA
# =========================
df = pd.read_excel("data_kuesioner.xlsx")

questions = [c for c in df.columns if c.startswith("Q")]

skala_order = ["SS", "S", "CS", "CTS", "TS", "STS"]

score_map = {
    "SS": 6,
    "S": 5,
    "CS": 4,
    "CTS": 3,
    "TS": 2,
    "STS": 1
}

kategori_map = {
    "SS": "Positif",
    "S": "Positif",
    "CS": "Netral",
    "CTS": "Negatif",
    "TS": "Negatif",
    "STS": "Negatif"
}

st.title("📊 Dashboard Visualisasi Kuesioner")

# =========================
# PREP DATA
# =========================
long_df = df.melt(id_vars=["Partisipan"],
                  value_vars=questions,
                  var_name="Pertanyaan",
                  value_name="Jawaban")

# =========================
# 1. BAR CHART KESELURUHAN
# =========================
overall_count = long_df["Jawaban"].value_counts().reindex(skala_order)

fig1 = px.bar(
    x=overall_count.index,
    y=overall_count.values,
    labels={"x": "Skala", "y": "Jumlah"},
    title="Distribusi Jawaban Keseluruhan"
)
st.plotly_chart(fig1, use_container_width=True)

# =========================
# 2. PIE CHART
# =========================
fig2 = px.pie(
    names=overall_count.index,
    values=overall_count.values,
    title="Proporsi Jawaban"
)
st.plotly_chart(fig2, use_container_width=True)

# =========================
# 3. STACKED BAR PER PERTANYAAN
# =========================
stack_df = (
    long_df.groupby(["Pertanyaan", "Jawaban"])
    .size()
    .reset_index(name="Jumlah")
)

fig3 = px.bar(
    stack_df,
    x="Pertanyaan",
    y="Jumlah",
    color="Jawaban",
    barmode="stack",
    title="Distribusi Jawaban per Pertanyaan"
)
st.plotly_chart(fig3, use_container_width=True)

# =========================
# 4. RATA-RATA SKOR PER PERTANYAAN
# =========================
score_df = df[questions].replace(score_map)
avg_scores = score_df.mean()

fig4 = px.bar(
    x=avg_scores.index,
    y=avg_scores.values,
    labels={"x": "Pertanyaan", "y": "Rata-rata Skor"},
    title="Rata-rata Skor per Pertanyaan"
)
st.plotly_chart(fig4, use_container_width=True)

# =========================
# 5. KATEGORI POSITIF/NETRAL/NEGATIF
# =========================
long_df["Kategori"] = long_df["Jawaban"].map(kategori_map)
cat_count = long_df["Kategori"].value_counts()

fig5 = px.bar(
    x=cat_count.index,
    y=cat_count.values,
    title="Distribusi Kategori Jawaban"
)
st.plotly_chart(fig5, use_container_width=True)
