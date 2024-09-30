import requests
import pandas as pd
import os

# 'data' klasörünün var olup olmadığını kontrol et, yoksa oluştur
if not os.path.exists('data'):
    os.makedirs('data')

# API anahtarını buraya ekliyoruz
api_key = '14137c24b9825da634b9dbf967068220'

base_url = "https://api.themoviedb.org/3/discover/movie"

def get_movies_by_year(year, api_key, max_pages=5):
    """
    Belirli bir yıl için TMDb API üzerinden film verilerini çeker.
    max_pages: Her yıl için çekilecek sayfa sayısı (Her sayfada 20 film bulunur).
    """
    all_movies = []
    for page in range(1, max_pages + 1):
        params = {
            'api_key': api_key,
            'language': 'en-US',
            'sort_by': 'popularity.desc',
            'primary_release_year': year,
            'page': page
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            all_movies.extend(data['results'])
        else:
            print(f"Error for year {year}, page {page}: {response.status_code}")
            break  # Eğer bir hata varsa, döngüden çıkıyoruz
    return all_movies

# Genre adlarını almak için gerekli kodu burada ekle
def get_genres(api_key):
    genre_url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        'api_key': api_key,
        'language': 'en-US'
    }
    response = requests.get(genre_url, params=params)
    if response.status_code == 200:
        return response.json()['genres']
    else:
        print(f"Error: {response.status_code}")
        return None

# Türleri id'lerinden isimlerine çevirebilmek için genre sözlüğünü oluştur
genres = get_genres(api_key)
genre_dict = {genre['id']: genre['name'] for genre in genres}

# Tüm filmleri tutacak bir liste
all_movies = []

# 1930'dan 2023'e kadar her 10 yılda en çok izlenen filmleri al
for year in range(1930, 2024, 10):
    movies = get_movies_by_year(year, api_key, max_pages=5)  # Her yıl için 5 sayfa veri çek
    if movies:
        all_movies.extend(movies)  # Gelen filmleri listeye ekle

# DataFrame oluştur
df_all_movies = pd.DataFrame(all_movies)

# Genre adlarını DataFrame'e ekle
genre_names = []
for movie in all_movies:
    movie_genres = movie.get('genre_ids', [])
    genre_names.append([genre_dict.get(gid) for gid in movie_genres])

df_all_movies['genre_names'] = genre_names

# Eğer DataFrame boşsa bir hata mesajı ver
if df_all_movies.empty:
    print("Hiçbir film verisi alınamadı.")
else:
    # Veriyi 'data/movies_data.pkl' dosyasına kaydediyoruz
    df_all_movies.to_pickle('data/movies_data.pkl')
    print(f"Toplam {len(df_all_movies)} film verisi alındı ve kaydedildi.")
