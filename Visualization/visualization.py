import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mplcursors

# Dosya yolu
file_path = os.path.join(os.path.dirname(__file__), '../data/movies_data.pkl')
df = pd.read_pickle(file_path)  # Dosyayı buradan yükle

# 'release_date' bilgisi boşsa, varsayılan bir tarih ekliyoruz
df['release_date'] = df['release_date'].fillna('1900-01-01')

# Yıl sütununu ekliyoruz
df['year'] = df['release_date'].str[:4].astype(int)

# 10 yıllık dönemleri gruplandırmak için 'decade' sütunu ekliyoruz
df['decade'] = (df['year'] // 10) * 10

# 'genre_names' sütununu patlatmak için 'explode' kullanıyoruz
df_exploded = df.explode('genre_names')

# Hangi film türlerinin hangi dönemde olduğunu sayıyoruz
decade_count_df = df_exploded.groupby(['decade', 'genre_names']).size().reset_index(name='count')

# CGI sonrası veriler (1990 sonrası)
df_cgi = df[df['year'] >= 1990]

# 'genre_names' sütununu explode ederek türleri ayırıyoruz
df_cgi_exploded = df_cgi.explode('genre_names')

# CGI sonrası film türlerini ve yılları gruplandırıp sayıyoruz (1990 sonrası)
cgi_count_df = df_cgi_exploded.groupby(['year', 'genre_names']).size().reset_index(name='count')

# Grafikleri yan yana yerleştirmek için iki subplot kullanıyoruz
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# 1930'dan itibaren her 10 yıllık film türü analiz çizgi grafiği
sns.lineplot(x='decade', y='count', hue='genre_names', data=decade_count_df, marker='o', ax=ax1)
ax1.set_title("1930'dan İtibaren Her 10 Yılda Film Türlerinin Popülaritesi", fontsize=16)
ax1.set_xlabel("On Yıllık Dönemler", fontsize=12)
ax1.set_ylabel("Film Sayısı", fontsize=12)
ax1.grid(True)

# Interaktif noktalar için mplcursors kullanımı (1930 sonrası)
mplcursors.cursor(ax1, hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(
        f"On Yıl: {int(sel.target[0])}\nTür: {sel.artist.get_label()}\nFilm Sayısı: {int(sel.target[1])}"))

# 1990'dan itibaren CGI kullanımına göre film türlerinin çizgi grafiği
sns.lineplot(x='year', y='count', hue='genre_names', data=cgi_count_df, marker='o', ax=ax2)
ax2.set_title("1990'dan İtibaren CGI Kullanımına Göre Film Türlerinin Popülaritesi", fontsize=16)
ax2.set_xlabel("Yıl", fontsize=12)
ax2.set_ylabel("Film Sayısı", fontsize=12)
ax2.grid(True)

# Interaktif noktalar için mplcursors kullanımı (CGI sonrası)
mplcursors.cursor(ax2, hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(
        f"Yıl: {int(sel.target[0])}\nTür: {sel.artist.get_label()}\nFilm Sayısı: {int(sel.target[1])}"))

# Grafikleri daha iyi yerleştirmek için layout ayarları
plt.tight_layout()
plt.show()
