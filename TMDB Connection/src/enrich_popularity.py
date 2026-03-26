from src.tmdb_connection import search_title, get_details

def get_popularity(title):
    item = search_title(title)
    if not item:
        return None

    details = get_details(item["media_type"], item["id"])
    return details.get("popularity")

def categorize_popularity(value):
    if value is None:
        return None
    if value == 0:
        return "Sin actividad"
    if 0 < value <= 10:
        return "Poco visto"
    if 10 < value <= 100:
        return "Moderadamente popular"
    if 100 < value <= 1000:
        return "Muy popular"
    if value > 1000:
        return "Extremadamente popular"
    
