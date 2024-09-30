import pandas as pd
import os
import matplotlib.pyplot as plt

# Dosya yolu
file_path = os.path.join(os.path.dirname(__file__), '../data/movies_data.pkl')
df = pd.read_pickle(file_path)  # Dosyayı buradan yükle

# CGI ile ilgili verileri hazırlama (1990'dan itibaren)
cgi_start_year = 1990
df_cgi = df[df['release_date'].str[:4].astype(int) >= cgi_start_year]

# 'decade' sütununu ekliyoruz
df_cgi['decade'] = (df_cgi['release_date'].str[:4].astype(int) // 10) * 10

# Türlerin yıllara göre izlenme sayısını bulma
popularity_by_genre = df_cgi.explode('genre_names').groupby(['decade', 'genre_names']).size().reset_index(name='count')

# Çizgi grafiği oluşturma
plt.figure(figsize=(12, 6))
for genre in popularity_by_genre['genre_names'].unique():
    genre_data = popularity_by_genre[popularity_by_genre['genre_names'] == genre]
    plt.plot(genre_data['decade'], genre_data['count'], marker='o', label=genre)

plt.title("CGI Kullanımı ile Film Türlerinin İzlenme Sayıları Arasındaki İlişki")
plt.xlabel("Yıllar")
plt.ylabel("Film Sayısı")
plt.xticks(popularity_by_genre['decade'].unique())
plt.legend(title='Film Türleri', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.tight_layout()
plt.show()
