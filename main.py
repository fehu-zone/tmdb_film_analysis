import requests  # API ile veri çekmek için gerekli kütüphane
import pandas as pd  # Veriyi işlemek ve tablo olarak saklamak için

# TMDb API anahtarını buraya ekliyoruz
api_key = 'YOUR_TMDB_API_KEY'  # TMDb'den aldığın API anahtarını buraya yaz

# TMDb'den film verilerini çekmek için kullanılacak temel URL
base_url = "https://api.themoviedb.org/3/discover/movie"

def get_movies_by_year(year, api_key):
    """
    Belirli bir yıldaki popüler filmleri TMDb API ile çeker.
    Parametreler:
        year (int): Filmlerin hangi yıldan çekileceğini belirler.
        api_key (str): API anahtarını kullanarak TMDb'ye erişim sağlar.
    """
    # API'ye göndereceğimiz parametreler
    params = {
        'api_key': api_key,  # TMDb API anahtarı
        'language': 'en-US',  # İngilizce sonuçlar
        'sort_by': 'popularity.desc',  # Popülerliğe göre sıralama
        'primary_release_year': year,  # Belirli bir yılın verilerini çekiyoruz
        'page': 1  # İlk sayfayı çekiyoruz
    }

    # API'ye GET isteği gönderiyoruz
    response = requests.get(base_url, params=params)

    # Eğer başarılı bir cevap alırsak (status_code 200), veriyi al
    if response.status_code == 200:
        data = response.json()  # Cevabı JSON formatında alıyoruz
        return data['results']  # Sonuçları döndürüyoruz
    else:
        print(f"Error: {response.status_code}")  # Eğer hata varsa, hata kodunu yazdır
        return None

def get_genres(api_key):
    """
    TMDb API'den film türlerini (janr) çeker.
    """
    genre_url = "https://api.themoviedb.org/3/genre/movie/list"  # Film türleri için URL
    params = {
        'api_key': api_key,  # API anahtarını kullanıyoruz
        'language': 'en-US'  # İngilizce sonuçlar
    }

    # API'ye GET isteği gönderiyoruz
    response = requests.get(genre_url, params=params)

    # Eğer başarılı bir cevap alırsak, janr verisini al
    if response.status_code == 200:
        return response.json()['genres']  # Tüm janrları döndürüyoruz
    else:
        print(f"Error: {response.status_code}")  # Eğer hata varsa, hata kodunu yazdır
        return None

# Tüm film türlerini (janr) alıyoruz
genres = get_genres(api_key)
# Janr ID'lerini, janr isimlerine eşleştiren bir sözlük oluşturuyoruz
genre_dict = {genre['id']: genre['name'] for genre in genres}

# 1930'lardan başlayarak her 10 yıllık dönem için en popüler filmleri çekiyoruz
decades = [1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2023]

all_movies = []  # Tüm filmleri saklamak için boş bir liste

# Her 10 yıllık dilim için verileri çekiyoruz
for year in decades:
    movies = get_movies_by_year(year, api_key)  # Yıl bazlı filmleri çekiyoruz
    if movies:
        all_movies.extend(movies)  # Eğer film varsa, tüm filmleri listeye ekle

# Çektiğimiz tüm verileri DataFrame'e çeviriyoruz
df_all_movies = pd.DataFrame(all_movies)

# Film türlerini (janr) DataFrame'e ekliyoruz
df_all_movies['genre_names'] = df_all_movies['genre_ids'].apply(lambda x: [genre_dict.get(i) for i in x])

# Veriyi 'data' klasörüne kaydediyoruz
df_all_movies.to_pickle('data/movies_data.pkl')  # Veriyi 'data/movies_data.pkl' dosyasına kaydediyoruz

print("Veri çekme işlemi tamamlandı ve dosyaya kaydedildi.")
