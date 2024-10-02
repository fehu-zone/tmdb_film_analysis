import pandas as pd
from API_Operations.IMDBapiOperations import df_selected  # IMDb verisini içe aktar
from Visualization.visualization import visualize_cgi_movies  # Görselleştirme fonksiyonunu içe aktar

def main():
    # CGI filmlerinin görselleştirilmesi
    visualize_cgi_movies(df_selected)

if __name__ == "__main__":
    main()
