import pandas as pd
import re

def normalize_title(title):
    # Büyük/küçük harf dönüşümü ve özel karakterlerin kaldırılması
    title = title.lower()  # Küçük harfe çevir
    title = re.sub(r'[-]', ' ', title)  # '-' işaretlerini boşluk ile değiştir
    title = re.sub(r'[:?]', '', title)  # ':' ve '?' işaretlerini kaldır
    title = re.sub(r'\s+', ' ', title)  # Birden fazla boşluğu tek boşlukla değiştir
    title = title.strip()  # Başında ve sonunda boşlukları kaldır

    # "the" ve "a" ile başlayan kelimeleri kaldır
    if title.startswith("the "):
        title = title[4:]  # "the " kelimesini kaldır
    elif title.startswith("a "):
        title = title[2:]  # "a " kelimesini kaldır

    return title
