import requests
import pandas as pd
import os


# ==========================================================
# KONFIGURASI
# ==========================================================

YEAR = 2023

RAW_DIR = "data/raw"

os.makedirs(RAW_DIR, exist_ok=True)


# ==========================================================
# FUNGSI MENGAMBIL DATA WORLD BANK API
# ==========================================================

def get_world_bank_data(indicator, year):

    url = (
        f"https://api.worldbank.org/v2/"
        f"country/all/indicator/{indicator}"
        f"?date={year}&format=json&per_page=1000"
    )

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(
            f"Gagal mengambil data {indicator}. "
            f"Status code: {response.status_code}"
        )

    result = response.json()

    records = result[1]

    data = []

    for record in records:

        data.append({
            "Country": record["country"]["value"],
            "Country_Code": record["countryiso3code"],
            "Year": int(record["date"]),
            "Value": record["value"]
        })

    return pd.DataFrame(data)


# ==========================================================
# DAFTAR INDIKATOR
# ==========================================================

indicators = {

    # Tabel 1
    "GDP": "NY.GDP.MKTP.CD",
    "GDP_Per_Capita": "NY.GDP.PCAP.CD",
    "GDP_Growth": "NY.GDP.MKTP.KD.ZG",
    "Inflation": "FP.CPI.TOTL.ZG",

    # Tabel 2
    "Unemployment": "SL.UEM.TOTL.ZS",

    # Tabel 3
    "Exports": "NE.EXP.GNFS.CD",
    "Imports": "NE.IMP.GNFS.CD"
}


# ==========================================================
# AMBIL SEMUA DATA
# ==========================================================

dataframes = {}

for name, indicator_code in indicators.items():

    print(f"Mengambil {name}...")

    df = get_world_bank_data(
        indicator_code,
        YEAR
    )

    df = df.rename(
        columns={
            "Value": name
        }
    )

    dataframes[name] = df


# ==========================================================
# GABUNGKAN DATA SEMENTARA
# ==========================================================

combined = None

for name, df in dataframes.items():

    if combined is None:

        combined = df

    else:

        combined = combined.merge(
            df,
            on=[
                "Country",
                "Country_Code",
                "Year"
            ],
            how="outer"
        )


# ==========================================================
# SIMPAN RAW DATA
# ==========================================================

output_file = f"{RAW_DIR}/world_bank_economic_{YEAR}.csv"

combined.to_csv(
    output_file,
    index=False
)

print("\n" + "=" * 70)
print("EXTRACT SELESAI")
print("=" * 70)

print("\nJumlah data:")
print(combined.shape)

print("\nKolom:")
print(combined.columns.tolist())

print("\nFile disimpan:")
print(output_file)