import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize_numeric_columns(df, numeric_columns):
    """
    Sayısal sütunların MinMaxScaler ile 0-1 aralığında normalizasyonu.

    Parametreler:
    df: Pandas DataFrame - Normalizasyon yapılacak veri seti.
    numeric_columns: list - Normalizasyon yapılacak sayısal sütunlar listesi.

    Geri dönen:
    df: Pandas DataFrame - Normalleştirilmiş veri seti.
    """
    # Eksik değerleri ortalama ile dolduralım
    for col in numeric_columns:
        df[col].fillna(df[col].mean(), inplace=True)

    # MinMaxScaler kullanarak normalizasyon
    scaler = MinMaxScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    
    return df

# Örnek kullanım
if __name__ == "__main__":
    # CSV dosyasını yükleme
    file_path = '../data/imdb_top_1000.csv'  # Kendi dosya yolunuza göre güncelleyin
    df = pd.read_csv(file_path)

    # Normalizasyon yapılacak sayısal sütunlar
    numeric_columns = ['IMDB_Rating', 'Meta_score', 'No_of_Votes', 'Gross']

    # Normalizasyon işlemini gerçekleştirme
    df = normalize_numeric_columns(df, numeric_columns)

    # Sonucu kaydetme
    df.to_csv('../data/imdb_normalized_data.csv', index=False)
