import pandas as pd
import matplotlib.pyplot as plt
from Cgi.cgi_operations import get_cgi_movies  # Cgi klasöründeki cgi_operations'dan içe aktar

def visualize_cgi_movies(df):
    # CGI filmleri için 'Title' ve 'Year' bilgilerini al
    cgi_movies_df = get_cgi_movies(df)  # Veriyi almak için fonksiyonu çağır

    if cgi_movies_df.empty:
        print("No CGI movies found for visualization.")
        return

    # Görselleştirmek için DataFrame'e dönüştür
    plt.figure(figsize=(10, 6))
    plt.barh(cgi_movies_df['Series_Title'], cgi_movies_df['IMDB_Rating'], color='skyblue')
    plt.xlabel('IMDB Puanı')
    plt.title('CGI Filmleri IMDB Puanları')
    plt.xlim(0, 10)  # Puan aralığı 0-10
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()
