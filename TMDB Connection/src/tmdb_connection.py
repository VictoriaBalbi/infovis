import requests
import time

API_KEY = "8f258076b0df2391298a90c1512ffd76"

#safe get por si TMDb  corta la conexión
def safe_get(url, params=None, retries=3, timeout=5):
    for i in range(retries):
        try:
            return requests.get(url, params=params, timeout=timeout).json()
        except Exception:
            time.sleep(1)
    return None

def search_title(title):
    url = "https://api.themoviedb.org/3/search/multi"
    params = {"api_key": API_KEY, "query": title}

    r = safe_get(url, params)
    if not r or not r.get("results"):
        return None

    return r["results"][0]


def get_details(media_type, tmdb_id):
    url = f"https://api.themoviedb.org/3/{media_type}/{tmdb_id}"
    return safe_get(url, {"api_key": API_KEY})

