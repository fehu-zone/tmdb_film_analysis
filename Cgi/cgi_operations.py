import pandas as pd
from Normalizations.title_normalizations import normalize_title  # Normalizations klasöründen içe aktar

# CGI filmleri listesi kategorilere ayrılmış şekilde
cgi_movies_1970s = [
    "A Clockwork Orange", "Star Wars", "Close Encounters of the Third Kind",
    "The Black Hole", "Alien"
]

cgi_movies_1980s = [
    "Tron", "The Last Starfighter", "Ghostbusters",
    "The Terminator", "Robocop"
]

cgi_movies_1990s = [
    "Jurassic Park", "Terminator 2: Judgment Day", "The Matrix",
    "Toy Story", "Starship Troopers"
]

cgi_movies_2000s_onward = [
    "Gladiator", "Final Fantasy: The Spirits Within", 
    "The Lord of the Rings: The Fellowship of the Ring", "Spider-Man",
    "Finding Nemo", "The Incredibles", "King Kong", 
    "Transformers", "Avatar", "Toy Story 3"
]

# Eksik CGI filmleri manuel olarak ekle
missing_cgi_movies = [
    # 1970'ler
    "The Black Hole", 
    
    # 1980'ler
    "Tron", "The Last Starfighter", "Robocop",
    
    # 1990'lar
    "Starship Troopers",
    
    # 2000-2010
    "Final Fantasy: The Spirits Within", "Spider-Man", "Transformers"
]

# CGI filmlerini filtreleme fonksiyonu
def get_cgi_movies(df):
    # Normalize edilmiş başlıkları almak
    df['Normalized_Title'] = df['Series_Title'].apply(normalize_title)
    
    # Tüm kategorilerden normalize edilmiş başlıkları al
    normalized_cgi_titles = []
    for category in [cgi_movies_1970s, cgi_movies_1980s, cgi_movies_1990s, cgi_movies_2000s_onward]:
        normalized_cgi_titles.extend([normalize_title(title) for title in category])

    # CGI filmleri veri çerçevesini döndür
    cgi_df = df[df['Normalized_Title'].isin(normalized_cgi_titles)].copy()
    
    # Manuel olarak eklediğimiz filmleri DataFrame'e ekleyelim
    for title in missing_cgi_movies:
        normalized_title = normalize_title(title)
        # Eğer bu başlık zaten veri çerçevesinde yoksa ekle
        if not cgi_df['Normalized_Title'].isin([normalized_title]).any():
            new_row = pd.DataFrame([{'Series_Title': title, 'Normalized_Title': normalized_title}])
            cgi_df = pd.concat([cgi_df, new_row], ignore_index=True)
            print(f"Manuel ekleme yapıldı: {title}")  # Hata ayıklama için eklenen başlık

    # CGI filmlerini yazdır
    print("Elde edilen CGI filmleri:")
    print(cgi_df[['Series_Title', 'Normalized_Title']])  # Hangi filmlerin eklendiğini görmek için

    return cgi_df
