# Ujian Akhir Semester — Pembelajaran Mesin

## Regresi Prediksi Konsentrasi CO pada Dataset Air Quality

| | |
|---|---|
| **Nama** | Agus Priyansah |
| **NPM** | 2327270005 |
| **Kelas** | TE6A/EL4010 |
| **Mata Kuliah** | Pembelajaran Mesin (EL4010) |
| **Institusi** | Universitas MDP |

---

## Lampiran Digital

| Platform | Tautan |
|----------|--------|
| Repositori GitHub | https://github.com/Arcadiavr/uas-air-quality-regression |
| Google Colab | https://colab.research.google.com/github/Arcadiavr/uas-air-quality-regression/blob/main/Air_Quality_UAS.ipynb |

---

## Dataset

| Sumber | Tautan |
|--------|--------|
| UCI Machine Learning Repository | https://archive.ics.uci.edu/dataset/360/air+quality |
| Unduhan resmi (ZIP) | https://archive.ics.uci.edu/static/public/360/air+quality.zip |

Dataset juga tersedia di `data/AirQualityUCI.csv`. Pada Google Colab, dataset akan diunduh otomatis dari UCI jika file lokal tidak ditemukan.

---

## Struktur Repositori

```
Air_Quality_UAS.ipynb       — Notebook analisis utama
LAMPIRAN_LINK.md            — Lampiran tautan untuk laporan
requirements.txt            — Daftar library Python
data/AirQualityUCI.csv      — Dataset
output/                     — Grafik dan tabel hasil evaluasi
```

---

## Hasil Evaluasi (Test Set)

| Model | RMSE | MAE | R² |
|-------|------|-----|-----|
| Linear Regression | 0.613 | — | 0.820 |
| Ridge | 0.613 | — | 0.820 |
| Lasso | 0.617 | — | 0.817 |
| **Random Forest** | **0.539** | **0.306** | **0.861** |
| Gradient Boosting | 0.548 | — | 0.856 |

Model **Random Forest** dipilih berdasarkan RMSE terendah pada validation set.

---

## Referensi

- De Vito, S., et al. (2008). https://doi.org/10.1016/j.snb.2008.01.035
- UCI Air Quality: https://archive.ics.uci.edu/dataset/360/air+quality
- scikit-learn: https://scikit-learn.org/stable/supervised_learning.html#regression
