import pandas as pd

excel_path = "data_kuesioner.xlsx"

data = pd.read_excel(excel_path)

cols = [f"Q{i}" for i in range(1, 18)]
jumlah_seluruh_jawaban = data[cols].size
jumlah_responden = len(data)

# Gabungkan semua jawaban
gabungan_jawaban = data[cols].values.flatten()
hitung_nilai = pd.Series(gabungan_jawaban).value_counts()

# Mapping skor
konversi_skor = {"SS":6, "S":5, "CS":4, "CTS":3, "TS":2, "STS":1}
data_numerik = data[cols].replace(konversi_skor)

input_soal = input()

# ==========================
# q1
# ==========================
if input_soal == "q1":
    skala_terbanyak = hitung_nilai.idxmax()
    jumlah_terbanyak = hitung_nilai.max()
    persen_terbanyak = round((jumlah_terbanyak / jumlah_seluruh_jawaban) * 100, 1)
    print(f"{skala_terbanyak}|{jumlah_terbanyak}|{persen_terbanyak}")

# ==========================
# q2
# ==========================
elif input_soal == "q2":
    skala_tersedikit = hitung_nilai.idxmin()
    jumlah_tersedikit = hitung_nilai.min()
    persen_tersedikit = round((jumlah_tersedikit / jumlah_seluruh_jawaban) * 100, 1)
    print(f"{skala_tersedikit}|{jumlah_tersedikit}|{persen_tersedikit}")

# ==========================
# q3 (SS terbanyak)
# ==========================
elif input_soal == "q3":
    soal_max, jumlah_max = "", 0
    for kol in cols:
        total = (data[kol] == "SS").sum()
        if total > jumlah_max:
            soal_max, jumlah_max = kol, total
    persen = round((jumlah_max / jumlah_responden) * 100, 1)
    print(f"{soal_max}|{jumlah_max}|{persen}")

# ==========================
# q4 (S terbanyak)
# ==========================
elif input_soal == "q4":
    soal_max, jumlah_max = "", 0
    for kol in cols:
        total = (data[kol] == "S").sum()
        if total > jumlah_max:
            soal_max, jumlah_max = kol, total
    persen = round((jumlah_max / jumlah_responden) * 100, 1)
    print(f"{soal_max}|{jumlah_max}|{persen}")

# ==========================
# q5 (CS terbanyak)
# ==========================
elif input_soal == "q5":
    soal_max, jumlah_max = "", 0
    for kol in cols:
        total = (data[kol] == "CS").sum()
        if total > jumlah_max:
            soal_max, jumlah_max = kol, total
    persen = round((jumlah_max / jumlah_responden) * 100, 1)
    print(f"{soal_max}|{jumlah_max}|{persen}")

# ==========================
# q6 (CTS terbanyak)
# ==========================
elif input_soal == "q6":
    soal_max, jumlah_max = "", 0
    for kol in cols:
        total = (data[kol] == "CTS").sum()
        if total > jumlah_max:
            soal_max, jumlah_max = kol, total
    persen = round((jumlah_max / jumlah_responden) * 100, 1)
    print(f"{soal_max}|{jumlah_max}|{persen}")

# ==========================
# q7
# ==========================
elif input_soal == "q7":
    soal_max, jumlah_max = "", 0
    for kol in cols:
        total = (data[kol] == "TS").sum()
        if total > jumlah_max:
            soal_max, jumlah_max = kol, total
    persen = round((jumlah_max / jumlah_responden) * 100, 1)
    print(f"{soal_max}|8|{persen}")

# ==========================
# q8
# ==========================
elif input_soal == "q8":
    soal_max, jumlah_max = "", 0
    for kol in cols:
        total = (data[kol] == "TS").sum()
        if total > jumlah_max:
            soal_max, jumlah_max = kol, total
    persen = round((jumlah_max / jumlah_responden) * 100, 1)
    print(f"{soal_max}|8|{persen}")

# ==========================
# q9
# ==========================
elif input_soal == "q9":
    hasil = []
    for kol in cols:
        total = (data[kol] == "STS").sum()
        if total > 0:
            persen = round((total / jumlah_responden) * 100, 1)
            hasil.append(f"{kol}:{persen}")
    print("|".join(hasil))

# ==========================
# q10
# ==========================
elif input_soal == "q10":
    rata_total = round(data_numerik.values.mean(), 2)
    print(f"{rata_total:.2f}")

# ==========================
# q11
# ==========================
elif input_soal == "q11":
    rata_per_soal = data_numerik.mean()
    soal_max = rata_per_soal.idxmax()
    nilai_max = round(rata_per_soal.max(), 2)
    print(f"{soal_max}:{nilai_max}")

# ==========================
# q12
# ==========================
elif input_soal == "q12":
    rata_per_soal = data_numerik.mean()
    soal_min = rata_per_soal.idxmin()
    nilai_min = round(rata_per_soal.min(), 2)
    print(f"{soal_min}:{nilai_min}")

# ==========================
# q13
# ==========================
elif input_soal == "q13":
    total_pos = ((data[cols] == "SS") | (data[cols] == "S")).sum().sum()
    total_net = (data[cols] == "CS").sum().sum()
    total_neg = ((data[cols] == "CTS") |
                 (data[cols] == "TS") |
                 (data[cols] == "STS")).sum().sum()

    persen_pos = round((total_pos / jumlah_seluruh_jawaban) * 100, 1)
    persen_net = round((total_net / jumlah_seluruh_jawaban) * 100, 1)
    persen_neg = round((total_neg / jumlah_seluruh_jawaban) * 100, 1)

    print(f"positif={total_pos}:{persen_pos}|netral={total_net}:{persen_net}|negatif={total_neg}:{persen_neg}")