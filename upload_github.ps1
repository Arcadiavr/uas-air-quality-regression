# Upload ke GitHub — Arcadiavr
# Jalankan sekali: gh auth login (jika belum login)
# Lalu jalankan script ini.

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "=== Upload UAS Air Quality ke GitHub ===" -ForegroundColor Cyan
Write-Host "Akun: https://github.com/Arcadiavr" -ForegroundColor Gray

# Cek login GitHub CLI
$authOk = $false
try {
    gh auth status 2>$null
    if ($LASTEXITCODE -eq 0) { $authOk = $true }
} catch {}

if (-not $authOk) {
    Write-Host ""
    Write-Host "Anda belum login GitHub CLI. Jalankan perintah berikut:" -ForegroundColor Yellow
    Write-Host "  gh auth login" -ForegroundColor White
    Write-Host ""
    Write-Host "Pilih: GitHub.com -> HTTPS -> Login with browser" -ForegroundColor Gray
    Write-Host "Setelah login, jalankan script ini lagi." -ForegroundColor Gray
    Write-Host ""
    $run = Read-Host "Jalankan gh auth login sekarang? (y/n)"
    if ($run -eq "y") {
        gh auth login
    } else {
        exit 1
    }
}

# Buat repo & push
Write-Host "Membuat repository dan push..." -ForegroundColor Green
gh repo create uas-air-quality-regression --public `
    --description "UAS Pembelajaran Mesin EL4010 - Air Quality Regression" `
    --source=. --remote=origin --push

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "BERHASIL! Link untuk laporan:" -ForegroundColor Green
    Write-Host "GitHub: https://github.com/Arcadiavr/uas-air-quality-regression"
    Write-Host "Colab:  https://colab.research.google.com/github/Arcadiavr/uas-air-quality-regression/blob/main/Air_Quality_UAS.ipynb"
} else {
    # Repo mungkin sudah ada, coba push saja
    Write-Host "Repo mungkin sudah ada, mencoba push..." -ForegroundColor Yellow
    git remote remove origin 2>$null
    git remote add origin https://github.com/Arcadiavr/uas-air-quality-regression.git
    git push -u origin main
}
