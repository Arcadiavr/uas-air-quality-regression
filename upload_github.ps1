# Upload ke GitHub — Arcadiavr (tanpa kode browser)
# Metode: Personal Access Token (PAT) — paling stabil di Cursor terminal

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Upload UAS Air Quality ke GitHub" -ForegroundColor Cyan
Write-Host "  Akun: https://github.com/Arcadiavr" -ForegroundColor Gray
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# --- Cek sudah login? ---
$loggedIn = $false
try {
    gh auth status 2>$null | Out-Null
    if ($LASTEXITCODE -eq 0) { $loggedIn = $true }
} catch {}

if ($loggedIn) {
    Write-Host "[OK] Sudah login GitHub CLI" -ForegroundColor Green
} else {
    Write-Host "[!] Belum login. Pakai TOKEN (bukan kode browser)." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Buat token di browser:" -ForegroundColor White
    Write-Host "  1. Buka: https://github.com/settings/tokens/new" -ForegroundColor Gray
    Write-Host "  2. Note: UAS-upload" -ForegroundColor Gray
    Write-Host "  3. Centang: repo (full control)" -ForegroundColor Gray
    Write-Host "  4. Generate token -> COPY token (ghp_...)" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Paste token di bawah (tidak akan tampil saat mengetik):" -ForegroundColor White
    $token = Read-Host "GitHub Token"

    if (-not $token -or $token.Length -lt 20) {
        Write-Host "Token tidak valid. Coba lagi." -ForegroundColor Red
        exit 1
    }

  $token | gh auth login --with-token
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Login gagal. Cek token dan coba lagi." -ForegroundColor Red
        exit 1
    }
    Write-Host "[OK] Login berhasil!" -ForegroundColor Green
}

Write-Host ""
Write-Host "Mengupload ke GitHub..." -ForegroundColor Cyan

# Coba buat repo + push
gh repo create uas-air-quality-regression --public `
    --description "UAS Pembelajaran Mesin EL4010 - Air Quality Regression" `
    --source=. --remote=origin --push 2>$null

if ($LASTEXITCODE -ne 0) {
    Write-Host "Repo mungkin sudah ada, push langsung..." -ForegroundColor Yellow
    git remote remove origin 2>$null
    git remote add origin https://github.com/Arcadiavr/uas-air-quality-regression.git
    git push -u origin main
}

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "  BERHASIL UPLOAD!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "GitHub:" -ForegroundColor White
    Write-Host "  https://github.com/Arcadiavr/uas-air-quality-regression" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Google Colab:" -ForegroundColor White
    Write-Host "  https://colab.research.google.com/github/Arcadiavr/uas-air-quality-regression/blob/main/Air_Quality_UAS.ipynb" -ForegroundColor Cyan
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "Upload gagal. Kirim error di atas ke asisten." -ForegroundColor Red
    exit 1
}
