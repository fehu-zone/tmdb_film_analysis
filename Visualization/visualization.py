import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dosya yolu
file_path = os.path.join(os.path.dirname(__file__), '../data/movies_data.pkl')
df = pd.read_pickle(file_path)  # Dosyayı buradan yükle

# 'release_date' bilgisi boşsa, varsayılan bir tarih ekliyoruz
df['release_date'] = df['release_date'].fillna('1900-01-01')

# 10 yıllık dönemleri gruplandırmak için 'decade' sütunu ekliyoruz
df['decade'] = (df['release_date'].str[:4].astype(int) // 10) * 10

# 'genre_names' sütununu patlatmak için 'explode' kullanıyoruz
df_exploded = df.explode('genre_names')

# Hangi film türlerinin hangi dönemde olduğunu sayıyoruz
count_df = df_exploded.groupby(['genre_names', 'decade']).size().reset_index(name='count')

# Sütun grafiği için Seaborn kullanarak görselleştirme
plt.figure(figsize=(14, 8))
sns.barplot(x='decade', y='count', hue='genre_names', data=count_df, palette='tab20', dodge=True)

# Grafiği düzenleme
plt.title("10 Yıllık Periyotlarla En Çok Çekilen Film Türleri", fontsize=16)
plt.xlabel("Years", fontsize=12)
plt.ylabel("Number Of Movies", fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Movie Genres', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y')

plt.tight_layout()
plt.show()
