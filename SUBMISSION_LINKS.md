# Lampiran Link — UAS Pembelajaran Mesin

**Copy bagian ini ke laporan / dokumen pengumpulan UAS.**

---

## Identitas

| | |
|---|---|
| Nama | [NAMA LENGKAP] |
| NIM | [NIM] |
| Kelas | 25/26/2/TE6A/EL4010 |
| Mata Kuliah | Pembelajaran Mesin — UAS |
| Tugas | Regression — Dataset Air Quality (No. 1) |

---

## 1. Link GitHub & Google Colab (akses view)

| Platform | Link |
|----------|------|
| **GitHub Repository** | https://github.com/Arcadiavr/uas-air-quality-regression |
| **Google Colab (view & run)** | https://colab.research.google.com/github/Arcadiavr/uas-air-quality-regression/blob/main/Air_Quality_UAS.ipynb |
| **Notebook di GitHub** | https://github.com/Arcadiavr/uas-air-quality-regression/blob/main/Air_Quality_UAS.ipynb |
| **Profil GitHub** | https://github.com/Arcadiavr |

> Repository **Public** — dosen dapat membuka tanpa login.

---

## 2. Link Dataset

| Sumber | Link |
|--------|------|
| UCI — Air Quality Dataset | https://archive.ics.uci.edu/dataset/360/air+quality |
| Download ZIP (official) | https://archive.ics.uci.edu/static/public/360/air+quality.zip |

**Dataset dalam repository:** `data/AirQualityUCI.csv`

---

## 3. Referensi Paper

1. **De Vito, S., Massera, E., Piga, M., Martinotto, L., & Francia, G. (2008).** On field calibration of an electronic nose for benzene estimation in an urban pollution monitoring scenario. *Sensors and Actuators B: Chemical*, 129(2), 750–757.  
   https://doi.org/10.1016/j.snb.2008.01.035

2. **De Vito, S., et al. (2008).** Evidences of cross-sensitivities and sensor drifts in air quality chemical sensor devices. *Sensors and Actuators B*, Vol. 129(2).  
   https://archive.ics.uci.edu/dataset/360/air+quality

3. **UCI Machine Learning Repository (2016).** Air Quality Data Set. Donated by Saverio De Vito.  
   https://archive.ics.uci.edu/dataset/360/air+quality

---

## 4. Referensi Code / Implementasi

| No. | Deskripsi | Link |
|-----|-----------|------|
| 1 | scikit-learn — Supervised Learning (Regression) | https://scikit-learn.org/stable/supervised_learning.html#regression |
| 2 | scikit-learn — `train_test_split` | https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html |
| 3 | scikit-learn — `Pipeline` | https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html |
| 4 | scikit-learn — `RandomForestRegressor` | https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html |
| 5 | scikit-learn — `GradientBoostingRegressor` | https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html |
| 6 | scikit-learn — Regression metrics | https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics |
| 7 | UCI — Import dataset dengan Python | https://archive.ics.uci.edu/datasets |

---

## 5. Ringkasan Metode

| Tahap | Kegiatan |
|-------|----------|
| Task Conceptualization | Target: `CO(GT)`; metrik: RMSE, MAE, R² |
| Data Preparation | Cleaning `-200`, split Train 60% / Val 20% / Test 20% |
| Model Training & Selection | Linear, Ridge, Lasso, Random Forest, Gradient Boosting |
| Final Evaluation | Test set; model terbaik: Random Forest (R² ≈ 0.86) |
