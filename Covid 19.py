import pandas as pd
import matplotlib.pyplot as plt

# Dataset COVID-19 Indonesia dari GitHub
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_cases.csv'

# Load data
df = pd.read_csv(url)

# Ambil data Indonesia
indonesia = df[['date', 'Indonesia']].dropna()
indonesia.columns = ['Tanggal', 'Kasus_Baru']
indonesia['Tanggal'] = pd.to_datetime(indonesia['Tanggal'])

# Tampilkan beberapa data
print(indonesia.tail())

# Visualisasi kasus harian
plt.figure(figsize=(10,5))
plt.plot(indonesia['Tanggal'], indonesia['Kasus_Baru'], color='blue')
plt.title('Kasus Harian COVID-19 di Indonesia')
plt.xlabel('Tanggal')
plt.ylabel('Kasus Baru')
plt.grid(True)
plt.tight_layout()
plt.show()