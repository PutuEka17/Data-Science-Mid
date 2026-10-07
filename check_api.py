import requests
import pandas as pd

# ==========================================================
# PEMERIKSAAN WORLD BANK API
# ==========================================================

print("=" * 70)
print("PEMERIKSAAN DATA EKONOMI WORLD BANK API")
print("=" * 70)

# ----------------------------------------------------------
# 1. Parameter API
# ----------------------------------------------------------

indicator = "NY.GDP.PCAP.CD"
year = 2023

url = (
    f"https://api.worldbank.org/v2/"
    f"country/all/indicator/{indicator}"
    f"?date={year}&format=json&per_page=1000"
)

print("\nURL API:")
print(url)

# ----------------------------------------------------------
# 2. Request API
# ----------------------------------------------------------

response = requests.get(url)

print("\nStatus Code:")
print(response.status_code)

# ----------------------------------------------------------
# 3. Periksa response
# ----------------------------------------------------------

if response.status_code == 200:

    data = response.json()

    print("\nAPI berhasil diakses.")

    # ------------------------------------------------------
    # 4. Ambil data
    # ------------------------------------------------------

    records = data[1]

    df = pd.DataFrame(records)

    print("\nJumlah baris:")
    print(len(df))

    print("\nNama kolom:")
    print(df.columns.tolist())

    print("\n5 data pertama:")
    print(df.head())

    print("\nInformasi dataset:")
    print(df.info())

else:

    print("\nAPI gagal diakses.")
    print("Status:", response.status_code)