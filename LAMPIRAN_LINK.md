# Lampiran Tautan — UAS Pembelajaran Mesin

## Identitas Mahasiswa

| | |
|---|---|
| Nama | Agus Priyansah |
| NPM | 2327270005 |
| Kelas | TE6A/EL4010 |
| Mata Kuliah | Pembelajaran Mesin (EL4010) |
| Institusi | Universitas MDP |
| Jenis Tugas | Regression — Dataset Air Quality (No. 1) |

---

## 1. Tautan Repositori dan Google Colab

| Platform | Tautan |
|----------|--------|
| Repositori GitHub | https://github.com/Arcadiavr/uas-air-quality-regression |
| Google Colab | https://colab.research.google.com/github/Arcadiavr/uas-air-quality-regression/blob/main/Air_Quality_UAS.ipynb |
| Notebook | https://github.com/Arcadiavr/uas-air-quality-regression/blob/main/Air_Quality_UAS.ipynb |

---

## 2. Tautan Dataset

| Sumber | Tautan |
|--------|--------|
| UCI — Air Quality Dataset | https://archive.ics.uci.edu/dataset/360/air+quality |
| Unduhan resmi (ZIP) | https://archive.ics.uci.edu/static/public/360/air+quality.zip |

File dataset dalam repositori: `data/AirQualityUCI.csv`

---

## 3. Referensi Publikasi

1. De Vito, S., Massera, E., Piga, M., Martinotto, L., & Francia, G. (2008). On field calibration of an electronic nose for benzene estimation in an urban pollution monitoring scenario. *Sensors and Actuators B: Chemical*, 129(2), 750–757. https://doi.org/10.1016/j.snb.2008.01.035

2. De Vito, S., et al. (2008). Evidences of cross-sensitivities and sensor drifts in air quality chemical sensor devices. *Sensors and Actuators B*, 129(2). https://archive.ics.uci.edu/dataset/360/air+quality

3. UCI Machine Learning Repository (2016). Air Quality Data Set. Donated by Saverio De Vito. https://archive.ics.uci.edu/dataset/360/air+quality

---

## 4. Referensi Implementasi

| No. | Deskripsi | Tautan |
|-----|-----------|--------|
| 1 | scikit-learn — Supervised Learning (Regression) | https://scikit-learn.org/stable/supervised_learning.html#regression |
| 2 | scikit-learn — `train_test_split` | https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html |
| 3 | scikit-learn — `Pipeline` | https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html |
| 4 | scikit-learn — `RandomForestRegressor` | https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html |
| 5 | scikit-learn — `GradientBoostingRegressor` | https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html |
| 6 | scikit-learn — Regression metrics | https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics |

---

## 5. Ringkasan Metodologi

| Tahap | Kegiatan |
|-------|----------|
| Task Conceptualization | Target `CO(GT)`; metrik RMSE, MAE, dan R² |
| Data Preparation | Penanganan nilai hilang (`-200`), pembagian Train 60%, Validation 20%, Test 20% |
| Model Training & Selection | Linear Regression, Ridge, Lasso, Random Forest, Gradient Boosting |
| Final Evaluation | Evaluasi pada test set; model terpilih: Random Forest (R² ≈ 0,86) |
