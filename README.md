# UAS Pembelajaran Mesin — Regression: Air Quality Dataset

**Universitas MDP** | EL4010 Pembelajaran Mesin | Model Validation and Generalization

Regresi untuk memprediksi konsentrasi CO (`CO(GT)`) dari dataset Air Quality (UCI), dengan pipeline **Train / Validation / Test** sesuai materi kuliah.

---

## Link Pengumpulan (untuk laporan UAS)

| Item | Link |
|------|------|
| **GitHub Repository** (view) | https://github.com/Arcadiavr/uas-air-quality-regression |
| **Google Colab** (view) | https://colab.research.google.com/github/Arcadiavr/uas-air-quality-regression/blob/main/Air_Quality_UAS.ipynb |
| **Notebook langsung** | https://github.com/Arcadiavr/uas-air-quality-regression/blob/main/Air_Quality_UAS.ipynb |

---

## Dataset

| Item | Link |
|------|------|
| **UCI Machine Learning Repository** | https://archive.ics.uci.edu/dataset/360/air+quality |
| **Download dataset (ZIP)** | https://archive.ics.uci.edu/static/public/360/air+quality.zip |
| **File CSV di repo ini** | `data/AirQualityUCI.csv` |

**Deskripsi singkat:** Respons rata-rata per jam dari 5 sensor gas metal oxide di area perkotaan Italia (Maret 2004 – Februari 2005). Missing value ditandai dengan `-200`.

---

## Referensi Paper

| No. | Referensi | Link |
|-----|-----------|------|
| 1 | De Vito, S., et al. (2008). *On field calibration of an electronic nose for benzene estimation in an urban pollution monitoring scenario.* Sensors and Actuators B: Chemical. | https://doi.org/10.1016/j.snb.2008.01.035 |
| 2 | De Vito, S., et al. (2008). *Calibration and validation of gas sensor arrays for air quality monitoring.* Sensors and Actuators B, 129(2). (cross-sensitivity & drift) | https://archive.ics.uci.edu/dataset/360/air+quality |
| 3 | Tsanas, A., & Xifara, A. (2012). *Accurate quantitative estimation of energy performance...* (metodologi regresi ML — referensi metode) | https://archive.ics.uci.edu/dataset/242/energy+efficiency |

---

## Referensi Code / Library

| No. | Sumber | Link |
|-----|--------|------|
| 1 | scikit-learn — Regression | https://scikit-learn.org/stable/supervised_learning.html#regression |
| 2 | scikit-learn — `train_test_split` | https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html |
| 3 | scikit-learn — `RandomForestRegressor` | https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html |
| 4 | scikit-learn — Metrics (RMSE, MAE, R²) | https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics |
| 5 | UCI ML Repository — Python import | https://archive.ics.uci.edu/datasets |

---

## Struktur Proyek

```
├── Air_Quality_UAS.ipynb    # Notebook utama (GitHub / Colab)
├── air_quality_uas.py         # Script pipeline lengkap
├── SUBMISSION_LINKS.md        # Template link untuk copy ke laporan
├── requirements.txt
├── data/
│   └── AirQualityUCI.csv
└── output/
    ├── model_comparison.csv
    └── *.png                  # Grafik hasil
```

---

## Cara Menjalankan

### Lokal (Windows)

```powershell
cd "d:\scripts\dataset Pembelajaran mesin"
py -m pip install -r requirements.txt
py air_quality_uas.py
```

Atau buka `Air_Quality_UAS.ipynb` di VS Code / Jupyter.

### Google Colab

1. Upload repo ke GitHub (public).
2. Buka link Colab:
   https://colab.research.google.com/github/Arcadiavr/uas-air-quality-regression/blob/main/Air_Quality_UAS.ipynb
3. Jalankan semua cell — dataset akan diunduh otomatis dari UCI jika file lokal tidak ada.

---

## Upload ke GitHub (agar link view bisa dipakai)

```powershell
cd "d:\scripts\dataset Pembelajaran mesin"
git init
git add .
git commit -m "UAS regression Air Quality - train/val/test pipeline"
git branch -M main
git remote add origin https://github.com/Arcadiavr/uas-air-quality-regression.git
git push -u origin main
```

Pastikan repository **Public** agar dosen bisa membuka tanpa login.

---

## Hasil Model (Test Set)

| Model | RMSE | MAE | R² |
|-------|------|-----|-----|
| Linear Regression | 0.613 | — | 0.820 |
| Ridge | 0.613 | — | 0.820 |
| Lasso | 0.617 | — | 0.817 |
| **Random Forest** | **0.539** | **0.306** | **0.861** |
| Gradient Boosting | 0.548 | — | 0.856 |

Model terpilih: **Random Forest** (RMSE validation terendah).

---

## Identitas (isi sebelum submit)

| Field | Isi |
|-------|-----|
| Nama | _[Nama Anda]_ |
| NIM | _[NIM]_ |
| Kelas | 25/26/2/TE6A/EL4010 |
| Mata Kuliah | Pembelajaran Mesin — UAS |
