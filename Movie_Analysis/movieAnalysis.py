import os
import pandas as pd

# 'data' klasöründe bulunan veriyi yükle
file_path = os.path.join(os.path.dirname(__file__), '../data/movies_data.pkl')
df = pd.read_pickle(file_path)  # Veriyi buradan yükle

# 1930'dan itibaren olan verileri alıyoruz
df_1930 = df[df['release_date'].str[:4].astype(int) >= 1930]

# 'decade' sütununu ekliyoruz (her 10 yıl için bir gruplama)
df_1930['decade'] = (df_1930['release_date'].str[:4].astype(int) // 10) * 10

# Türlerin yıllara göre sayısını bulmak için 'genre_names' sütununu explode ediyoruz
df_1930_exploded = df_1930.explode('genre_names')

# Her 10 yıllık dönem için hangi film türünden kaç adet olduğunu grupluyoruz
decade_count_df = df_1930_exploded.groupby(['decade', 'genre_names']).size().reset_index(name='count')

# Sonuçları CSV dosyasına kaydediyoruz
csv_output_path = os.path.join('data', 'decade_genre_popularity.csv')
decade_count_df.to_csv(csv_output_path, index=False)
print(f"1930'dan itibaren her 10 yılda film türlerinin popülaritesi '{csv_output_path}' dosyasına kaydedildi.")
