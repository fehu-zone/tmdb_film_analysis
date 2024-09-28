import pandas as pd  # Veriyi yüklemek için
import matplotlib.pyplot as plt  # Grafikler çizmek için
import seaborn as sns  # Grafik stilini iyileştirmek için

# Veri dosyasını 'data' klasöründen yükleme
df = pd.read_pickle('../data/movies_data.pkl')  # 'data/movies_data.pkl' dosyasını yüklüyoruz

# Grafik stilini belirleyelim
sns.set(style="whitegrid")

# 1. Grafik: Film kategorilerine göre popülerlik
plt.figure(figsize=(10, 6))
sns.countplot(y='genre_names', data=df.explode('genre_names'), order=df.explode('genre_names')['genre_names'].value_counts().index)
plt.title('Popüler Film Kategorileri (1930-2023)')
plt.xlabel('Film Sayısı')
plt.ylabel('Kategori')
plt.tight_layout()
plt.show()

# 2. Grafik: Yıllara göre filmlerin popülerlik trendi
plt.figure(figsize=(10, 6))
sns.lineplot(x=pd.to_datetime(df['release_date']).dt.year, y='popularity', data=df)
plt.title('Yıllara Göre Filmlerin Popülerlik Trendi')
plt.xlabel('Yıl')
plt.ylabel('Popülerlik')
plt.tight_layout()
plt.show()
