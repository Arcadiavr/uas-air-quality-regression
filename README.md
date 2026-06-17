# Ujian Akhir Semester — Pembelajaran Mesin

## Regresi Prediksi Konsentrasi CO pada Dataset Air Quality

| | |
|---|---|
| **Nama** | Agus Priyansah |
| **NPM** | 2327270005 |
| **Kelas** | TE6A/EL4010 |
| **Mata Kuliah** | Pembelajaran Mesin (EL4010) |
| **Institusi** | Universitas MDP |
| **Topik** | Model Validation and Generalization |

---

## Deskripsi

Penelitian ini membangun model regresi untuk memprediksi konsentrasi karbon monoksida (`CO(GT)`) berdasarkan respons sensor gas dan variabel lingkungan, menggunakan dataset Air Quality dari UCI Machine Learning Repository. Proses pengembangan model mengikuti pipeline pembelajaran mesin dengan pembagian data **training**, **validation**, dan **testing** untuk menilai kemampuan generalisasi model.

---

## Lampiran Digital

| Platform | Tautan |
|----------|--------|
| Repositori GitHub | https://github.com/Arcadiavr/uas-air-quality-regression |
| Google Colab | https://colab.research.google.com/github/Arcadiavr/uas-air-quality-regression/blob/main/Air_Quality_UAS.ipynb |
| Notebook | https://github.com/Arcadiavr/uas-air-quality-regression/blob/main/Air_Quality_UAS.ipynb |

---

## Dataset

| Sumber | Tautan |
|--------|--------|
| UCI Machine Learning Repository | https://archive.ics.uci.edu/dataset/360/air+quality |
| Unduhan resmi (ZIP) | https://archive.ics.uci.edu/static/public/360/air+quality.zip |

Dataset merekam respons rata-rata per jam dari lima sensor gas metal oxide yang dipasang di area perkotaan Italia (Maret 2004 – Februari 2005). Nilai hilang ditandai dengan `-200`.

---

## Referensi

### Publikasi

1. De Vito, S., Massera, E., Piga, M., Martinotto, L., & Francia, G. (2008). On field calibration of an electronic nose for benzene estimation in an urban pollution monitoring scenario. *Sensors and Actuators B: Chemical*, 129(2), 750–757. https://doi.org/10.1016/j.snb.2008.01.035

2. UCI Machine Learning Repository (2016). Air Quality Data Set. https://archive.ics.uci.edu/dataset/360/air+quality

### Implementasi

- scikit-learn — Regression: https://scikit-learn.org/stable/supervised_learning.html#regression
- scikit-learn — `train_test_split`: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
- scikit-learn — `RandomForestRegressor`: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
- scikit-learn — Regression metrics: https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics

---

## Hasil Evaluasi (Test Set)

| Model | RMSE | MAE | R² |
|-------|------|-----|-----|
| Linear Regression | 0.613 | — | 0.820 |
| Ridge | 0.613 | — | 0.820 |
| Lasso | 0.617 | — | 0.817 |
| **Random Forest** | **0.539** | **0.306** | **0.861** |
| Gradient Boosting | 0.548 | — | 0.856 |

Model **Random Forest** dipilih berdasarkan nilai RMSE terendah pada validation set dan menunjukkan performa konsisten pada test set.

---

## Struktur Repositori

```
Air_Quality_UAS.ipynb    — Notebook analisis utama
air_quality_uas.py       — Implementasi pipeline
data/AirQualityUCI.csv   — Dataset
output/                  — Grafik dan tabel hasil evaluasi
LAMPIRAN_LINK.md         — Lampiran tautan untuk laporan
```
