"""
Ujian Akhir Semester — Pembelajaran Mesin (EL4010)
Universitas MDP — Model Validation and Generalization

Nama  : Agus Priyansah
NPM   : 2327270005
Kelas : 25/26/2/TE6A/EL4010

Regresi prediksi konsentrasi CO(GT) pada dataset Air Quality (UCI).
Pipeline: Task Conceptualization → Data Preparation → Model Selection → Final Evaluation
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# ---------------------------------------------------------------------------
# Konfigurasi
# ---------------------------------------------------------------------------
RANDOM_STATE = 42
DATA_PATH = Path(__file__).parent / "data" / "AirQualityUCI.csv"
OUTPUT_DIR = Path(__file__).parent / "output"
TARGET = "CO(GT)"
FEATURES = [
    "PT08.S1(CO)",
    "PT08.S2(NMHC)",
    "PT08.S3(NOx)",
    "PT08.S4(NO2)",
    "PT08.S5(O3)",
    "T",
    "RH",
    "AH",
]

TRAIN_RATIO = 0.60
VAL_RATIO = 0.20
TEST_RATIO = 0.20


def load_and_clean(path: Path) -> pd.DataFrame:
    """Load CSV UCI dan bersihkan missing value (-200)."""
    df = pd.read_csv(
        path,
        sep=";",
        decimal=",",
        na_values=["-200", -200],
        encoding="utf-8",
    )
    df.columns = df.columns.str.strip()
    df = df.drop(columns=[c for c in df.columns if c == "" or c.startswith("Unnamed")], errors="ignore")

    numeric_cols = FEATURES + [TARGET]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=[TARGET])
    return df


def split_data(X: pd.DataFrame, y: pd.Series):
    """Pisah Train (60%) / Validation (20%) / Test (20%)."""
    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=TEST_RATIO, random_state=RANDOM_STATE
    )
    val_size = VAL_RATIO / (TRAIN_RATIO + VAL_RATIO)
    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=val_size, random_state=RANDOM_STATE
    )
    return X_train, X_val, X_test, y_train, y_val, y_test


def evaluate(y_true, y_pred) -> dict:
    rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
    mae = float(mean_absolute_error(y_true, y_pred))
    r2 = float(r2_score(y_true, y_pred))
    return {"RMSE": rmse, "MAE": mae, "R2": r2}


def build_models() -> dict:
    """Pipeline: imputer + scaler + model (fit hanya di training)."""
    base_steps = [
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
    return {
        "Linear Regression": Pipeline(base_steps + [("model", LinearRegression())]),
        "Ridge": Pipeline(base_steps + [("model", Ridge(alpha=1.0))]),
        "Lasso": Pipeline(base_steps + [("model", Lasso(alpha=0.01, max_iter=10000))]),
        "Random Forest": Pipeline(
            [("imputer", SimpleImputer(strategy="median"))]
            + [("model", RandomForestRegressor(n_estimators=200, random_state=RANDOM_STATE))]
        ),
        "Gradient Boosting": Pipeline(
            [("imputer", SimpleImputer(strategy="median"))]
            + [("model", GradientBoostingRegressor(random_state=RANDOM_STATE))]
        ),
    }


def plot_results(y_test, predictions: dict, comparison_df: pd.DataFrame, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    # 1. Perbandingan metrik
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(comparison_df))
    width = 0.35
    ax.bar(x - width / 2, comparison_df["RMSE_Val"], width, label="Validation RMSE")
    ax.bar(x + width / 2, comparison_df["RMSE_Test"], width, label="Test RMSE")
    ax.set_xticks(x)
    ax.set_xticklabels(comparison_df["Model"], rotation=20, ha="right")
    ax.set_ylabel("RMSE (mg/m³)")
    ax.set_title("Perbandingan RMSE: Validation vs Test")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_dir / "01_rmse_comparison.png", dpi=150)
    plt.close(fig)

    # 2. Actual vs Predicted (model terbaik)
    best_model = comparison_df.iloc[0]["Model"]
    y_pred_best = predictions[best_model]
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(y_test, y_pred_best, alpha=0.4, edgecolors="none")
    lims = [min(y_test.min(), y_pred_best.min()), max(y_test.max(), y_pred_best.max())]
    ax.plot(lims, lims, "r--", lw=1.5, label="Ideal")
    ax.set_xlabel("Aktual CO(GT)")
    ax.set_ylabel("Prediksi CO(GT)")
    ax.set_title(f"Actual vs Predicted — {best_model} (Test Set)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_dir / "02_actual_vs_predicted.png", dpi=150)
    plt.close(fig)

    # 3. Residual plot
    residuals = y_test - y_pred_best
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.scatter(y_pred_best, residuals, alpha=0.4, edgecolors="none")
    ax.axhline(0, color="r", linestyle="--")
    ax.set_xlabel("Prediksi CO(GT)")
    ax.set_ylabel("Residual")
    ax.set_title(f"Residual Plot — {best_model}")
    fig.tight_layout()
    fig.savefig(output_dir / "03_residual_plot.png", dpi=150)
    plt.close(fig)

def main():
    print("=" * 60)
    print("UAS REGRESSION — AIR QUALITY DATASET")
    print("Agus Priyansah | NPM 2327270005 | Universitas MDP")
    print("=" * 60)

    # -----------------------------------------------------------------------
    # TAHAP 1: Task Conceptualization
    # -----------------------------------------------------------------------
    print("\n[TAHAP 1] Task Conceptualization")
    print(f"  Target   : {TARGET} (konsentrasi CO aktual, mg/m³)")
    print(f"  Fitur    : {len(FEATURES)} sensor + lingkungan")
    print("  Metrik   : RMSE, MAE, R²")
    print("  Split    : Train 60% | Validation 20% | Test 20%")

    # -----------------------------------------------------------------------
    # TAHAP 2: Data Collection & Preparation
    # -----------------------------------------------------------------------
    print("\n[TAHAP 2] Data Collection & Preparation")
    df = load_and_clean(DATA_PATH)
    print(f"  Baris setelah cleaning : {len(df)}")
    print(f"  Missing per fitur      :\n{df[FEATURES].isna().sum().to_string()}")

    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y)
    print(f"  Train      : {len(X_train)} sampel")
    print(f"  Validation : {len(X_val)} sampel")
    print(f"  Test       : {len(X_test)} sampel")

    # Korelasi (disimpan sebagai gambar)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(9, 7))
    sns.heatmap(
        df[FEATURES + [TARGET]].corr(),
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        ax=ax,
    )
    ax.set_title("Korelasi Fitur dan Target")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "00_correlation_heatmap.png", dpi=150)
    plt.close(fig)
    print(f"  Heatmap korelasi disimpan di {OUTPUT_DIR / '00_correlation_heatmap.png'}")

    # -----------------------------------------------------------------------
    # TAHAP 3: Model Training & Selection (pilih terbaik di Validation)
    # -----------------------------------------------------------------------
    print("\n[TAHAP 3] Model Training & Selection")
    models = build_models()
    val_results = []
    test_predictions = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        val_metrics = evaluate(y_val, model.predict(X_val))
        test_metrics = evaluate(y_test, model.predict(X_test))
        test_predictions[name] = model.predict(X_test)

        val_results.append(
            {
                "Model": name,
                "RMSE_Val": val_metrics["RMSE"],
                "MAE_Val": val_metrics["MAE"],
                "R2_Val": val_metrics["R2"],
                "RMSE_Test": test_metrics["RMSE"],
                "MAE_Test": test_metrics["MAE"],
                "R2_Test": test_metrics["R2"],
            }
        )
        print(
            f"  {name:20s} | Val RMSE={val_metrics['RMSE']:.4f} R²={val_metrics['R2']:.4f}"
            f" | Test RMSE={test_metrics['RMSE']:.4f} R²={test_metrics['R2']:.4f}"
        )

    comparison = pd.DataFrame(val_results).sort_values("RMSE_Val").reset_index(drop=True)
    best = comparison.iloc[0]
    comparison.to_csv(OUTPUT_DIR / "model_comparison.csv", index=False)

    # -----------------------------------------------------------------------
    # TAHAP 4: Final Evaluation & Generalization
    # -----------------------------------------------------------------------
    print("\n[TAHAP 4] Final Evaluation (Test Set)")
    print(f"  Model terpilih : {best['Model']}")
    print(f"  RMSE (Test)    : {best['RMSE_Test']:.4f} mg/m³")
    print(f"  MAE  (Test)    : {best['MAE_Test']:.4f} mg/m³")
    print(f"  R²   (Test)    : {best['R2_Test']:.4f}")

    gap = abs(best["RMSE_Val"] - best["RMSE_Test"])
    print(f"\n  Generalisasi   : selisih RMSE Val-Test = {gap:.4f}")
    if gap < 0.15:
        print("  >> Model cukup baik digeneralisasi (tidak overfitting berat).")
    else:
        print("  >> Perhatikan overfitting; pertimbangkan regularisasi lebih kuat.")

    plot_results(y_test, test_predictions, comparison, OUTPUT_DIR)
    print(f"\n  Grafik disimpan di folder: {OUTPUT_DIR}")
    print("\nSelesai.")


if __name__ == "__main__":
    main()
