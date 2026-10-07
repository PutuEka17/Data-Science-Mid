import pandas as pd
import os

# ==========================================================
# CLEANING 3 TABEL DATA EKONOMI
# ==========================================================

print("=" * 70)
print("CLEANING DATA EKONOMI WORLD BANK API")
print("=" * 70)


# ==========================================================
# 1. MEMBUAT FOLDER CLEANED
# ==========================================================

os.makedirs("data/cleaned", exist_ok=True)


# ==========================================================
# 2. FUNGSI CLEANING
# ==========================================================

def clean_table(df, table_name):

    print("\n" + "=" * 70)
    print(f"CLEANING: {table_name}")
    print("=" * 70)

    # ------------------------------------------------------
    # KONDISI SEBELUM CLEANING
    # ------------------------------------------------------

    print("\n[SEBELUM CLEANING]")

    print("Jumlah baris :", len(df))
    print("Jumlah kolom :", len(df.columns))

    print("\nMissing value:")
    print(df.isnull().sum())

    print("\nJumlah duplikat:")
    print(df.duplicated().sum())


    # ------------------------------------------------------
    # 1. MENGHAPUS DATA DUPLIKAT
    # ------------------------------------------------------

    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        df = df.drop_duplicates()
        print(f"\n{duplicate_count} data duplikat dihapus.")
    else:
        print("\nTidak terdapat data duplikat.")


    # ------------------------------------------------------
    # 2. MEMBERSIHKAN KOLOM IDENTITAS
    # ------------------------------------------------------

    # Country merupakan identitas utama negara.
    # Jika Country kosong, baris tidak dapat digunakan
    # untuk analisis berdasarkan negara.

    if "Country" in df.columns:
        missing_country = df["Country"].isnull().sum()

        if missing_country > 0:
            df = df.dropna(subset=["Country"])
            print(
                f"{missing_country} baris dengan Country kosong dihapus."
            )


    # ------------------------------------------------------
    # 3. MEMBERSIHKAN COUNTRY CODE
    # ------------------------------------------------------

    # Country_Code merupakan kode negara.
    # Kita tidak mengisi dengan kode negara lain karena
    # hal tersebut dapat menghasilkan identitas negara yang salah.

    if "Country_Code" in df.columns:

        missing_code = df["Country_Code"].isnull().sum()

        if missing_code > 0:

            # Jika Country_Code kosong, kita tidak langsung
            # mengisinya dengan nilai mode.
            # Nilai kosong ditandai sebagai UNKNOWN agar
            # identitas negara tidak tertukar.

            df["Country_Code"] = df["Country_Code"].fillna(
                "UNKNOWN"
            )

            print(
                f"{missing_code} Country_Code kosong "
                f"diubah menjadi 'UNKNOWN'."
            )


    # ------------------------------------------------------
    # 4. MEMBERSIHKAN VARIABEL NUMERIK
    # ------------------------------------------------------

    numeric_columns = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    print("\nKolom numerik yang diproses:")

    for column in numeric_columns:

        missing = df[column].isnull().sum()

        if missing > 0:

            median_value = df[column].median()

            df[column] = df[column].fillna(
                median_value
            )

            print(
                f"- {column}: "
                f"{missing} missing value "
                f"diisi dengan median "
                f"({median_value:.2f})"
            )

        else:
            print(
                f"- {column}: tidak ada missing value"
            )


    # ------------------------------------------------------
    # 5. MEMBERSIHKAN DATA STRING
    # ------------------------------------------------------

    string_columns = df.select_dtypes(
        include=["object"]
    ).columns

    for column in string_columns:

        if column == "Country_Code":
            continue

        missing = df[column].isnull().sum()

        if missing > 0:

            mode_value = df[column].mode()

            if len(mode_value) > 0:

                df[column] = df[column].fillna(
                    mode_value.iloc[0]
                )

                print(
                    f"- {column}: "
                    f"{missing} missing value "
                    f"diisi dengan modus."
                )


    # ------------------------------------------------------
    # 6. RESET INDEX
    # ------------------------------------------------------

    df = df.reset_index(drop=True)


    # ------------------------------------------------------
    # KONDISI SETELAH CLEANING
    # ------------------------------------------------------

    print("\n[SETELAH CLEANING]")

    print("Jumlah baris :", len(df))
    print("Jumlah kolom :", len(df.columns))

    print("\nMissing value:")
    print(df.isnull().sum())

    print("\nJumlah duplikat:")
    print(df.duplicated().sum())

    print("\n5 data pertama:")
    print(df.head())

    return df


# ==========================================================
# 3. TABEL 1 — MAKROEKONOMI
# ==========================================================

macro = pd.read_csv(
    "data/raw/economic_macro.csv"
)

macro_clean = clean_table(
    macro,
    "TABEL 1 - MAKROEKONOMI"
)

macro_clean.to_csv(
    "data/cleaned/economic_macro_clean.csv",
    index=False
)

print(
    "\nTabel makroekonomi berhasil disimpan:"
)

print(
    "data/cleaned/economic_macro_clean.csv"
)


# ==========================================================
# 4. TABEL 2 — KETENAGAKERJAAN
# ==========================================================

labor = pd.read_csv(
    "data/raw/economic_labor.csv"
)

labor_clean = clean_table(
    labor,
    "TABEL 2 - KETENAGAKERJAAN"
)

labor_clean.to_csv(
    "data/cleaned/economic_labor_clean.csv",
    index=False
)

print(
    "\nTabel ketenagakerjaan berhasil disimpan:"
)

print(
    "data/cleaned/economic_labor_clean.csv"
)


# ==========================================================
# 5. TABEL 3 — PERDAGANGAN
# ==========================================================

trade = pd.read_csv(
    "data/raw/economic_trade.csv"
)

trade_clean = clean_table(
    trade,
    "TABEL 3 - PERDAGANGAN"
)

trade_clean.to_csv(
    "data/cleaned/economic_trade_clean.csv",
    index=False
)

print(
    "\nTabel perdagangan berhasil disimpan:"
)

print(
    "data/cleaned/economic_trade_clean.csv"
)


# ==========================================================
# 6. PEMERIKSAAN AKHIR
# ==========================================================

print("\n" + "=" * 70)
print("CLEANING SELESAI")
print("=" * 70)

print("\nFile cleaned yang tersedia:")

files = [
    "data/cleaned/economic_macro_clean.csv",
    "data/cleaned/economic_labor_clean.csv",
    "data/cleaned/economic_trade_clean.csv"
]

for file in files:

    print(
        os.path.exists(file),
        "→",
        file
    )

print("\nSemua tabel telah melalui proses cleaning.")