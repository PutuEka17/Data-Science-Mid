import pandas as pd
import os

# ==========================================================
# ASSESSMENT 3 TABEL DATA EKONOMI
# ==========================================================

print("=" * 70)
print("ASSESSMENT DATA EKONOMI WORLD BANK API")
print("=" * 70)


# ==========================================================
# 1. MEMBACA 3 TABEL
# ==========================================================

economic_macro = pd.read_csv(
    "data/raw/economic_macro.csv"
)

economic_labor = pd.read_csv(
    "data/raw/economic_labor.csv"
)

economic_trade = pd.read_csv(
    "data/raw/economic_trade.csv"
)


# ==========================================================
# FUNGSI ASSESSMENT
# ==========================================================

def assessment_table(df, table_name):

    print("\n")
    print("=" * 70)
    print(f"ASSESSMENT {table_name}")
    print("=" * 70)

    # ------------------------------------------------------
    # A. Ukuran Data
    # ------------------------------------------------------

    print("\n1. UKURAN DATA")
    print(f"Jumlah baris : {df.shape[0]}")
    print(f"Jumlah kolom : {df.shape[1]}")

    # ------------------------------------------------------
    # B. Nama Kolom
    # ------------------------------------------------------

    print("\n2. NAMA KOLOM")
    print(df.columns.tolist())

    # ------------------------------------------------------
    # C. Lima Data Pertama
    # ------------------------------------------------------

    print("\n3. LIMA DATA PERTAMA")
    print(df.head())

    # ------------------------------------------------------
    # D. Tipe Data
    # ------------------------------------------------------

    print("\n4. TIPE DATA")
    print(df.dtypes)

    # ------------------------------------------------------
    # E. Missing Value
    # ------------------------------------------------------

    print("\n5. MISSING VALUE")
    print(df.isnull().sum())

    # ------------------------------------------------------
    # F. Persentase Missing Value
    # ------------------------------------------------------

    print("\n6. PERSENTASE MISSING VALUE")

    missing_percentage = (
        df.isnull().sum() / len(df) * 100
    )

    print(missing_percentage)

    # ------------------------------------------------------
    # G. Data Duplikat
    # ------------------------------------------------------

    print("\n7. DATA DUPLIKAT")
    print(
        "Jumlah data duplikat:",
        df.duplicated().sum()
    )

    # ------------------------------------------------------
    # H. Statistik Deskriptif
    # ------------------------------------------------------

    print("\n8. STATISTIK DESKRIPTIF")

    print(
        df.describe(
            include="all"
        )
    )

    # ------------------------------------------------------
    # I. Jumlah Nilai Unik
    # ------------------------------------------------------

    print("\n9. JUMLAH NILAI UNIK")

    print(df.nunique())

    # ------------------------------------------------------
    # J. Informasi Data
    # ------------------------------------------------------

    print("\n10. INFORMASI DATA")

    df.info()


# ==========================================================
# 2. ASSESSMENT TABEL 1
# ==========================================================

assessment_table(
    economic_macro,
    "TABEL MAKROEKONOMI"
)


# ==========================================================
# 3. ASSESSMENT TABEL 2
# ==========================================================

assessment_table(
    economic_labor,
    "TABEL KETENAGAKERJAAN"
)


# ==========================================================
# 4. ASSESSMENT TABEL 3
# ==========================================================

assessment_table(
    economic_trade,
    "TABEL PERDAGANGAN"
)


# ==========================================================
# 5. MENYIMPAN HASIL ASSESSMENT
# ==========================================================

os.makedirs(
    "data/assessed",
    exist_ok=True
)


# ----------------------------------------------------------
# Assessment Tabel 1
# ----------------------------------------------------------

assessment_macro = pd.DataFrame({
    "Variable": economic_macro.columns,
    "Data_Type": economic_macro.dtypes.astype(str),
    "Missing_Value": economic_macro.isnull().sum().values,
    "Missing_Percentage":
        (
            economic_macro.isnull().sum()
            / len(economic_macro)
            * 100
        ).values,
    "Unique_Value":
        economic_macro.nunique().values
})


# ----------------------------------------------------------
# Assessment Tabel 2
# ----------------------------------------------------------

assessment_labor = pd.DataFrame({
    "Variable": economic_labor.columns,
    "Data_Type": economic_labor.dtypes.astype(str),
    "Missing_Value": economic_labor.isnull().sum().values,
    "Missing_Percentage":
        (
            economic_labor.isnull().sum()
            / len(economic_labor)
            * 100
        ).values,
    "Unique_Value":
        economic_labor.nunique().values
})


# ----------------------------------------------------------
# Assessment Tabel 3
# ----------------------------------------------------------

assessment_trade = pd.DataFrame({
    "Variable": economic_trade.columns,
    "Data_Type": economic_trade.dtypes.astype(str),
    "Missing_Value": economic_trade.isnull().sum().values,
    "Missing_Percentage":
        (
            economic_trade.isnull().sum()
            / len(economic_trade)
            * 100
        ).values,
    "Unique_Value":
        economic_trade.nunique().values
})


# ==========================================================
# 6. SIMPAN HASIL ASSESSMENT
# ==========================================================

assessment_macro.to_csv(
    "data/assessed/assessment_macro.csv",
    index=False
)

assessment_labor.to_csv(
    "data/assessed/assessment_labor.csv",
    index=False
)

assessment_trade.to_csv(
    "data/assessed/assessment_trade.csv",
    index=False
)


# ==========================================================
# 7. SELESAI
# ==========================================================

print("\n")
print("=" * 70)
print("ASSESSMENT SELESAI")
print("=" * 70)

print("\nFile assessment yang dibuat:")

print(
    "1. data/assessed/assessment_macro.csv"
)

print(
    "2. data/assessed/assessment_labor.csv"
)

print(
    "3. data/assessed/assessment_trade.csv"
)