# Cara Upload ke GitHub & Dapatkan Link Colab

Ikuti langkah ini agar link **view** bisa dilampirkan di laporan UAS.

---

## Langkah 1 — Buat repository GitHub (Public)

1. Login ke https://github.com
2. Klik **New repository**
3. Nama contoh: `uas-air-quality-regression`
4. Visibility: **Public** (wajib agar dosen bisa view tanpa login)
5. **Create repository** (tanpa README jika sudah ada di lokal)

---

## Langkah 2 — Push project dari komputer

Jalankan di PowerShell (ganti `USERNAME` dan `REPO`):

```powershell
cd "d:\scripts\dataset Pembelajaran mesin"

git init
git add .
git commit -m "UAS regression Air Quality - train validation test pipeline"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

Jika diminta login, gunakan GitHub Personal Access Token sebagai password.

---

## Langkah 3 — Link untuk laporan

Setelah push, ganti `USERNAME` dan `REPO` di link berikut:

| Platform | Format link |
|----------|-------------|
| **GitHub** | `https://github.com/USERNAME/REPO` |
| **Colab** | `https://colab.research.google.com/github/USERNAME/REPO/blob/main/Air_Quality_UAS.ipynb` |
| **Notebook** | `https://github.com/USERNAME/REPO/blob/main/Air_Quality_UAS.ipynb` |

**Contoh** (jika username `johndoe`, repo `uas-air-quality-regression`):

- GitHub: https://github.com/johndoe/uas-air-quality-regression
- Colab: https://colab.research.google.com/github/johndoe/uas-air-quality-regression/blob/main/Air_Quality_UAS.ipynb

---

## Langkah 4 — Tes link Colab

1. Buka link Colab di browser
2. Klik **Run all** — dataset akan diunduh otomatis dari UCI
3. Pastikan semua cell berjalan tanpa error

---

## Langkah 5 — Copy ke laporan

Buka file `SUBMISSION_LINKS.md`, isi nama/NIM, paste link GitHub & Colab yang sudah jadi, lalu copy ke dokumen laporan UAS.

---

## Checklist sebelum submit

- [ ] Repository **Public**
- [ ] `Air_Quality_UAS.ipynb` ada di branch `main`
- [ ] `data/AirQualityUCI.csv` ikut di-push (atau Colab bisa download otomatis)
- [ ] Link Colab bisa dibuka tanpa login
- [ ] `SUBMISSION_LINKS.md` sudah diisi link final
- [ ] Notebook cell pertama sudah di-update link GitHub/Colab Anda
