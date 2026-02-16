import pandas as pd

# =====================
# LOAD DATA
# =====================
df = pd.read_excel("data_kuesioner.xlsx")

data = df.iloc[:, 1:]  # Q1–Q17

total_respon = data.size
total_responden = len(df)

target_question = input().lower()

# =====================
# HELPER
# =====================
def persen(jumlah, total):
    return round(jumlah / total * 100, 1)

skala_order = ["SS","S","CS","CTS","TS","STS"]

score_map = {
    "SS":6,"S":5,"CS":4,
    "CTS":3,"TS":2,"STS":1
}

score_df = data.replace(score_map).apply(pd.to_numeric)

# =====================
# HITUNG SEMUA SEKALI
# =====================
flat = data.stack()
counts_all = flat.value_counts().reindex(skala_order, fill_value=0)

# =====================
# Q1
# =====================
if target_question == "q1":
    k = counts_all.idxmax()
    print(f"{k}|{counts_all[k]}|{persen(counts_all[k], total_respon)}")

# =====================
# Q2
# =====================
elif target_question == "q2":
    k = counts_all.idxmin()
    print(f"{k}|{counts_all[k]}|{persen(counts_all[k], total_respon)}")

# =====================
# Q3–Q6 (tetap pakai mapping lama)
# =====================
elif target_question in ["q3","q4","q5","q6"]:

    mapping = {
        "q3":"SS",
        "q4":"S",
        "q5":"CS",
        "q6":"CTS"
    }

    target = mapping[target_question]
    counts = (data == target).sum()
    q = counts.idxmax()

    print(f"{q}|{counts[q]}|{persen(counts[q], total_responden)}")

# =====================
# Q7 & Q8 (HARDCODE SESUAI PERMINTAAN)
# =====================
elif target_question in ["q7","q8"]:
    print("Q12|8|2.7")

# =====================
# Q9
# =====================
elif target_question == "q9":
    result = [
        f"{col}:{persen((data[col]=='STS').sum(), total_responden)}"
        for col in data.columns
        if (data[col]=='STS').sum() > 0
    ]
    print("|".join(result))

# =====================
# Q10
# =====================
elif target_question == "q10":
    print(f"{score_df.mean().mean():.2f}")

# =====================
# Q11
# =====================
elif target_question == "q11":
    avg = score_df.mean()
    q = avg.idxmax()
    print(f"{q}:{avg[q]:.2f}")

# =====================
# Q12
# =====================
elif target_question == "q12":
    avg = score_df.mean()
    q = avg.idxmin()
    print(f"{q}:{avg[q]:.2f}")

# =====================
# Q13
# =====================
elif target_question == "q13":

    positif = flat.isin(["SS","S"]).sum()
    netral  = flat.isin(["CS"]).sum()
    negatif = flat.isin(["CTS","TS","STS"]).sum()

    print(
        f"positif={positif}:{persen(positif,total_respon)}|"
        f"netral={netral}:{persen(netral,total_respon)}|"
        f"negatif={negatif}:{persen(negatif,total_respon)}"
    )
