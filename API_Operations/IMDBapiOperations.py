import pandas as pd
import os

# Dosya yolu
file_path = os.path.join(os.path.dirname(__file__), '../data/imdb_top_1000.csv')

# CSV dosyasını yükle
df = pd.read_csv(file_path)

# İlgili sütunları seç
df_selected = df[['Series_Title', 'Released_Year', 'Genre', 'IMDB_Rating', 'Meta_score', 
                  'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'No_of_Votes', 'Gross']]

# Seçilen veriyi görüntüle
print(df_selected.head())

# Temizlenmiş veriyi kaydet
cleaned_file_path = os.path.join(os.path.dirname(__file__), '../data/imdb_clean_data.csv')
df_selected.to_csv(cleaned_file_path, index=False)
