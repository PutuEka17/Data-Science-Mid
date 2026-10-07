import pandas as pd
import os

# ==========================================================
# LANGKAH 7
# MEMBENTUK 3 TABEL DATA EKONOMI
# ==========================================================

print("=" * 70)
print("MEMBENTUK 3 TABEL DATA EKONOMI")
print("=" * 70)

# ==========================================================
# 1. MEMBACA DATA HASIL EXTRACT API
# ==========================================================

input_file = "data/raw/world_bank_economic_2023.csv"

print("\nMembaca data:")
print(input_file)

df = pd.read_csv(input_file)

print("\nData berhasil dibaca.")

print("Jumlah baris :", df.shape[0])
print("Jumlah kolom :", df.shape[1])

print("\nKolom yang tersedia:")
print(df.columns.tolist())


# ==========================================================
# 2. MEMBUAT FOLDER OUTPUT
# ==========================================================

os.makedirs("data/raw", exist_ok=True)


# ==========================================================
# 3. TABEL 1 — MAKROEKONOMI
# ==========================================================

economic_macro = df[
    [
        "Country",
        "Country_Code",
        "Year",
        "GDP",
        "GDP_Per_Capita",
        "GDP_Growth",
        "Inflation"
    ]
].copy()

print("\n" + "=" * 70)
print("TABEL 1 — MAKROEKONOMI")
print("=" * 70)

print(economic_macro.head())

print("\nUkuran Tabel 1:")
print(economic_macro.shape)


# ==========================================================
# 4. TABEL 2 — KETENAGAKERJAAN
# ==========================================================

economic_labor = df[
    [
        "Country",
        "Country_Code",
        "Year",
        "Unemployment"
    ]
].copy()

print("\n" + "=" * 70)
print("TABEL 2 — KETENAGAKERJAAN")
print("=" * 70)

print(economic_labor.head())

print("\nUkuran Tabel 2:")
print(economic_labor.shape)


# ==========================================================
# 5. TABEL 3 — PERDAGANGAN
# ==========================================================

economic_trade = df[
    [
        "Country",
        "Country_Code",
        "Year",
        "Exports",
        "Imports"
    ]
].copy()

print("\n" + "=" * 70)
print("TABEL 3 — PERDAGANGAN")
print("=" * 70)

print(economic_trade.head())

print("\nUkuran Tabel 3:")
print(economic_trade.shape)


# ==========================================================
# 6. MENYIMPAN TABEL 1
# ==========================================================

economic_macro.to_csv(
    "data/raw/economic_macro.csv",
    index=False
)

print("\nTabel 1 berhasil disimpan:")
print("data/raw/economic_macro.csv")


# ==========================================================
# 7. MENYIMPAN TABEL 2
# ==========================================================

economic_labor.to_csv(
    "data/raw/economic_labor.csv",
    index=False
)

print("\nTabel 2 berhasil disimpan:")
print("data/raw/economic_labor.csv")


# ==========================================================
# 8. MENYIMPAN TABEL 3
# ==========================================================

economic_trade.to_csv(
    "data/raw/economic_trade.csv",
    index=False
)

print("\nTabel 3 berhasil disimpan:")
print("data/raw/economic_trade.csv")


# ==========================================================
# 9. PEMERIKSAAN FILE
# ==========================================================

print("\n" + "=" * 70)
print("PEMBENTUKAN 3 TABEL SELESAI")
print("=" * 70)

print("\nFile yang tersedia:")

print(
    os.path.exists("data/raw/economic_macro.csv"),
    "→ economic_macro.csv"
)

print(
    os.path.exists("data/raw/economic_labor.csv"),
    "→ economic_labor.csv"
)

print(
    os.path.exists("data/raw/economic_trade.csv"),
    "→ economic_trade.csv"
)

print("\nSemua tabel berhasil dibuat.")