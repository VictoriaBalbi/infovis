import pandas as pd
import requests
import time
import urllib.parse

API_KEY = "8f258076b0df2391298a90c1512ffd76"
BASE_URL = "https://api.themoviedb.org/3"
IMG_BASE = "https://image.tmdb.org/t/p/w200"

df = pd.read_csv('data/flourish_final.csv')
titles = df['title'].tolist()

def search_series(title):
    query = urllib.parse.quote(title)
    url = f"{BASE_URL}/search/tv?api_key={API_KEY}&query={query}&language=es-ES"
    try:
        r = requests.get(url, timeout=10)
        results = r.json().get('results', [])
        if results and results[0].get('poster_path'):
            return IMG_BASE + results[0]['poster_path']
    except:
        pass
    return ""

images = {}
for title in titles:
    img = search_series(title)
    images[title] = img
    status = "OK" if img else "NO"
    print(f"{status} - {title}")
    time.sleep(0.25)

df['image'] = df['title'].map(images)
df.to_csv('flourish_series_horas_img.csv', index=False)
print(f"\nListo! Encontrados: {sum(1 for v in images.values() if v)}/{len(images)}")